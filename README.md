# Joe's Judge Bot

A.k.a. @joedgebot for those who are used to it.

This bot was written to be ran with Python 3.4.4 with [Telepot](https://github.com/nickoala/telepot) and [Make](https://www.gnu.org/software/make/).

# Building

The bot can be ran by typing:

```
make run API=YOUR_API_HERE
```
Its unit tests are also provided in the makefile and can be run by:
```
make test
```


# Usage

Type

```
/start
```

into the bot to start talking to it. The first message must be your source code, and its first line must be

```
#! language
```

where `language` is the language of your source code. Don't worry, this line is removed from the source code before running it. The second message must be your input, which will be provided to your program by through the standard input. A procedure can be cancelled by saying the following command to the bot:

```
/cancel
```


## Available languages ##

I have currently implemented the following languages:

- Python (`python3 script.py`)
- Ruby (`ruby script.rb`)
- C (`gcc script.c -o script.c.out; ./script.c.out`)
- Go (`go run script.go`)
- Lua (`lua script.lua`)
- Java (`javac Script.java; java Script`)

And I am planning on providing the following languages:

- C++
- C#
- Javascript
