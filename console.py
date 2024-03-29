#!/usr/bin/python3

import cmd
from models import storage
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

valid_classes = ['User', 'Place', 'State', 'City', 'Amenity', 'Review']


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit on EOF (Ctrl+D)"""
        return True

    def do_help(self, arg):
        """
        List available commands with 'help' or
        detailed help with 'help cmd'.

        """
        cmd.Cmd.do_help(self, arg)

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_create(self, arg):
        """Create command to create a new instance of a class."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in valid_classes:
            print("** class doesn't exist **")
            return
        new_obj = eval(args[0])()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, arg):
        """Show command to display the string representation of an object."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        objects = storage.all()
        obj = objects.get(key)
        if obj is None:
            print("** no instance found **")
        else:
            print(obj)

    def do_destroy(self, arg):
        """Destroy command to delete an instance."""
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in valid_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        objects = storage.all()
        if key in objects:
            del objects[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """All command to display all instances of a class or all classes."""
        objects = storage.all()
        if not arg:
            obj_list = list(objects.values())
            print([str(obj) for obj in obj_list])
        else:
            args = arg.split()
            if args[0] in valid_classes:
                obj_list = eval(args[0]).all()
                print([str(obj) for obj in obj_list])
            else:
                print("** class doesn't exist **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
