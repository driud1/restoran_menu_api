def foo(a):
    print(locals())
    print(globals())
    return a ** 5


def bar(a, b):
    print(locals())
    print(globals())
    return a - b




def cycle():
    print(locals())
    print(globals())
    for i in reversed(range(10)):
        print(i)


if __name__ == '__main__':
    cycle()
    foo(4)
    spam = foo(2)
    eggs = bar(4, 8)

    print(spam, eggs)