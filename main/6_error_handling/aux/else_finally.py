"""else finally"""


def else_finally():
    """In the implementation of the 'else' and 'finally' blocks,
    it's important to ensure that the 'finally'
    block executes regardless of whether an exception is raised."""

    user_input: str = input("You there.....please input a simple number here ")

    try:
        number: float = float(user_input)
        print(number)
    except Exception as e:
        print("e ", e)
    else:
        print("Sucessufully executed code")
    finally:
        print('This block of code  will always run anyway')
