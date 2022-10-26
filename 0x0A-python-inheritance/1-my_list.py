#!/usr/bin/python3
''' Module for MyList class '''


class MyList(list):
    ''' Custom list class'''

    def print_sorted(self):
        ''' Instance method:
            print sorted list
        '''
        print(sorted(self))


    if __name__ == "__main__":
        import doctest
        doctest.testfile("tests/1-my_list.txt")
