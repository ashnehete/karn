from commands.basecommand import BaseCommand
from db import DB


class GetCommand(BaseCommand):
    def __init__(self, raw_arg):
        super(GetCommand, self).__init__('GET', raw_arg)
        self.key = None

    def execute(self):
        db = DB.instance()
        value = db.get(self.key)
        return value if value else '(nil)'

    def validate(self):
        self.key = self.raw_arg.split(' ', 1)[0]
        if not self.key:
            raise Exception('Wrong number of arguments')
