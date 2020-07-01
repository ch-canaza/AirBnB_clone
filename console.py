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
            element = 0

            if len(line_args) == 0:
                print("** class name missing **")
                return False

            try:
                class_name = line_args.split()[0]
                eval("{}()".format(class_name))
            except IndexError:
                print("** class doesn\'t exist **")
                return False

            try:
                instance_id = line_args.split()[1]
            except IndexError:
                print("** instance id missing **")
                return False

            my_objects = storage.all()
            try:
                class_instance = my_objects["{}.{}".format(class_name,
                                                           instance_id)]
            except IndexError:
                print("** no instance found **")
                return False

            try:
                attribute_name = line_args.split()[2]
            except IndexError:
                print("** attribute name missing **")
                return False

            try:
                attr_value = line_args.split()[3]
            except IndexError:
                print("** value missing **")
                return False

            if attr_value.isdecimal() is True:
                setattr(class_instance, attribute_name, int(attr_value))
                storage.save()
            else:
                if line_args:
                    setattr(class_instance, attribute_name, float(attr_value))
                    storage.save()
                else:
                    setattr(class_instance, attribute_name, str(attr_value))
                    storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
