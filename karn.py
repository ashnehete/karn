import cmd

from commands.get import GetCommand
from commands.incr import IncrCommand
from commands.incrby import IncrbyCommand
from commands.set import SetCommand
from commands.delete import DelCommand


class Karn(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(karn) '
    multi_mode = False
    multi_commands_queue = []

    def do_GET(self, arg):
        op = self.run(GetCommand, arg)
        if op:
            print(op)

    def do_SET(self, arg):
        op = self.run(SetCommand, arg)
        if op:
            print(op)

    def do_DEL(self, arg):
        op = self.run(DelCommand, arg)
        if op:
            print(op)

    def do_INCR(self, arg):
        op = self.run(IncrCommand, arg)
        if op:
            print(op)

    def do_INCRBY(self, arg):
        op = self.run(IncrbyCommand, arg)
        if op:
            print(op)

    def do_MULTI(self, arg):
        self.multi_mode = True

    def do_EXEC(self, arg):
        self.multi_mode = False
        self.cmdqueue.extend(self.multi_commands_queue)
        self.multi_commands_queue = []

    def do_DISCARD(self, arg):
        self.multi_mode = False
        self.multi_commands_queue = []

    def do_COMPACT(self, arg):
        pass

    def do_EXIT(self, arg):
        return True

    def run(self, command_class, arg):
        command = command_class(arg)
        try:
            command.validate()
            if self.multi_mode:
                self.multi_commands_queue.append(f'{command} {arg}')
            else:
                return command.execute()
        except Exception as e:
            return f'(error) {e}'