import cmd

from commands.get import GetCommand


class Karn(cmd.Cmd):
    """Simple command processor example."""
    prompt = '(karn) '

    def do_GET(self, arg):
        GetCommand(arg).execute()

    def do_SET(self, arg):
        pass

    def do_DEL(self, arg):
        pass

    def do_MULTI(self, arg):
        pass

    def do_INCR(self, arg):
        pass

    def do_INCRBY(self, arg):
        pass

    def do_EXEC(self, arg):
        pass

    def do_DISCARD(self, arg):
        pass

    def do_COMPACT(self, arg):
        pass

    def do_EXIT(self, arg):
        return True
