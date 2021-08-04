# Karn In-Memory Database

Karn is a simple in-memory database accessible why the command line.

## Commands

1. GET - Get the value of a key
2. SET - Set the value of a key
3. DEL - Delete a key and its value
4. INCR - Increment the integer value of the key by 1
5. INCRBY - Increment the integer value of the key by input number
6. MULTI - Start a multi line command
7. EXEC - Execute a multi line command
8. DISCARD - Discard a multi line command
9. COMPACT - Compacts the previous commands

## Technical Details

The database is implemented as a python `dict` data structure. Access to the database is controlled using a **
Singleton** class.

The commands are parsed using the in-built `cmd.Cmd` module provided by python.

A `Makefile` is provided for ease of use.

First time setup,  
```shell
$ make init
```

Run command line program  
```shell
$ make run
```

Run tests  
```shell
$ make test
```

## Limitations
1. All data will be lost after the terminal is closed.
2. `SET` command will convert any numeric input to int. All other values are stored as string.
3. Input errors are handled wherever possible except for the `COMPACT` command.
4. `COMPACT` command considers history from the start of execution but ignores `MULTI`, `EXEC`, `DISCARD`.