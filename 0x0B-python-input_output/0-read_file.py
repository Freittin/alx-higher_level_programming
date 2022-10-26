#!/usr/bin/python3
''' Module for read_file func '''


def read_file(filename=""):
    ''' Read from a file '''
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        print(content, end="")
