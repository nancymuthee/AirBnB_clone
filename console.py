#!/usr/bin/python3
"""Contains the entry point of the command interpreter.

You must use the module cmd.
Your class definition must be: class HBNBCommand(cmd.Cmd):
Your command interpreter should implement:
quit and EOF to exit the program,
help (this action is provided by default by cmd but you should keep it
updated and documented as you work through tasks),
a custom prompt: (hbnb),
an empty line + ENTER shouldn’t execute anything.
Your code should not be executed when imported
"""
import cmd
from models.base_model import BaseModel


class HBNBCommand(cmd.Cmd):
    """class for command processor.

    Args:
        cmd (_type_): _description_
    """
    prompt = '(hbnb) '

    def do_quit(self, args):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """EOF command to exit the program
        """
        return True

    def emptyline(self):
        """Empty line shouldn't execute anything
        """
        pass

    def create(self, class_name):
        """Creates a new instance of BaseModel, saves it (to the JSON
        file) and prints the id.

        Args:
            class_name (class): name of current class.
        """
        classes = ['BaseModel']

        if not class_name:
            print("** class name missing **")
        elif class_name not in classes:
            print("** class doesn't exist **")
        else:
            new_model = BaseModel()
            print(new_model.id)
            new_model.save()

if __name__ == '__main__':
    HBNBCommand().cmdloop()
