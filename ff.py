#!/usr/bin/python3
"""
this is 'console' module

this module contains 1 class: HBNBCommand

this class contains 9 methods: do_EOF, do_help, do_quit,
                               do_create, do_show, do_destroy,
                               do_all, do_update, emptyline
"""
import cmd
import models
from shlex import split
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    This is a new class to console
    """
    prompt = "(hbnb) "
    cls_objs = ["BaseModel", "User", "Amenity", "City",
                "Place", "Review", "State"]
    cmds = ["EOF", "help", "quit", "create",
            "count", "show", "destroy",
            "all", "update"]

    def do_EOF(self, line):
        """EOF command to exit the program
        """
        return True

    def do_help(self, line):
        """Help command to show docstring for a command
        """
        cmd.Cmd.do_help(self, line)

    def do_quit(self, line):
        """Quit command to exit the program
        """
        raise SystemExit

    def do_create(self, line):
        """Create command to create a new instance of BaseModel,
        saves it (to the JSON file) and prints the id.
        Ex: $ create BaseModel
        """
        new_list = line.split()
        if not new_list:
            print("** class name missing **")
            return
        elif new_list[0] not in HBNBCommand.cls_objs:
            print("** class doesn't exist **")
            return
        else:
            obj = eval(new_list[0]+'()')
            obj.save()
            print(obj.id)

    def do_count(self, line):
        """Count command to retrieve the number of instances \
        of a class.
        Ex: $ count BaseModel
        """
        count = 0
        new_list = line.split()
        if new_list[0] in self.cls_objs:
            for key in models.storage.all().keys():
                if new_list[0] in key:
                    count += 1
        print(count)

    def do_show(self, line):
        """Show command to print the string representation of an instance,
        based on the class name and id.
        Ex: $ show BaseModel 1234-1234-1234
        """
        new_list = line.split()
        if not new_list:
            print("** class name missing **")
            return
        elif new_list[0] not in HBNBCommand.cls_objs:
            print("** class doesn't exist **")
            return
        elif len(new_list) < 2:
            print("** instance id missing **")
            return
        else:
            objs = models.storage.all()
            key = new_list[0] + '.' + new_list[1]
            if key not in objs.keys():
                print("** no instance found **")
                return
            else:
                print(objs[key].__str__())

    def do_destroy(self, line):
        """Destroy command to delete an instance based on the class name and id
        (save the change into the JSON file).
        Ex: $ destroy BaseModel 1234-1234-1234
        """
        new_list = line.split()
        if not new_list:
            print("** class name missing **")
            return
        elif new_list[0] not in HBNBCommand.cls_objs:
            print("** class doesn't exist **")
            return
        elif len(new_list) < 2:
            print("** instance id missing **")
            return
        else:
            objs = models.storage.all()
            key = "{}.{}".format(new_list[0], new_list[1])
            if key not in objs.keys():
                print("** no instance found **")
                return
            else:
                del(objs[key])
                models.storage.save()

    def do_all(self, line):
        """All command to print all string representation of all instances,
        based or not on the class name.
        Ex: $ all BaseModel or $ all
        """
        new_list = line.split()

        if not len(new_list) or new_list[0] in HBNBCommand.cls_objs:
            string_list = []
            objs = models.storage.all()
            for obj in objs.values():
                string_list.append(obj.__str__())
            print(string_list)
        else:
            print("** class doesn't exist **")
            return

    def do_update(self, line):
        """Update command to update an instance based on the class name and id
        by adding or updating attribute (save the change into the JSON file).
        Ex: $ update BaseModel 1234-1234-1234 email "aibnb@mail.com"
        """
        new_list = line.split()
        if not new_list:
            print("** class name missing **")
            return
        elif new_list[0] not in HBNBCommand.cls_objs:
            print("** class doesn't exist **")
            return
        elif len(new_list) < 2:
            print("** instance id missing **")
            return
        elif len(new_list) < 3:
            print("** attribute name missing **")
            return
        elif len(new_list) < 4:
            print("** value missing **")
            return
        else:
            objs = models.storage.all()
            key = "{}.{}".format(new_list[0], new_list[1])
            if key not in objs.keys():
                print("** no instance found **")
                return
            setattr(objs[key], new_list[2], eval(new_list[3]))
            objs[key].save()

    def default(self, line):
        """Executes a command.
        """

        words = line.split('.')
        if "(" in words[-1] and ")" in words[-1]:
            method_and_args = words[-1].split("(")
            method = method_and_args[0]
            args = method_and_args[1].rstrip(")").split(",")

            if method not in self.cmds:
                print("** Unknown syntax:", method)
                return

            class_name = ".".join(words[:-1])
            if class_name not in self.cls_objs:
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

    def emptyline(self):
        """to ignore performing any command when presseing only enter
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
