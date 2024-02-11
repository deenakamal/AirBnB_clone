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
    cmds = ['EOF', 'help', 'quit', 'all',
            'count', 'show', 'destroy', 'update', 'create']
    cls_names = models.storage.CLASSES_DICT

    def do_quit(self, line):
        """To Exit the program"""
        return True

    def do_EOF(self, line):
        """EOf exit """
        return True

    def emptyline(self):
        """Empty line."""
        pass

    def do_help(self, line):
        """Help to show docstring for a command"""
        cmd.Cmd.do_help(self, line)

    def do_count(self, line):
        """Count command to retrieve the number of instances
        Args:
            line: input command
        """
        count = 0
        _list = line.split()
        if _list[0] in self.cls_names:
            for key in models.storage.all().keys():
                if _list[0] in key:
                    count += 1
        print(count)

    def do_create(self, line):
        """Create a new instance of BaseModel"""
        if not line:
            print("** class name missing **")
            return
        _list = line.split()
        class_name = _list[0]
        if class_name not in models.storage.CLASSES_DICT:
            print("** class doesn't exist **")
            return
        new_obj = models.storage.CLASSES_DICT[class_name]()
        new_obj.save()
        print(new_obj.id)

    def do_all(self, line):
        """Prints all string representations of instances
        based on the class
        Args:
            line: command
        """
        objects = models.storage.all()
        if not line:
            result = []
            for obj in objects.values():
                result.append(str(obj))
            print(result)
            return
        args = line.split()
        if len(args) == 1:
            class_name = args[0]

        if class_name and class_name not in models.storage.CLASSES_DICT:
            print("** class doesn't exist **")
            return
        all = []
        for obj in objects.values():
            if obj.__class__.__name__ == args[0]:
                all.append(str(obj))
        print(all)

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
        line = line.split()
        if not line:
            print("** class name missing **")
            return
        
        class_name = line[0]
        if class_name not in models.storage.CLASSES_DICT:
            print("** class doesn't exist **")
            return
        if len(line) < 2:
            print("** instance id missing **")
            return
        obj_id = line[1]
        objects = models.storage.all()
        key = class_name + "." + obj_id
        if key not in objects.keys():
            print("** no instance found **")
            return
        else:
            objects.pop(key)
            models.storage.save()

    def do_update(self, line):
        """Update an instance based on the class name and id"""
        args = line.split()

        if len(args) < 4:
            print("** Not enough arguments for update **")
            return

        class_name = args[0]
        obj_id = args[1]
        attribute_name = args[2]

        if class_name not in models.storage.CLASSES_DICT:
            print("** Class doesn't exist **")
            return
        key = "{}.{}".format(class_name, obj_id)
        objects = models.storage.all()
        if key not in objects:
            print("** No instance found **")
            return

        obj = objects[key]

        attribute_value = eval(args[3])
        setattr(obj, attribute_name, attribute_value)
        obj.save()

    def default(self, line):
        """Executes a command."""
        words = line.split('.')
        if "(" in words[-1] and ")" in words[-1]:
            method_and_args = words[-1].split("(")
            method = method_and_args[0]
            args = method_and_args[1].rstrip(")").split(",")

            if method not in self.cmds:
                print("** Unknown syntax:", method)
                return
            class_name = ".".join(words[:-1])
            if class_name not in self.cls_names:
                print("** class doesn't exist **")
                return

            function = getattr(self, "do_" + method)
            full_args = " ".join([class_name] + args)
            function(full_args)
        else:
            command = words[0]
            if command not in self.cmds:
                print("** Unknown syntax:", command)
                return
            function = getattr(self, "do_" + command)
            function(" ".join(words[1:]))


if __name__ == "__main__":
    HBNBCommand().cmdloop()
