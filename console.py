#!/usr/bin/python3
"""
"""
import cmd
import shlex
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    """
    prompt = "(hbnb) "
    my_class = {"BaseModel"}

    def do_create(self, args):
        """
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
        """
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
        """
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
        """
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
        """
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

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        """
        print()
        return True

    def emptyline(self):
        """
        """
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
