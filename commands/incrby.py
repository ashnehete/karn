from commands.basecommand import BaseCommand
from db import DB


class IncrbyCommand(BaseCommand):
    def __init__(self, raw_arg):
        super(IncrbyCommand, self).__init__('INCRBY', raw_arg)
        self.key = None
        self.incr_by = 0

    def execute(self):
        db = DB.instance()
        value = db.get(self.key)

        # Create new key if it doesn't exist
        if value is None:
            value = 0

        if type(value) is int:
            value = value + self.incr_by
            db.set(self.key, value)
            return value
        else:
            raise Exception('Value is not an integer')

    def validate(self):
        args = self.raw_arg.split(' ', 1)
        self.key = args[0]

        if len(args) < 2 or not self.key:
            raise Exception('Wrong number of arguments')

        if args[1].isdigit():
            self.incr_by = int(args[1])
        else:
            raise Exception('Argument is not an integer')
