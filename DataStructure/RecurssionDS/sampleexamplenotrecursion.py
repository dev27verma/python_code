def method_one():
    method_two()
    print("print 1")


def method_two():
    method_three()
    print("print 2")


def method_three():
    method_four()
    print("print 3")


def method_four():
    print("print 4")


method_one()
