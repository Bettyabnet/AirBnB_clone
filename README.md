# 0x00. AirBnB clone - The consuole

Project done by  Betelhem Assefa

## Description of the project

The project aims to build an AirBnB clone, starting with the development of a command interpreter to manage AirBnB objects. The command interpreter will allow users to create new objects, retrieve objects from files or databases, perform operations on objects (such as counting and computing statistics), update object attributes, and destroy objects.

The project will involve the following key concepts:

 - Python packages: You will learn how to create a Python package to organize and structure your code effectively.

 - AirBnB clone: The project is centered around building an AirBnB clone, which will serve as the foundation for future projects related to HTML/CSS templating, database storage, API development, and front-end integration.

 - Command interpreter: The command interpreter is a shell-like interface that enables users to interact with the AirBnB objects. Users can execute commands to perform various operations on the objects, such as creating, retrieving, updating, and deleting.

 - Serialization and deserialization: You will learn how to serialize (convert to a specific format) and deserialize (convert back to its original form) objects. This process allows objects to be stored in files or transferred over a network.

 - File storage: The project will involve developing an abstracted storage engine for handling the storage and retrieval of objects.

## Description of the command interpreter

The command interpreter in this project is a shell-like interface that allows you to manage AirBnB objects. Here's a description of how to start and use the command interpreter, along with some examples:

* Starting the Command Interpreter:
To start the command interpreter, you need to execute the console.py script. You can do this by running the following command in your terminal:

```python 3
$ ./console.py
```
After starting the interpreter, you will see a prompt `(hbnb)` indicating that you can start entering commands.

* Using the Command Interpreter:
The command interpreter provides several commands that you can use to manage AirBnB objects. Here are some of the available commands:

help: Displays a list of available commands or provides help for a specific command. You can use help followed by a command name to get more information about that command.

```python 3
(hbnb) help
(hbnb) help create
```

- `create`: Creates a new instance of a specified class. You need to provide the class name as an argument.

* Examples
Here are some examples of using the command interpreter:

Creating a new User instance:
   (hbnb) create User
```

- Displaying a User instance:
(hbnb) show User 1234-5678
- Displaying all instances of User class:
(hbnb) all User
- Updating the name attribute of a User instance:
(hbnb) update User 1234-5678 name "John Doe"
- Deleting a User instance:
(hbnb) destroy User 1234-5678

# There is more commands available on `help` command within the interpreter.


## Objectives

  - To create a Python package
  - To create a command interpreter in Python using the cmd module
  - To understand Unit testing and to impliment it on a large project
  - To serialize and deserialize a Class
  - To write and read a JSON file
  - To manage "datetime"
  - To know "UUID"
  - To know how to use 'args'
  - To handle named arguments in a function

## Resources
  
Read or watch:

  - cmd module
  - cmd module in depth
  - packages concept page
  - uuid module
  - datetime
  - unittest module
  - args/kwargs
  - Python test cheatsheet
  - cmd module wiki page
  - python unittest

## Concepts 

* Python packages
* AirBnB clone

## Python Script Requiments
  
   - allowed editors: `vi`, `vim`, `emacs`   
   - the first line of all files should be exactly `#!/usr/bin/python3`   
   - all code should use the `PEP8` style (version 1.7.)   
   - all files must be executable   
   - all files will be interpreted/compiled on Ubuntu 14.04 LTS using `python3` (version 3.4.3) 

## Usage Examples for console

## Interactive Mode

```python3
~/me$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb)
(hbnb)
(hbnb) quit
~/me$
```

## Non-Interactive Mode

```python3
~/me$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)

~/me$ cat test_help
help
~/me$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb)
~/me$
```

## Bugs

At this time, there are no known bugs.

## License

**AirBnB Clone** is open source and free to download and use
