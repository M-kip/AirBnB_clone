#!/usr/bin/python3
"""
   Implements command line interface using the cmd module

   Classes
   -------
   HBNBCommand(cmd.Cmd)
       implements the various commands
"""
import cmd
import sys
import os
import models
import inspect
from models import storage

# TODO checks if instance of the same class exists in storage
class HBNBCommand(cmd.Cmd):
    """
       Creates the command line interface

    Attributes
    ---------
    intro: str
        Introduces the class and it's  functions
    prompt: str
        The place holder where user inputs commans

    Methods
    -------
    do_quit(self)
        closes the command line interface
    do_help(self)
        inbuilt command that prints help message
    do_EOF(self)
        exit the program
    """

    prompt = "(hbnb)"

    def do_quit(self, arg):
        """ closes/exits the command line interface
        """
        return True

    def do_EOF(self, arg):
        """ Exits the command interface when supplied with EOF character
        """
        return True
   
    def emptyline(self):
        """ Do nothing
        """
        pass

    def do_create(self, arg):
        """Creates an instance of the class specified in the arg var
        """
        if not arg:
            print("** class name missing **")

        elif not arg in inspect.getmembers(models):
            print("** class doesn't exists **")
        else:
            my_model = models.base_model.BaseModel()
            my_model.save()
            print(my_model.id)

    def do_show(self, arg):
        """ Prints and instance based on the id and class name
        """
        objs = storage.all()
        args = arg.split()
        if len(args) < 1:
            print("** class name missing **")
        elif len(args) == 1:
            print("** instance id is missing **")

        if not args[0] in inspect.getmembers(models):
            print("** class doesn't exists **")
        else:
            if not args[1] in objs.keys():
                print("** no instance found **")

    def do_destory(self, arg):
        """ destorys an instance object
        """
        if not args:
            print("** class name is missing **")
        args = arg.split()
        class_ = args[0]
        id = args[1]
        objs = storage.all()

        if not id:
            print("** instance id is missing **")
        if not class_ in inspect.getmembers(models):
            print("** class doesn't exists **")
        else:
            if not id in objs.keys():
                print("** no instance found **")
            else:
                del objs[id]
    def do_all(self, args):
        """Prints all the instances of arg
        """

        objs = storage.all()
        print(objs)
         
    def do_update(self, line):
        """Updates an instance by adding or updating attribute.
        """
        if line == "" or line is None:
            print("** class name missing **")
            return

        rex = r'^(\S+)(?:\s(\S+)(?:\s(\S+)(?:\s((?:"[^"]*")|(?:(\S)+)))?)?)?'
        match = re.search(rex, line)
        classname = match.group(1)
        uid = match.group(2)
        attribute = match.group(3)
        value = match.group(4)
        if not match:
            print("** class name missing **")
        elif classname not in storage.classes():
            print("** class doesn't exist **")
        elif uid is None:
            print("** instance id missing **")
        else:
            key = "{}.{}".format(classname, uid)
            if key not in storage.all():
                print("** no instance found **")
            elif not attribute:
                print("** attribute name missing **")
            elif not value:
                print("** value missing **")
            else:
                cast = None
                if not re.search('^".*"$', value):
                    if '.' in value:
                        cast = float
                    else:
                        cast = int
                else:
                    value = value.replace('"', '')
                attributes = storage.attributes()[classname]
                if attribute in attributes:
                    value = attributes[attribute](value)
                elif cast:
                    try:
                        value = cast(value)
                    except ValueError:
                        pass  # fine, stay a string then
                setattr(storage.all()[key], attribute, value)
                storage.all()[key].save()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
