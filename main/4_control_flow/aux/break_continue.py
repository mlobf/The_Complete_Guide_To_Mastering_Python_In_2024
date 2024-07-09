"""
Just a simple example for use continue and break
"""


def with_for_break_continue():
    """Simple implemetation of topic's concepts
    for use by side break and continue
    """
    for i in range(5):
        if i == 3:
            continue
        if i == 4:
            print("Break triggered!")
        print(i)


def with_for_break():
    """Simple implemetation of topic's concepts
    for use
    """
    for i in range(10):
        print(i)
        if i == 5:
            break
    print("Done")


def with_while_break():
    """Simple implemetation of topic's concepts
    while use
    """
    i = 0
    while i < 3:
        print(i)
        if i == 1:
            break
        i += 1
    print("Done")


def with_for_continue():
    """Simple implemetation of topic's concepts
    for use
    """
    for i in range(5):
        if i == 3:
            continue
        print(i)
