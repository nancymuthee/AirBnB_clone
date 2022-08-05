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
from models.__init__ import storage


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

    def do_create(self, class_name):
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

    def do_show(self, inp):
        """Prints the string representation of an instance based on the
        class name and id.
        """
        args = inp.split

        if not self.class_verification(args):
            return

        if not self.id_verification(args):
            return

        string_key = str(args[0]) + '.' + str(args[1])
        objects = storage.all()
        print(objects[string_key])

    @classmethod
    def class_verification(cls, args):
        """Verifies class and checks if it is in the class list.

        Returns:
            bool: True or false depending on status of class.
        """
        classes = ['BaseModel']
        if len(args) == 0:
            print("** class name missing **")
            return False

        if args[0] not in classes:
            return False

        return True

    @staticmethod
    def id_verification(args):
        """Verifies id of class.

        Returns:
            bool: True or False depending on status of id.
        """
        if len(args) < 2:
            print("** instance id missing **")
            return False

        objects = storage.all()
        string_key = str(args[0]) + '.' + str(args[1])
        if string_key not in objects.keys():
            print("** no instance found **")
            return False

        return True

if __name__ == '__main__':
    HBNBCommand().cmdloop()
