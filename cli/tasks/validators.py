from datetime import datetime
import re
from typing import List, Dict, Tuple


class UserDataProcessor:
    FILTERS = ["telephone_number", "email"]

    def __init__(self, user_data: List[Dict]):
        self.user_data = user_data

    @staticmethod
    def is_valid_email(email):
        email_regex = r"^[^@]+@[^@]+\.[a-zA-Z\d]{1,4}$"
        return bool(re.match(email_regex, email))

    @staticmethod
    def is_valid_telephone_number(tel_number: str) -> bool:
        return len(tel_number) == 9 and tel_number.isdigit()

    @staticmethod
    def clean_telephone_number(tel_number: str) -> str:
        return tel_number.replace(" ", "")[-9:].lstrip("0")

    @staticmethod
    def convert_str_into_datetime(date_string: str) -> datetime:
        return datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

    def clean_and_validate_telephone_number(
        self, telephone_number: str
    ) -> Tuple[str, bool]:
        cleaned_number = self.clean_telephone_number(telephone_number)
        is_valid = self.is_valid_telephone_number(cleaned_number)
        return cleaned_number, is_valid

    def remove_duplicates_recursive(
        self,
        user_data: (List[dict] or dict),
        filters: List[str],
        current_filter_idx: int = 0,
    ) -> List[Dict]:
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
