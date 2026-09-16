#!/usr/bin/python3
"""Command interpreter module."""

import cmd


class HBNBCommand(cmd.Cmd):
    """Command interpreter for the AirBnB project."""

    prompt = '(hbnb)'

    def do_quit(self,arg):
        """Quit command to exist the program."""
        print()
        return True
    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

if __name__ == "__main__":
    HBNBCommand().cmdloop()
