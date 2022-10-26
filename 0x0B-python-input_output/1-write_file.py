#!/usr/bin/python3
''' Module for write_file func '''


def write_file(filename="", text=""):
    ''' writes a string to a text file '''
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
