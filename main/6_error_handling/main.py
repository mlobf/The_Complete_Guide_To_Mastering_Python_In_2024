"""Simple review - error handling
"""

from aux.else_finally import else_finally
from aux.raise_statement import raise_statement, is_connected
from aux.unknown_error import unknown_error


if __name__ == "__main__":
    # else_finally()
    # raise_statement()
    """
    try:
        is_connected(connection=True)
    except ConnectionError:
        print("There is no connection.")

    """
    # unknown_error(range(100))
    unknown_error(["marcos", "carlos"])
