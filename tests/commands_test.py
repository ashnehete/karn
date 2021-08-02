from commands.get import GetCommand
from commands.incr import IncrCommand
from commands.incrby import IncrbyCommand
from commands.set import SetCommand
from commands.delete import DelCommand
from karn import Karn

karn = Karn()


def test_basic():
    karn.run(SetCommand, 'hello world')
    value = karn.run(GetCommand, 'hello')
    assert value == 'world'

    karn.run(DelCommand, 'hello')
    value = karn.run(GetCommand, 'hello')
    assert value is None


def test_numeric():
    karn.run(SetCommand, 'counter 10')
    value = karn.run(GetCommand, 'counter')
    assert value == 10

    value = karn.run(IncrCommand, 'counter')
    assert value == 11

    value = karn.run(IncrbyCommand, 'counter 10')
    assert value == 21


def test_numeric_advanced():
    value = karn.run(IncrCommand, 'c1')
    assert value == 1
    value = karn.run(GetCommand, 'c1')
    assert value == 1

    value = karn.run(IncrbyCommand, 'c2 10')
    assert value == 10
    value = karn.run(GetCommand, 'c2')
    assert value == 10
