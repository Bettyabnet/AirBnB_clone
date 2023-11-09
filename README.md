# 0x00. AirBnB clone - The console

Project done in teams of 2 people (our team: Betelhem Assefa, Nadya Ali)


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
