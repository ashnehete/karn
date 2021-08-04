import cmd
import traceback

from commands.compact import CompactCommand
from commands.get import GetCommand
from commands.incr import IncrCommand
from commands.incrby import IncrbyCommand
from commands.set import SetCommand
from commands.delete import DelCommand


class Karn(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(karn) '

    # For Multi line processing
    multi_mode = False
    multi_commands_queue = []

    # For compact processing
    command_history = []

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
        for command in self.multi_commands_queue:
            self.onecmd(command)
        self.multi_commands_queue = []

    def do_DISCARD(self, arg):
        self.multi_mode = False
        self.multi_commands_queue = []

    def do_COMPACT(self, arg):
        op = self.run(CompactCommand, self.command_history)
        if op:
            print(op)

    def do_EXIT(self, arg):
        return True

    def run(self, command_class, arg):
        command = command_class(arg)
        self.command_history.append({
            'cmd': str(command),
            'arg': arg
        })

        try:
            command.validate()
            if self.multi_mode:
                self.multi_commands_queue.append(f'{command} {arg}')
            else:
                return command.execute()
        except Exception as e:
            print(traceback.format_exc())
            return f'(error) {e}'
