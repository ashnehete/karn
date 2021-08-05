from commands.basecommand import BaseCommand
from db import DB


class CompactCommand(BaseCommand):
    def __init__(self, raw_arg):
        super(CompactCommand, self).__init__('COMPACT', raw_arg)
        self.command_history = raw_arg

    def execute(self):
        keys = {}
        for command in self.command_history:
            cmd = command.get('cmd')
            if cmd == 'COMPACT':
                continue

            args = command.get('arg').split(' ', 1)
            if cmd == 'DEL':
                if args[0] in keys:
                    del keys[args[0]]

            elif cmd == 'SET':
                value = int(args[1]) if args[1].isdigit() else args[1]
                keys[args[0]] = value

            elif cmd == 'INCR':
                key = args[0]
                keys[key] = keys[key] + 1 if key in keys else 1

            elif cmd == 'INCRBY':
                key = args[0]
                keys[key] = keys[key] + int(args[1]) if key in keys else int(args[1])

        return '\n'.join([f'SET {key} {keys[key]}' for key in keys])

    def validate(self):
        return True
