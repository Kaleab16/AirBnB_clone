# AirBnB Clone - The Console

## Description

This project is the first part of the AirBnB Clone project. It is a command-line interpreter that manages AirBnB objects and provides a foundation for building a complete web application.

The project focuses on:

- Creating and managing Python classes and objects
- Implementing object-oriented programming concepts
- Creating a command interpreter
- Serializing and deserializing objects
- Persisting objects using JSON files
- Writing unit tests
- Following Python coding standards

## The Command Interpreter

The command interpreter is a command-line interface that allows users to interact with the AirBnB application.

It can be used to:

- Create new objects
- Display objects
- Update object attributes
- Destroy objects
- Display object information
- Manage stored application data

### How to Start

Clone the repository and navigate into the project directory:

    git clone https://github.com/Kaleab16/AirBnB_clone.git
    cd AirBnB_clone

Start the command interpreter with:

    ./console.py

You can also run it using:

    python3 console.py

### How to Use

Once the console is running, commands can be entered at the prompt:

    (hbnb)

For example:

    (hbnb) help
    (hbnb) create BaseModel
    (hbnb) all
    (hbnb) show BaseModel <id>
    (hbnb) update BaseModel <id> name "My First Model"
    (hbnb) destroy BaseModel <id>
    (hbnb) quit

To exit the console:

    (hbnb) quit

You can also use `Ctrl+D` to exit.

## Available Commands

| Command | Description |
|---|---|
| `quit` | Exits the command interpreter |
| `EOF` | Exits the command interpreter |
| `help` | Displays available commands and their descriptions |
| `create` | Creates a new instance of a class |
| `show` | Displays an instance based on its class and ID |
| `destroy` | Deletes an instance based on its class and ID |
| `all` | Displays all instances or all instances of a specific class |
| `update` | Updates an instance attribute |

## Project Structure

    AirBnB_clone/
    ├── AUTHORS
    ├── README.md
    ├── console.py
    ├── models/
    │   ├── __init__.py
    │   ├── base_model.py
    │   └── engine/
    │       ├── __init__.py
    │       └── file_storage.py
    └── tests/
        ├── __init__.py
        └── test_models/

## Testing

Unit tests are located in the `tests` directory.

Run all tests with:

    python3 -m unittest discover tests

Run the tests in non-interactive mode with:

    echo "python3 -m unittest discover tests" | bash

## Coding Style

The project follows Python's PEP 8 coding standards.

Code style can be checked using:

    pycodestyle .

## Authors

See the `AUTHORS` file for the list of contributors to this project.
