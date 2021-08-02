from commands.incrby import IncrbyCommand


class IncrCommand(IncrbyCommand):
    def __init__(self, raw_arg):
        super(IncrCommand, self).__init__(raw_arg)
        self.command = 'INCR'
        self.incr_by = 1

    def validate(self):
        self.key = self.raw_arg.split(' ', 1)[0]
        if not self.key:
            raise Exception('Wrong number of arguments')
