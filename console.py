#!/usr/bin/python3
"""
    contains the entry point of the command interpreter:
"""
import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
import json
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
        command interprete
    """

    prompt = '(hbnb) '
    my_classes = ["BaseModel", "User", "Place", "State", "Amenity", "Review",
                                                                    "City"]

    def do_help(self, args):
        """
            defines help options
        """
        cmd.Cmd.do_help(self, args)

    def do_quit(self, args):
        """
            Quit command to exit the program
        """
        return True

    def do_EOF(self, args):
        """
            EOF command exits out of the command interpreter
        """
        print()
        return True

    def emptyline(self):
        """
            avoid any execution when enter is hit in empty line
        """
        pass

    def do_create(self, line_args):
        """
             Creates a new instance of BaseModel,
             saves it (to the JSON file) and prints the id.
             Ex: $ create BaseModel
        """
        if len(line_args) < 1:
            print("** class name missing **")
        elif line_args not in self.my_classes:
            print('** class doesn\'t exist **')
            return False
        else:
            new = eval("{}()".format(line_args))
            new.save()
            print(new.id)

    def do_show(self, line_args):
        """
            Prints the stringrepresentation of an instance
            based on the class name and id
        """
        args = line_args.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        elif args[0] not in self.my_classes:
            print("** class doesn\'t exist **")
            return False

        if len(args) < 2:
            print("** instance id missing **")
            return False

        my_objects = storage.all()
        for i in my_objects.keys():
            if i == "{}.{}". format(args[0], args[1]):
                print(my_objects[i])
                return False
        print("** no instance found **")

    def do_destroy(self, line_args):
        """
             Deletes an instance based on the class name and id
        """
        args = line_args.split()
        if len(line_args) == 0:
            print("** class name missing **")
            return False
        elif args[0] not in self.my_classes:
            print('** class doesn\'t exist **')
            return False
        elif len(args) < 2:
            print("** instance id missing **")
            return False
        else:
            my_objects = storage.all()
            for i in my_objects:
                if i == "{}.{}".format(args[0], args[1]):
                    my_objects.pop(i)
                    storage.save()
                    return False
            print("** no instance found **")

    def do_all(self, line_args):
        """
            Prints all string representation
            of all instances based or not on the class name
        """
        args = line_args.split()
        my_objects = storage.all()

        if len(args) == 0:
            for i in my_objects:
                args_as_str = str(my_objects[i])
                print(args_as_str)
        elif line_args not in self.my_classes:
            print("** class doesn\'t exist **")
            return False
        else:
            for i in my_objects:
                if i.startswith(args[0]):
                    args_as_str = str(my_objects[i])
                    print(args_as_str)
        return False

    def do_update(self, line_args):
        """
            Updates an instance based on the class name and id
            by adding or updating attribute (save the change
            into the JSON file).
        """
        args = line_args.split()
        counter = 0
        if len(args) < 1:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.my_classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        elif len(args) < 3:
            print("** attribute name missing **")
        elif len(args) < 4:
            print("** value missing **")
        else:
            element = (args[0] + "." + args[1])
            for key, obj in storage.all().items():
                if key == element:
                    idx_arg = len(args[0]) + len(args[1]) + len(args[2]) + 3
                    value = args[idx_arg:]
                    if args[idx_arg] == "\"":
                        idx_arg += 1
                        value = args[idx_arg:-1]
                    if hasattr(obj, arg[2]):
                        value = type(getattr(obj, args[2]))(args[idx_arg:])
                    setattr(obj, args[2], value)
                    counter = 1
                    storage.save()
            if counter == 0:
                print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
