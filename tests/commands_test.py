from karn import Karn

karn = Karn()


def test_compact(capsys):
    karn.onecmd('SET counter 10')
    captured = capsys.readouterr()
    assert captured.out == 'OK\n'

    karn.onecmd('INCR counter')
    captured = capsys.readouterr()
    assert captured.out == '11\n'

    karn.onecmd('INCRBY counter 10')
    captured = capsys.readouterr()
    assert captured.out == '21\n'

    karn.onecmd('COMPACT')
    captured = capsys.readouterr()
    assert captured.out == 'SET counter 12\n'


def test_basic(capsys):
    karn.onecmd('SET hello world')
    captured = capsys.readouterr()
    assert captured.out == 'OK\n'

    karn.onecmd('GET hello')
    captured = capsys.readouterr()
    assert captured.out == 'world\n'

    karn.onecmd('DEL hello')
    captured = capsys.readouterr()
    assert captured.out == 'OK\n'

    karn.onecmd('GET hello')
    captured = capsys.readouterr()
    assert captured.out == '(nil)\n'


def test_numeric(capsys):
    karn.onecmd('SET counter 10')
    captured = capsys.readouterr()
    assert captured.out == 'OK\n'

    karn.onecmd('INCR counter')
    captured = capsys.readouterr()
    assert captured.out == '11\n'

    karn.onecmd('INCRBY counter 10')
    captured = capsys.readouterr()
    assert captured.out == '21\n'


def test_numeric_advanced(capsys):
    karn.onecmd('INCR c1')
    captured = capsys.readouterr()
    assert captured.out == '1\n'

    karn.onecmd('INCRBY c2 10')
    captured = capsys.readouterr()
    assert captured.out == '10\n'


def test_multi_exec(capsys):
    karn.onecmd('MULTI')
    captured = capsys.readouterr()
    assert captured.out == ''

    karn.onecmd('SET m1 world')
    captured = capsys.readouterr()
    assert captured.out == ''

    karn.onecmd('GET m1')
    captured = capsys.readouterr()
    assert captured.out == ''

    karn.onecmd('EXEC')
    captured = capsys.readouterr()
    assert captured.out == 'OK\nworld\n'

    karn.onecmd('GET m1')
    captured = capsys.readouterr()
    assert captured.out == 'world\n'


def test_multi_discard(capsys):
    karn.onecmd('MULTI')
    captured = capsys.readouterr()
    assert captured.out == ''

    karn.onecmd('SET m2 world')
    captured = capsys.readouterr()
    assert captured.out == ''

    karn.onecmd('GET m2')
    captured = capsys.readouterr()
    assert captured.out == ''

    karn.onecmd('DISCARD')
    captured = capsys.readouterr()
    assert captured.out == ''

    karn.onecmd('GET m2')
    captured = capsys.readouterr()
    assert captured.out == '(nil)\n'
