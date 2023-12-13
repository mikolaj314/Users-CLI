import copy
import datetime
import os
import unittest
from unittest.mock import patch


from click.testing import CliRunner


from cli.tasks.commands import cli
from cli.tasks.database import DatabaseManager
from cli.tasks.models import Base
from config import TestConfig
from tests.test_data import clean_data


class TestCommands(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()
        self.db_manager = DatabaseManager(TestConfig.DATABASE_URL)
        self.db_manager_patch = patch("cli.tasks.commands.db_manager", self.db_manager)
        self.db_manager_patch.start()

        self.data = clean_data

        self.test_data = copy.deepcopy(self.data)
        self.db_manager.populate_database_with(self.data)

    def tearDown(self):
        Base.metadata.drop_all(bind=self.db_manager.engine)
        db_file_path = TestConfig.DATABASE_URL.replace("sqlite:///", "")
        os.remove(db_file_path)
        self.db_manager_patch.stop()

    def test_are_admin_credentials_valid(self):
        expected = len(self.test_data)
        for user in self.test_data:
            email = user.get("email")
            tel = user.get("telephone_number")
            password = user.get("password")
            invalid_input = ""
            role = user.get("role")
            result_valid_email_valid_password = self.runner.invoke(
                cli, ["print-all-accounts", "--login", email, "--password", password]
            )
            result_valid_tel_valid_password = self.runner.invoke(
                cli, ["print-all-accounts", "--login", tel, "--password", password]
            )
            result_valid_email_invalid_password = self.runner.invoke(
                cli,
                ["print-all-accounts", "--login", email, "--password", invalid_input],
            )
            result_valid_tel_invalid_password = self.runner.invoke(
                cli, ["print-all-accounts", "--login", tel, "--password", invalid_input]
            )
            result_invalid_email_valid_password = self.runner.invoke(
                cli,
                [
                    "print-all-accounts",
                    "--login",
                    invalid_input,
                    "--password",
                    password,
                ],
            )
            result_invalid_tel_valid_password = self.runner.invoke(
                cli,
                [
                    "print-all-accounts",
                    "--login",
                    invalid_input,
                    "--password",
                    password,
                ],
            )
            result_invalid_tel_invalid_password = self.runner.invoke(
                cli,
                [
                    "print-all-accounts",
                    "--login",
                    invalid_input,
                    "--password",
                    invalid_input,
                ],
            )

            if role == "admin":
                self.assertEqual(result_valid_email_valid_password.exit_code, 0)
                self.assertEqual(
                    int(result_valid_email_valid_password.output), expected
                )

                self.assertEqual(result_valid_tel_valid_password.exit_code, 0)
                self.assertEqual(int(result_valid_tel_valid_password.output), expected)

                self.assertEqual(result_valid_email_invalid_password.exit_code, 1)
                self.assertEqual(
                    result_valid_email_invalid_password.output,
                    "Login failed. Please provide valid credentials.\nAborted!\n",
                )

                self.assertEqual(result_valid_tel_invalid_password.exit_code, 1)
                self.assertEqual(
                    result_valid_tel_invalid_password.output,
                    "Login failed. Please provide valid credentials.\nAborted!\n",
                )

                self.assertEqual(result_invalid_email_valid_password.exit_code, 1)
                self.assertEqual(
                    result_invalid_email_valid_password.output,
                    "Login failed. Please provide valid credentials.\nAborted!\n",
                )

                self.assertEqual(result_invalid_tel_valid_password.exit_code, 1)
                self.assertEqual(
                    result_invalid_tel_valid_password.output,
                    "Login failed. Please provide valid credentials.\nAborted!\n",
                )

                self.assertEqual(result_invalid_tel_invalid_password.exit_code, 1)
                self.assertEqual(
                    result_invalid_tel_invalid_password.output,
                    "Login failed. Please provide valid credentials.\nAborted!\n",
                )

            else:
                self.assertEqual(result_valid_email_valid_password.exit_code, 1)
                self.assertEqual(
                    result_valid_email_valid_password.output,
                    "Login failed. Please provide valid credentials.\nAborted!\n",
                )

                self.assertEqual(result_valid_tel_valid_password.exit_code, 1)
                self.assertEqual(
                    result_valid_tel_valid_password.output,
                    "Login failed. Please provide valid credentials.\nAborted!\n",
                )

                self.assertEqual(result_valid_email_invalid_password.exit_code, 1)
                self.assertEqual(
                    result_valid_email_invalid_password.output,
                    "Login failed. Please provide valid credentials.\nAborted!\n",
                )

                self.assertEqual(result_valid_tel_invalid_password.exit_code, 1)
                self.assertEqual(
                    result_valid_tel_invalid_password.output,
                    "Login failed. Please provide valid credentials.\nAborted!\n",
                )

                self.assertEqual(result_invalid_email_valid_password.exit_code, 1)
                self.assertEqual(
                    result_invalid_email_valid_password.output,
                    "Login failed. Please provide valid credentials.\nAborted!\n",
                )

                self.assertEqual(result_invalid_tel_valid_password.exit_code, 1)
                self.assertEqual(
                    result_invalid_tel_valid_password.output,
                    "Login failed. Please provide valid credentials.\nAborted!\n",
                )

                self.assertEqual(result_invalid_tel_invalid_password.exit_code, 1)
                self.assertEqual(
                    result_invalid_tel_invalid_password.output,
                    "Login failed. Please provide valid credentials.\nAborted!\n",
                )

    def test_are_regular_user_credentials_valid(self):
        for user in self.test_data:
            email = user.get("email")
            tel = user.get("telephone_number")
            password = user.get("password")
            invalid_input = ""
            result_valid_email_valid_password = self.runner.invoke(
                cli, ["print-children", "--login", email, "--password", password]
            )
            result_valid_tel_valid_password = self.runner.invoke(
                cli, ["print-children", "--login", tel, "--password", password]
            )
            result_valid_email_invalid_password = self.runner.invoke(
                cli, ["print-children", "--login", email, "--password", invalid_input]
            )
            result_valid_tel_invalid_password = self.runner.invoke(
                cli, ["print-children", "--login", tel, "--password", invalid_input]
            )
            result_invalid_email_valid_password = self.runner.invoke(
                cli,
                ["print-children", "--login", invalid_input, "--password", password],
            )
            result_invalid_tel_valid_password = self.runner.invoke(
                cli,
                ["print-children", "--login", invalid_input, "--password", password],
            )
            result_invalid_tel_invalid_password = self.runner.invoke(
                cli,
                [
                    "print-children",
                    "--login",
                    invalid_input,
                    "--password",
                    invalid_input,
                ],
            )

            expected = ""
            if children := user.get("children"):
                for child in sorted(
                    children, key=lambda item: (item["name"], item["age"])
                ):
                    child: dict
                    expected += f"{child.get('name')}, {child.get('age')}\n"
                self.assertEqual(result_valid_email_valid_password.exit_code, 0)
                self.assertEqual(result_valid_email_valid_password.output, expected)

                self.assertEqual(result_valid_tel_valid_password.exit_code, 0)
                self.assertEqual(result_valid_tel_valid_password.output, expected)

                self.assertEqual(result_valid_email_invalid_password.exit_code, 1)
                self.assertEqual(
                    result_valid_email_invalid_password.output,
                    "Login failed. Please provide valid credentials.\nAborted!\n",
                )

                self.assertEqual(result_valid_tel_invalid_password.exit_code, 1)
                self.assertEqual(
                    result_valid_tel_invalid_password.output,
                    "Login failed. Please provide valid credentials.\nAborted!\n",
                )

                self.assertEqual(result_invalid_email_valid_password.exit_code, 1)
                self.assertEqual(
                    result_invalid_email_valid_password.output,
                    "Login failed. Please provide valid credentials.\nAborted!\n",
                )

                self.assertEqual(result_invalid_tel_valid_password.exit_code, 1)
                self.assertEqual(
                    result_invalid_tel_valid_password.output,
                    "Login failed. Please provide valid credentials.\nAborted!\n",
                )

                self.assertEqual(result_invalid_tel_invalid_password.exit_code, 1)
                self.assertEqual(
                    result_invalid_tel_invalid_password.output,
                    "Login failed. Please provide valid credentials.\nAborted!\n",
                )

            else:
                expected = "No children\n"
                self.assertEqual(result_valid_email_valid_password.exit_code, 0)
                self.assertEqual(result_valid_email_valid_password.output, expected)

                self.assertEqual(result_valid_tel_valid_password.exit_code, 0)
                self.assertEqual(result_valid_tel_valid_password.output, expected)

                self.assertEqual(result_valid_email_invalid_password.exit_code, 1)
                self.assertEqual(
                    result_valid_email_invalid_password.output,
                    "Login failed. Please provide valid credentials.\nAborted!\n",
                )

                self.assertEqual(result_valid_tel_invalid_password.exit_code, 1)
                self.assertEqual(
                    result_valid_tel_invalid_password.output,
                    "Login failed. Please provide valid credentials.\nAborted!\n",
                )

                self.assertEqual(result_invalid_email_valid_password.exit_code, 1)
                self.assertEqual(
                    result_invalid_email_valid_password.output,
                    "Login failed. Please provide valid credentials.\nAborted!\n",
                )

                self.assertEqual(result_invalid_tel_valid_password.exit_code, 1)
                self.assertEqual(
                    result_invalid_tel_valid_password.output,
                    "Login failed. Please provide valid credentials.\nAborted!\n",
                )

                self.assertEqual(result_invalid_tel_invalid_password.exit_code, 1)
                self.assertEqual(
                    result_invalid_tel_invalid_password.output,
                    "Login failed. Please provide valid credentials.\nAborted!\n",
                )

    def test_print_all_accounts(self):
        for user in self.test_data:
            expected = len(self.test_data)
            result = self.runner.invoke(
                cli,
                [
                    "print-all-accounts",
                    "--login",
                    user["telephone_number"],
                    "--password",
                    user["password"],
                ],
            )
            if user.get("role") == "admin":
                self.assertEqual(result.exit_code, 0)
                self.assertEqual(int(result.output), expected)
            else:
                expected = "Login failed. Please provide valid credentials.\nAborted!\n"
                self.assertEqual(result.exit_code, 1)
                self.assertEqual(result.output, expected)

    def test_print_oldest_account(self):
        oldest_date = datetime.datetime.max
        oldest_user = {"created_at": oldest_date}
        for user in self.test_data:
            if user.get("created_at") < oldest_user.get("created_at"):
                oldest_user = user

        for user in self.test_data:
            result = self.runner.invoke(
                cli,
                [
                    "print-oldest-account",
                    "--login",
                    user["telephone_number"],
                    "--password",
                    user["password"],
                ],
            )
            if user.get("role") == "admin":
                expected = (
                    f"name: {oldest_user.get('firstname')}\n"
                    f"email_address: {oldest_user.get('email')}\n"
                    f"created_at: {oldest_user.get('created_at')}\n"
                )
                self.assertEqual(result.exit_code, 0)
                self.assertEqual(result.output, expected)
            else:
                expected = "Login failed. Please provide valid credentials.\nAborted!\n"
                self.assertEqual(result.exit_code, 1)
                self.assertEqual(result.output, expected)

    def test_group_by_age(self):
        age_count = {}

        for user in self.test_data:
            if children := user.get("children", []):
                for child in children:
                    age = child.get("age")
                    age_count[age] = age_count.get(age, 0) + 1

        # Sort the result first by count (ascending) and then by age (ascending)
        sorted_age_count = dict(
            sorted(age_count.items(), key=lambda item: (item[1], item[0]))
        )

        expected_result = ""
        for age, count in sorted_age_count.items():
            expected_result += f"age: {age}, count: {count}\n"

        for user in self.test_data:
            result = self.runner.invoke(
                cli,
                [
                    "group-by-age",
                    "--login",
                    user["telephone_number"],
                    "--password",
                    user["password"],
                ],
            )
            if user.get("role") == "admin":
                self.assertEqual(result.output, expected_result)
                self.assertEqual(result.exit_code, 0)
            else:
                expected = "Login failed. Please provide valid credentials.\nAborted!\n"
                self.assertEqual(result.exit_code, 1)
                self.assertEqual(result.output, expected)

    def test_print_children(self):
        for user in self.test_data:
            result = self.runner.invoke(
                cli,
                [
                    "print-children",
                    "--login",
                    user["telephone_number"],
                    "--password",
                    user["password"],
                ],
            )
            expected = ""
            if children := user.get("children"):
                for child in sorted(
                    children, key=lambda item: (item["name"], item["age"])
                ):
                    child: dict
                    expected += f"{child.get('name')}, {child.get('age')}\n"
                self.assertEqual(result.exit_code, 0)
                self.assertEqual(result.output, expected)
            else:
                expected = "No children\n"
                self.assertEqual(result.exit_code, 0)
                self.assertEqual(result.output, expected)

    def test_find_similar_children_by_age(self):
        for user in self.test_data:
            result = self.runner.invoke(
                cli,
                [
                    "find-similar-children-by-age",
                    "--login",
                    user["telephone_number"],
                    "--password",
                    user["password"],
                ],
            )

            if user_children_ages := {
                child.get("age") for child in user.get("children", [])
            }:

                matching_users = []
                for other_user in self.test_data:
                    if other_user != user and other_user.get("children", []) != []:
                        for other_child in other_user.get("children"):
                            if other_child.get("age") in user_children_ages:
                                matching_users.append(other_user)
                                break

                if matching_users:
                    for matched_user in matching_users:
                        user_info = f"{matched_user.get('firstname')}, {matched_user.get('telephone_number')}:"
                        children_info = "; ".join(
                            [
                                f"{child.get('name')}, {child.get('age')}"
                                for child in matched_user.get("children")
                            ]
                        )
                        expected = f"{user_info} {children_info}\n"
                        self.assertEqual(result.exit_code, 0)
                        self.assertEqual(result.output, expected)

            else:
                expected = "No children\n"
                self.assertEqual(result.exit_code, 0)
                self.assertEqual(result.output, expected)


if __name__ == "__main__":
    unittest.main()
