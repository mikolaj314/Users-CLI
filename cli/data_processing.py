import csv
import json
import os


from typing import Any, Dict, List
import xml.etree.ElementTree as ETree


from cli.tasks.validators import UserDataProcessor


class DataParser:
    def parse(self, file_path: str) -> List[Dict]:
        raise NotImplementedError(
            f'Subclasses must implement the parse method for a file "{file_path}".'
        )


class JsonParser(DataParser):
    def parse(self, file_path: str) -> List[Dict]:
        try:
            with open(file_path) as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            raise


class CsvParser(DataParser):
    def _parse_children(self, children_data: str) -> List[Dict[str, Any]]:
        children_list = []

        if children_data:
            for child in children_data.split(","):
                name, age = child.split()
                # strip round brackets "(12)" -> "12"
                age = age[1:-1]
                children_list.append({"name": name, "age": age})

        return children_list

    def parse(self, file_path: str) -> List[Dict]:
        try:
            with open(file_path, "r", newline="") as csv_file:
                csv_reader = csv.DictReader(csv_file, delimiter=";")
                data_list = []
                for row in csv_reader:
                    row: dict
                    children_list = self._parse_children(row.get("children", ""))
                    row["children"] = children_list
                    data_list.append(row)

            return data_list

        except FileNotFoundError:
            print(f"File not found: {file_path}")
            raise


class XmlParser(DataParser):
    def _parse_element_to_dict(self, element: ETree.Element) -> Dict:
        result = {}
        for sub_element in element:
            tag = sub_element.tag

            if len(sub_element) == 0:
                result[tag] = sub_element.text if sub_element.text is not None else []
            elif tag == "children":
                result[tag] = [
                    self._parse_element_to_dict(child)
                    for child in sub_element.findall("child")
                ]

        return result

    def parse(self, file_path: str) -> List[Dict]:
        try:
            tree = ETree.parse(file_path)
            root = tree.getroot()

            return [self._parse_element_to_dict(user) for user in root.findall("user")]
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            raise


class UnsupportedFileExtensionError(Exception):
    """Exception for unsupported file extensions."""
    pass


class DataMerger:
    SUPPORTED_EXTENSIONS = {".json", ".csv", ".xml"}
    SUPPORTED_PARSERS = {
        ".json": JsonParser(),
        ".csv": CsvParser(),
        ".xml": XmlParser(),
    }

    def __init__(self, data_directory):
        self.data_list = []  # List to store merged data
        self.data_directory = data_directory

    def merge_data(self) -> List[Dict]:
        file_names_list = self._get_data_filenames()
        for filename in file_names_list:
            self.data_list.extend(self._dispatch_file(filename))

        return self.data_list

    def _get_data_filenames(self) -> List[str]:
        data_files = []
        for path, _, files in os.walk(self.data_directory):
            for name in files:
                file_path = os.path.join(path, name)
                data_files.append(file_path)

        if not data_files:
            raise FileNotFoundError(
                f"There is no data to populate the database. "
                f'Provide a "{self.data_directory}" directory with your data files. '
                f'Only {", ".join(self.SUPPORTED_EXTENSIONS)} formats are supported.'
            )

        return data_files

    def _dispatch_file(self, file_path: str) -> List[Dict]:
        _, extension = os.path.splitext(file_path)

        if extension not in self.SUPPORTED_EXTENSIONS:
            raise UnsupportedFileExtensionError(
                f'File "{file_path}" with "{extension}" extension not supported. '
                f'Only {", ".join(self.SUPPORTED_EXTENSIONS)} formats are supported.'
            )

        parser = self._get_parser(extension)
        return parser.parse(file_path)

    def _get_parser(self, extension: str) -> DataParser:
        return self.SUPPORTED_PARSERS.get(extension, DataParser())


def validate_data_to_populate_db(data_directory):
    merged_data = DataMerger(data_directory).merge_data()
    clean_data = UserDataProcessor(merged_data).clean_data()
    return clean_data
