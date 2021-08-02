from commands.basecommand import BaseCommand
from db import DB


class SetCommand(BaseCommand):
    def __init__(self, raw_arg):
        super(SetCommand, self).__init__('SET', raw_arg)
        self.key = None
        self.value = None

    def execute(self):
        db = DB.instance()
        db.set(self.key, self.value)
        return 'OK'

    def validate(self):
        args = self.raw_arg.split(' ', 1)
        self.key = args[0]

        if not self.key:
            raise Exception('Wrong number of arguments')

        self.value = args[1] if len(args) > 1 else ''

        if self.value.isdigit():
            self.value = int(self.value)
