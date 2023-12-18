# User Account Management CLI
This Command Line Interface (CLI) tool is designed for managing user accounts based on a dataset containing information about individuals, including their first name, telephone number, email, password, role, date of account creation, and a list of children with their names and ages.

## Code Structure

The CLI tool is organized into several modules to enhance code readability and maintainability:

- `cli`: Contains the main CLI commands and options.
- `cli.data_processing`: Handles data validation and processing.
- `cli.tasks.database`: Manages interactions with the database.
- `config`: Defines configuration settings.

## Configuration

The appropriate configuration is chosen based on the environment (testing or production). You can find the configuration details in the `config.py`.



## User Validation and Login

User credentials are validated using the `are_credentials_valid` function. The `login_required` decorator enforces login requirements for commands, allowing customization based on the need for admin privileges.



## CLI Commands

The CLI commands are grouped into functional categories, including admin actions and user actions. Each command provides specific functionality and returns relevant information.



## Database Interaction

The `DatabaseManager` class handle interaction with the database. It performs tasks such as counting all accounts, retrieving information about the oldest account, grouping children by age, and more.

## Data Processing

The `validate_data_to_populate_db` function in the `cli.data_processing` module processes and validates data from various file formats before populating the database.


## Installation

Clone the repository and install the required dependencies

1. Clone this repository to your local machine: [https://github.com/mikolaj314/Users-CLI.git](https://github.com/mikolaj314/Users-CLI.git)
2. Create venv:
```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

## Usage

Provide directory "data" inside main project directory containing `.xml`, `.json` and `.xml` files.
Files can be located in any subfolder locations.

Run the CLI using the following command scheme:
`All passwords must be enclosedin in a single / double quotes`


```bash
python script.py <command> --login <login> --password <password>
```



### Create database
```bash
python script.py create_database
```
- Validates and processes data from various file formats (.json, .csv, .xml) from directory (default directory = data/).
- Reject entries without provided telephone number
- Removes duplicates based on telephone number or email, saving the newer entry.
- Stores telephone numbers as 9 digits, removing special characters and leading zeros.
- Validates emails and rejects entries without a valid email address:
  - Email must contain only one "@" symbol.
  - The part before "@" must be at least 1 character long.
  - The part between "@" and "." must be at least 1 character long.
  - The part after the last "." must be between 1 and 4 characters long, containing only letters and/or digits.
- Populates the database with the cleaned and processed data.





### Admin Actions


#### PRINT THE NUMBER OF ALL VALID ACCOUNNTS

```bash
python script.py print-all-accounts --login <login> --password <password>
```
###### Print the total number of valid accounts
```commandline
> python script.py print-all-accounts --login 555123456 --password 'sASfC1234'
1233333
```


#### PRINT THE LONGEST EXISTING ACCOUNT

```bash
python script.py print-oldest-account --login <login> --password <password>
```
###### Print information about the account with the longest existence.
```commandline
> python script.py print-oldest-account --login 555123456 --password 'sASfC1234'
name: Boris
email_address: boris@gmail.com
created_at: 1990-12-12 13:20:00

```



#### GROUP CHILDREN BY AGE AND DISPLAY RELEVANT INFORMATIONG

```bash
python script.py group-by-age --login <login> --password <password>
```
###### Group children by age and display relevant information
```commandline
> python script.py group-by-age --login 555123456 --password 'sASfC1234'
age: 12, count: 5
age: 10, count: 7
```



### User Actions

#### PRINT CHILDREN

```bash
python script.py print-children --login <login> --password <password>
```
###### Display information about the user's children. Sort children alphabetically by name.

```commandline
> python script.py print-children --login 555123456 --password sASfC1234
Adam, 2
Sally, 12
```



#### FIND USERS WITH CHILDREN OF SAME AGE
```bash
python script.py find-similar-children-by-age --login <login> --password <password>
```
###### Find users with children of the same age as at least one own child, print the user and all of his children data. Sort children alphabetically by name.

```commandline
> python script.py find-similar-children-by-age --login 555123456 --password sASfC1234
Brock, 789543123: Bart, 4; Olive, 2
John, 432764512: Sally, 2
```

## Testing

The project includes a comprehensive set of unit tests to ensure the functionality and reliability of the CLI tool. The tests are implemented using the `unittest` framework and include both positive and negative scenarios.

### Test Structure

The test suite is organized into the following:

- `TestCommands`: Tests the functionality of various CLI commands.
  - `test_are_admin_credentials_valid`: Validates admin credentials for different scenarios.
  - `test_are_regular_user_credentials_valid`: Validates regular user credentials for different scenarios.
  - `test_print_all_accounts`: Tests the `print-all-accounts` command.
  - `test_print_oldest_account`: Tests the `print-oldest-account` command.
  - `test_group_by_age`: Tests the `group-by-age` command.
  - `test_print_children`: Tests the `print-children` command.
  - `test_find_similar_children_by_age`: Tests the `find-similar-children-by-age` command.

### Running Tests

To run the tests, execute the following command in the project directory:

```bash
python -m unittest tests.test_commands
```

### Test Data set
The test data set is defined in the `tests.test_data.py` and includes cleaned data used for populating the database.


Mikołaj Piekarski