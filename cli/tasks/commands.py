import functools
import os


import click


from cli.data_processing import validate_data_to_populate_db
from cli.tasks.database import DatabaseManager
from config import Config, TestConfig


# Choose the configuration based on the environment
config = TestConfig() if "TESTING" in os.environ else Config()
db_manager = DatabaseManager(config.DATABASE_URL)


def are_credentials_valid(login: str, password: str, admin_required: bool):
    user = db_manager.get_user_by_login(login, admin=admin_required)

    if (
        user
        and user.password == password
        and (not admin_required or user.role == "admin")
    ):
        return user

    click.echo("Login failed. Please provide valid credentials.")
    raise click.Abort()


def login_required(admin_required: bool = False):
    def decorator(func):
        @click.option("--login", required=True, help="User login")
        @click.option("--password", required=True, help="User password")
        @functools.wraps(func)
        def wrapper(**kwargs):
            kwargs["user"] = are_credentials_valid(
                kwargs["login"], kwargs["password"], admin_required
            )
            return func(**kwargs)

        return wrapper

    return decorator


@click.group()
def cli():
    """CLI tool for managing user accounts."""


@cli.command(name="print-all-accounts")
@login_required(admin_required=True)
def print_all_accounts(**kwargs):
    number_of_accounts = db_manager.count_all_accounts()
    click.echo(number_of_accounts)
    return number_of_accounts


@cli.command(name="print-oldest-account")
@login_required(admin_required=True)
def print_oldest_account(**kwargs):
    oldest_account = db_manager.get_oldest_account()
    click.echo(
        f"name: {oldest_account.firstname}\n"
        f"email_address: {oldest_account.email}\n"
        f"created_at: {oldest_account.created_at}"
    )


@cli.command(name="group-by-age")
@login_required(admin_required=True)
def group_by_age(**kwargs):
    grouped_by_age = db_manager.get_age_grouped_by_children()
    for age, count in grouped_by_age:
        click.echo(f"age: {age}, count: {count}")


@cli.command(name="print-children")
@login_required()
def print_children(**kwargs):
    user_id = kwargs["user"].user_id
    user_children = db_manager.get_children(user_id)

    if user_children:
        for child in user_children:
            click.echo(f"{child.name}, {child.age}")
    else:
        click.echo("No children")


@cli.command(name="find-similar-children-by-age")
@login_required()
def find_similar_children_by_age(**kwargs):
    user_id = kwargs["user"].user_id
    result = db_manager.get_children_with_user_children_same_age(user_id)

    if result:
        for row in result:
            user = f"{row.Users.firstname}, {row.Users.telephone_number}:"
            children_info = "; ".join(
                [f"{child.name}, {child.age}" for child in row.Users.children]
            )
            click.echo(f"{user} {children_info}")
    else:
        click.echo("No children")


@cli.command(name="create_database")
def create_database():
    """
    Create the database.

    1. Validates and processes data from various file formats (.json, .csv, .xml) in a directory (default=data).
    2. Removes duplicates based on telephone number or email, saving the newer entry.
    3. Stores telephone numbers as 9 digits, removing special characters and leading zeros.
    4. Validates emails and rejects entries without a valid email address.
    5. Populates the database with the cleaned and processed data.

    Returns:
        None
    """
    cleaned_data = validate_data_to_populate_db(config.DATA_DIRECTORY)
    db_manager.populate_database_with(cleaned_data)
    click.echo("Database created successfully")


@cli.command(name="delete_database")
def delete_database():
    os.remove(config.DATABASE_URL.replace("sqlite:///", ""))
