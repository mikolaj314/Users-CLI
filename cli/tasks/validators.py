from datetime import datetime
import re
from typing import List, Dict, Tuple


class UserDataProcessor:
    FILTERS = ["telephone_number", "email"]

    def __init__(self, user_data: List[Dict]):
        """
        Initializes UserDataProcessor instance.

        Args:
            user_data (List[Dict]): List of user data dictionaries.
        """
        self.user_data = user_data

    @staticmethod
    def is_valid_email(email: str) -> bool:
        """
        Validates an email address.

        Args:
            email (str): Email address.

        Returns:
            bool: True if the email is valid, otherwise False.
        """
        email_regex = r"^[^@]+@[^@]+\.[a-zA-Z\d]{1,4}$"
        return bool(re.match(email_regex, email))

    @staticmethod
    def is_valid_telephone_number(tel_number: str) -> bool:
        """
        Validates a telephone number.

        Args:
            tel_number (str): Telephone number.

        Returns:
            bool: True if the telephone number is valid, otherwise False.
        """
        return len(tel_number) == 9

    @staticmethod
    def clean_telephone_number(tel_number: str) -> str:
        """
        Cleans and extracts a valid telephone number.

        Args:
            tel_number (str): Telephone number.

        Returns:
            str: Cleaned telephone number.
        """
        cleaned_number = tel_number.replace(" ", "").lstrip("0")
        return cleaned_number[-9:]

    @staticmethod
    def convert_str_into_datetime(date_string: str) -> datetime:
        """
        Converts a string representation of a date into a datetime object.

        Args:
            date_string (str): String representation of a date.

        Returns:
            datetime: Datetime object.
        """
        return datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

    def clean_and_validate_telephone_number(
        self, telephone_number: str
    ) -> Tuple[str, bool]:
        """
        Cleans and validates a telephone number.

        Args:
            telephone_number (str): Telephone number.

        Returns:
            Tuple[str, bool]: Cleaned telephone number and a flag indicating its validity.
        """
        cleaned_number = self.clean_telephone_number(telephone_number)
        is_valid = self.is_valid_telephone_number(cleaned_number)
        return cleaned_number, is_valid

    def remove_duplicates_recursive(
        self,
        user_data: (List[dict] or dict),
        filters: List[str],
        current_filter_idx: int = 0,
    ) -> List[Dict]:
        """
        Recursively removes duplicates from user data based on specified filters.

        Args:
            user_data (List[dict] or dict.values())
            filters (List[str]): List of filters for duplicate removal.
            current_filter_idx (int): Current index of the filter being processed.

        Returns:
            List[Dict]: List of user data dictionaries without duplicates.
        """
        if current_filter_idx == len(filters):
            return list(user_data)

        current_filter = filters[current_filter_idx]
        filtered_data = {}
        for user in user_data:
            current_value = user[current_filter]
            existing_user = filtered_data.get(current_value)

            if not existing_user or existing_user["created_at"] < user["created_at"]:
                filtered_data[current_value] = user

        return self.remove_duplicates_recursive(
            user_data=filtered_data.values(),
            filters=filters,
            current_filter_idx=current_filter_idx + 1,
        )

    def clean_data(self) -> List[Dict]:
        """
        Cleans and processes user data.

        Returns:
            List[Dict[str, Union[str, List[Dict[str, Union[str, int]]]]]]: Processed user data without duplicates.
        """

        cleaned_users = []
        for user in self.user_data:
            (
                telephone_number,
                is_valid_telephone,
            ) = self.clean_and_validate_telephone_number(user["telephone_number"])

            if not is_valid_telephone:
                continue

            user["telephone_number"] = telephone_number
            user["created_at"] = self.convert_str_into_datetime(user["created_at"])

            if children := user["children"]:
                for child in children:
                    child["age"] = int(child["age"])

            if self.is_valid_email(user["email"]):
                cleaned_users.append(user)

        return self.remove_duplicates_recursive(cleaned_users, self.FILTERS)
