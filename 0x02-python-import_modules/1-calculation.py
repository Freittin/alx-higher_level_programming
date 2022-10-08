#!/usr/bin/python3
if __name__ == "__main__":
    import calculator_1 as calc

    a = 10
    b = 5
    print("{0} + {1} = {2}".format(a, b, calc.add(a, b)))
    print("{0} - {1} = {2}".format(a, b, calc.sub(a, b)))
    print("{0} * {1} = {2}".format(a, b, calc.mul(a, b)))
    print("{0} / {1} = {2}".format(a, b, calc.div(a, b)))
