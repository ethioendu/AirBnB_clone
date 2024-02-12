#!/usr/bin/python3
"""consol model contains class HBNBCommand
"""
import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.state import State
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    """class that inherice from cmd.Cmd
       it has prompt (Hbnb) and close with 'quit'
    """
    prompt = "(hbnb) "
    my_class = {"BaseModel",
                "User",
                "City",
                "State",
                "Amenity",
                "Place",
                "Review"}

    def do_create(self, args):
        """creates a class
        Usage: create <class Name>
        <class Name> should be from given options
        >BaseModel
        """
        if not args:
            print("** class name missing **")
            return

        args = shlex.split(args)
        class_name = args[0]

        if class_name not in self.my_class:
            print("** class doesn't exist **")
            return

        obj = eval(class_name)()
        obj.save()
        print(obj.id)

    def do_show(self, args):
        """displays mentioned class info
        Usage: show <class Name> <id>
        """
        if not args:
            print("** class name missing **")
            return

        args = shlex.split(args)
        class_name = args[0]

        if class_name not in self.my_class:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        all_instance = storage.all()

        if key in all_instance:
            obj = all_instance[key]
            print(obj)
        else:
            print("** no instance found **")

    def do_destroy(self, args):
        """delete a given class
        Usage: destroy <class name> <id>
        """
        if not args:
            print("** class name missing **")
            return

        args = shlex.split(args)
        class_name = args[0]

        if class_name not in self.my_class:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        all_instance = storage.all()

        if key in all_instance:
            del all_instance[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, args):
        """display all classes
        USage: all <class Name>
        """
        if args:
            class_name = args.split()[0]
            if class_name not in self.my_class:
                print("** class doesn't exist **")
                return

            objs = [str(obj) for obj in storage.all().values()
                    if class_name in obj.__class__.__name__]
        else:
            objs = [str(obj) for obj in storage.all().values()]

        print(objs)

    def do_update(self, args):
        """updates simple information str, number...
        Usage update <class> <id> <key> <value>
        """
        if not args:
            print("** class name missing **")
            return

        args = shlex.split(args)
        class_name = args[0]

        if class_name not in self.my_class:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = "{}.{}".format(class_name, obj_id)
        all_instance = storage.all()

        if key not in all_instance:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        attribute_name = args[2]
        if len(args) < 4:
            print("** value missing **")
            return

        attribute_value = args[3]
        obj = all_instance[key]
        setattr(obj, attribute_name, attribute_value)
        obj.save()

    def default(self, line):
        """Handles different methods of the form starting with class name
        then followed by a method
        Usage: <class name>.method()
        """
        args = line.split('.')
        if len(args) < 2:
            if args[0] in self.my_class:
                print("** method missing **")
            else:
                print("** unkown command **")
            return

        cl = args[0]
        method_args = args[1].split('(')
        method_name = method_args[0]
        if cl not in self.my_class:
            print("** class doesn't exist **")
        else:
            o = storage.all()
            ins = [obj for obj in o.values() if type(obj).__name__ == cl]
            if method_name == 'all':
                print([str(obj) for obj in ins])
            elif method_name == 'count':
                print(len(ins))
            elif method_name == 'show':
                if len(method_args) < 2 or not method_args[1].endswith(')'):
                    print("** instance id missing **")
                else:
                    instance_id = method_args[1][:-1]
                    key = class_name + "." + instance_id
                    if key in objects:
                        print(objects[key])
                    else:
                        print("** no instance found **")
            else:
                print("** method doesn't exist **")

    def do_count(self, args):
        """Counts the number of instances of a specific class
        Usage: count <ClassName>
        """
        if not args:
            print("** class name missing **")
            return

        class_name = args.split()[0]

        if class_name not in self.my_class:
            print("** class doesn't exist **")
            return

        instance_count = 0
        objects = storage.all()
        for obj in objects.values():
            if type(obj).__name__ == class_name:
                instance_count += 1
        print(instance_count)

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """Quit command to exit the prgram by Ctr+D
        """
        print()
        return True

    def emptyline(self):
        """skips to new prompt
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
