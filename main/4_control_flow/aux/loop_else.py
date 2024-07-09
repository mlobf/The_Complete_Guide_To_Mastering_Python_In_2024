"""
Using loop with else statement
"""


def loop_else():
    """Applying a simple loop with else statement"""
    for i in range(5):
        print(i, end="")

        if i == 2:
            break
    else:
        print("Success")
