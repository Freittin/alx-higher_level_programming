#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    arg_len = len(sys.argv)
    i = 1
    if arg_len - 1 > 1:
        print("{} arguments:".format(arg_len - 1))

    else:
        print("{} argument.".format(arg_len - 1))
    while i < arg_len:
        print("{0} :{1}".format(i, sys.argv[i]))
        i += 1
