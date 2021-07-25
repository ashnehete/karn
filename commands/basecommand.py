class BaseCommand:
    def __init__(self, arg):
        self.arg = arg

    def execute(self):
        raise NotImplementedError("Please Implement this method")

    def validate(self):
        raise NotImplementedError("Please Implement this method")
