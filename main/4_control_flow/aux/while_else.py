"""
Using loop while with else statement
"""


def while_else():
    """Applying a simple loop while with else statement"""
    i = 0
    while i < 3:
        print(i, end="")
        i += 1

        if i == 2:
            break
    else:
        print("Success")
