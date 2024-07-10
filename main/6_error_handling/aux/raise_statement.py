"""raise statement"""


def raise_statement():
    """In the implementation of the 'try' and 'finally' blocks with more,
    especific error handling provided by raise statement."""

    user_input: str = input("You there.....please input a simple number here ")
    if user_input == "0":
        raise Exception("Please never use 0")


def is_connected(connection: bool) -> str:
    """Other use of raise statement"""

    if not connection:
        raise ConnectionError("No internet")
    return print("Connected to internet")
