#!/usr/bin/python3
"""Command interpreter module."""

import cmd
import shlex

from models import storage
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB project."""

    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_create(self, arg):
        """Create a new instance of BaseModel."""
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)

        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return

        new_instance = BaseModel()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Show an instance based on class name and id."""
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)

        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "BaseModel." + args[1]
        instance = storage.all().get(key)

        if instance is None:
            print("** no instance found **")
            return

        print(instance)

    def do_destroy(self, arg):
        """Delete an instance based on class name and id."""
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)

        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "BaseModel." + args[1]
        instance = storage.all().get(key)

        if instance is None:
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Print all instances or all instances of BaseModel."""
        args = shlex.split(arg)

        if args and args[0] != "BaseModel":
            print("** class doesn't exist **")
            return

        instances = []

        for instance in storage.all().values():
            instances.append(str(instance))

        print(instances)

    def do_update(self, arg):
        """Update an instance based on class name and id."""
        if not arg:
            print("** class name missing **")
            return

        args = shlex.split(arg)

        if args[0] != "BaseModel":
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "BaseModel." + args[1]
        instance = storage.all().get(key)

        if instance is None:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attribute_name = args[2]
        attribute_value = args[3]

        if hasattr(instance, attribute_name):
            current_value = getattr(instance, attribute_name)

            if isinstance(current_value, int):
                attribute_value = int(attribute_value)
            elif isinstance(current_value, float):
                attribute_value = float(attribute_value)

        setattr(instance, attribute_name, attribute_value)
        instance.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
