# Overview

This is a program designed to run a chatroom with a client and server. Currently, this is all done in 
command line. You can choose the IP and port that you want to use, as well as set nicknames for
each person who joins.

[Software Demo Video](https://youtu.be/b6y2SI3so5E)

# Network Communication

For the program, it uses client/server as the model. Additionally, it was built for TCP.
Each message is encoded and decoded using utf-8.

The IP and port number used for testing are 127.0.0.1 (local) and 12345

# Development Environment

* Visual Studio Code 1.72
* Python 3.8.5
* threading and socket

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Build a Chatroom App with Python](https://python.plainenglish.io/build-a-chatroom-app-with-python-458fc435025a)
* [Simple TCP Chatroom in Python](https://www.youtube.com/watch?v=3UOyky9sEQY)
* [How to create a chatroom in Python?](https://www.askpython.com/python/examples/create-chatroom-in-python)
* [An Intro to Threading in Python](https://realpython.com/intro-to-python-threading/)
* [Socket Programming in Python (Guide)](https://realpython.com/python-sockets/)

# Future Work

* Add GUI using tkinter - see tkinter_test.py
* Add in-chat command to change nickname
* Add other in-chat commands