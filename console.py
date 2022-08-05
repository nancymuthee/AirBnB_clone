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
import shlex


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

    def do_destroy(self, inp):
        """Deletes an instance based on the class name and id (save the
        change into the JSON file).
        """
        args = inp.split()
        if not self.class_verification(args):
            return
        if not self.id_verification(args):
            return
        string_key = str(args[0]) + '.' + str(args[1])
        objects = storage.all()
        storage.delete(objects[string_key])
        storage.save()

    def do_all(self, inp):
        """Prints all string representation of all instances based or not
        on the class name.
        """
        args = inp.split()
        all_objects = storage.all()
        classes = ['BaseModel']
        list_ = []
        if len(args) == 0:
            # print all classes
            for value in all_objects.values():
                list_.append(str(value))
        elif args[0] in classes:
            # print just arg[0] class instances
            for (key, value) in all_objects.items():
                if args[0] in key:
                    list_.append(str(value))
        else:
            print("** class doesn't exist **")
            return False
        print(list_)

    def do_update(self, line):
        """ Updates an instance based on the class name and id by adding or
        updating attribute (save the change into the JSON file).
        """
        args = shlex.split(line)
        if not self.class_verification(args):
            return
        if not self.id_verification(args):
            return
        if not self.attribute_verification(args):
            return
        string_key = str(args[0]) + '.' + str(args[1])
        all_objects = storage.all()
        my_dict = all_objects[string_key].to_dict()
        attr_name = args[2]
        attr_value = args[3]
        for (key, value) in my_dict.items():
            if attr_name is key:
                attr_value = eval('({}){}'.format(type(value), attr_value))
        setattr(all_objects[string_key], attr_name, attr_value)
        storage.save()

    @staticmethod
    def attribute_verification(args):
        """Verifies attributes.
        """
        if len(args) < 3:
            print("** attribute name missing **")
            return False
        if len(args) < 4:
            print("** value missing **")
            return False
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
