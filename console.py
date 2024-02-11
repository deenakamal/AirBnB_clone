#!/usr/bin/python3
""" Definition of Console Module """

import sys
import cmd
import models
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """ cmd class """
    prompt = "(hbnb) "

    def do_quit(self, line):
        """To Exit the program"""
        return True

    def emptyline(self):
        """Empty line."""
        pass

    def do_quit(self, line):
        """To Exit the program"""
        return True

    def do_help(self, line):
        """Help to show docstring for a command"""
        cmd.Cmd.do_help(self, line)

    def do_count(self, line):
        """Count command to retrieve the number of instances
        Args:
            line: input command
        """
        count = 0
        new_list = line.split()
        if new_list[0] in self.cls_objs:
            for key in models.storage.all().keys():
                if new_list[0] in key:
                    count += 1
        print(count)

    def do_create(self, line):
        """Create a new instance of BaseModel"""
        if not line:
            print("** class name missing **")
            return
        class_name, *args = line.split()
        if class_name not in models.storage.CLASSES_DICT:
            print("** class doesn't exist **")
            return
        new_obj = models.storage.CLASSES_DICT[class_name]()
        new_obj.save()
        print(new_obj.id)

    def do_all(self, line):
        """Prints all string representations of instances based on the class
        Args:
            line: command
        """
        class_name, *args = line.split()
        if len(args) == 1:
            class_name = args[0]

        if class_name and class_name not in models.storage.CLASSES_DICT:
            print("** class doesn't exist **")
            return

        objects = models.storage.all()
        for key, val in objects.items():
            if class_name:
                if key.startswith(class_name):
                    print(str(val))
            else:
                print(str(val))

    def do_show(self, line):
        """ method to show command to print
        the string representation of an instance """
        args = line.split()
        class_name = args[0]
        if not args:
            print("** class name missing **")
            return

        elif class_name not in models.storage.CLASSES_DICT:
            print("** class doesn't exist **")
            return

        elif len(args) < 2:
            print("** instance id missing **")
            return

        else:
            objects = models.storage.all()
            instance_id = args[1]
            key = "{}.{}".format(class_name, instance_id)
            if key in objects.keys():
                print(objects[key].__str__())
            else:
                print("** no instance found **")
                return

    def do_destroy(self, line):
        """ delete an instance.
        Args:
           line: input command.
        """
        if not line:
            print("** class name missing **")
            return
        class_name, *args = line.split()
        if len(args) == 1:
            print("** instance id missing **")
            return
        class_name = args[1]
        if class_name not in models.storage.CLASSES_DICT:
            print("** class doesn't exist **")
            return
        obj_id = args[0]
        key = class_name + "." + obj_id
        objects = models.storage.all()
        if key not in models.storage.all():
            print("** no instance found **")
            return
        else:
            objects.pop(key)
            models.storage.save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()