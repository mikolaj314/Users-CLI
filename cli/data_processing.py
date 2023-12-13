import csv
import json
import os


from typing import Any, Dict, List
import xml.etree.ElementTree as ETree


from cli.tasks.validators import UserDataProcessor


class DataParser:
    """Base class for data parsers."""

    def parse(self, file_path: str) -> List[Dict]:
        """
        Parses the data from a file.

        Args:
            file_path (str): The path to the data file.

        Returns:
            List[Dict]: A list of dictionaries representing the parsed data.
        """
        raise NotImplementedError(
            f'Subclasses must implement the parse method for a file "{file_path}".'
        )


class JsonParser(DataParser):
    """Parses JSON files."""

    def parse(self, file_path: str) -> List[Dict]:
        """
        Parses JSON data from a file.

        Args:
            file_path (str): The path to the JSON file.

        Returns:
            List[Dict]: A list of dictionaries representing the parsed JSON format data.
        """
        try:
            with open(file_path) as json_file:
                return json.load(json_file)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
            raise


class CsvParser(DataParser):
    """Parses CSV files."""

    def _parse_children(self, children_data: str) -> List[Dict[str, Any]]:
        """
        Parses the children data from a CSV row.

        Args:
            children_data (str): The children data string from a CSV row.

        Returns:
            List[Dict[str, Any]]: A list of dictionaries representing the parsed children data.
        """
        children_list = []

        if children_data:
            for child in children_data.split(","):
                name, age = child.split()
                # strip round brackets "(12)" -> "12"
                age = age[1:-1]
                children_list.append({"name": name, "age": age})

        return children_list

    def parse(self, file_path: str) -> List[Dict]:
        """
        Parses CSV data from a file.

        Args:
            file_path (str): The path to the CSV file.

        Returns:
            List[Dict]: A list of dictionaries representing the parsed CSV format data.
        """
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
    """Parses XML files."""

    def _parse_element_to_dict(self, element: ETree.Element) -> Dict:
        """
        Recursively parses an XML element into a dictionary.

        Args:
            element (ETree.Element): The XML element to parse.

        Returns:
            Dict: A dictionary representing the parsed XML format element.
        """
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
        """
        Parses XML data from a file.

        Args:
            file_path (str): The path to the XML file.

        Returns:
            List[Dict]: A list of dictionaries representing the parsed XML format data.
        """
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
    """Merges data from various file formats in a directory.

    Attributes:
        SUPPORTED_EXTENSIONS (set): Set of supported file extensions.
        SUPPORTED_PARSERS (dict): Dictionary mapping file extensions to parser instances.
        data_directory (str): The directory containing data files.
    """
    SUPPORTED_EXTENSIONS = {".json", ".csv", ".xml"}
    SUPPORTED_PARSERS = {
        ".json": JsonParser(),
        ".csv": CsvParser(),
        ".xml": XmlParser(),
    }

    def __init__(self, data_directory):
        """
        Initialize the DataMerger instance.
        """
        self.data_list = []  # List to store merged data
        self.data_directory = data_directory

    def merge_data(self) -> List[Dict]:
        """
        Merges data from all supported file formats in the directory.

        Returns:
            List[Dict]: A list of dictionaries representing the merged data.
        """
        file_names_list = self._get_data_filenames()
        for filename in file_names_list:
            self.data_list.extend(self._dispatch_file(filename))

        return self.data_list

    def _get_data_filenames(self) -> List[str]:
        """
        Gets a list of all data file names in the directory.

        Returns:
            List[str]: A list of file paths for data files.
        """
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
        """
        Dispatches the file to the appropriate parser.
        Raises UnsupportedFileExtensionError if extension is not supported.

        Args:
            file_path (str): The path to the file to be dispatched.

        Returns:
            List[Dict]: A list of dictionaries representing the parsed data from the file.
        """
        _, extension = os.path.splitext(file_path)

        if extension not in self.SUPPORTED_EXTENSIONS:
            raise UnsupportedFileExtensionError(
                f'File "{file_path}" with "{extension}" extension not supported. '
                f'Only {", ".join(self.SUPPORTED_EXTENSIONS)} formats are supported.'
            )

        parser = self._get_parser(extension)
        return parser.parse(file_path)

    def _get_parser(self, extension: str) -> DataParser:
        """
        Gets the appropriate parser for a given file extension.

        Args:
            extension (str): The file extension.

        Returns:
            DataParser: An instance of the appropriate parser.
        """
        return self.SUPPORTED_PARSERS.get(extension, DataParser())


def validate_data_to_populate_db(data_directory):
    """
    Validates and processes data from various file formats from data_directory.

    Args:
        data_directory (str): The directory containing data files.

    Returns:
        List[Dict]: A list of dictionaries representing the cleaned and processed data.
    """
    merged_data = DataMerger(data_directory).merge_data()
    clean_data = UserDataProcessor(merged_data).clean_data()
    return clean_data
