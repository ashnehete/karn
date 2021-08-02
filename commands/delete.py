from commands.basecommand import BaseCommand
from db import DB


class DelCommand(BaseCommand):
    def __init__(self, raw_arg):
        super(DelCommand, self).__init__('DEL', raw_arg)
        self.key = None

    def execute(self):
        db = DB.instance()
        db.delete(self.key)
        return 'OK'

    def validate(self):
        self.key = self.raw_arg.split(' ', 1)[0]
        if not self.key:
            raise Exception('Wrong number of arguments')
