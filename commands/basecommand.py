class BaseCommand:
    def __init__(self, command, raw_arg):
        self.command = command
        self.raw_arg = raw_arg

    def execute(self):
        raise NotImplementedError("Please Implement this method")

    def validate(self):
        raise NotImplementedError("Please Implement this method")

    def __str__(self):
        return self.command
