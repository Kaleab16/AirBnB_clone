#!/usr/bin/python3
"""Command interpreter module."""

import cmd
import shlex

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB project."""

    prompt = '(hbnb) '

    classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_quit(self, arg):
        """Quit command."""
        return True

    def do_EOF(self, arg):
        """EOF command."""
        print()
        return True

    def emptyline(self):
        """Do nothing when an empty line is entered."""
        pass

    def do_create(self, arg):
        """Create a new instance."""
        if not arg:
            print("** class name missing **")
            return

        try:
            args = shlex.split(arg)
        except ValueError:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        new_instance = self.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Show an instance."""
        if not arg:
            print("** class name missing **")
            return

        try:
            args = shlex.split(arg)
        except ValueError:
            args = arg.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(class_name, args[1])
        instance = storage.all().get(key)

        if instance is None:
            print("** no instance found **")
            return

        print(instance)

    def do_destroy(self, arg):
        """Destroy an instance."""
        if not arg:
            print("** class name missing **")
            return

        try:
            args = shlex.split(arg)
        except ValueError:
            args = arg.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(class_name, args[1])

        if storage.all().get(key) is None:
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Show all instances or instances of a class."""
        try:
            args = shlex.split(arg)
        except ValueError:
            args = arg.split()

        if args and args[0] not in self.classes:
            print("** class doesn't exist **")
            return

        instances = []

        for instance in storage.all().values():
            if not args or instance.__class__.__name__ == args[0]:
                instances.append(str(instance))

        print(instances)

    def do_update(self, arg):
        """Update an instance."""
        if not arg:
            print("** class name missing **")
            return

        try:
            args = shlex.split(arg)
        except ValueError:
            args = arg.split()

        if not args:
            print("** class name missing **")
            return

        class_name = args[0]

        if class_name not in self.classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(class_name, args[1])
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
