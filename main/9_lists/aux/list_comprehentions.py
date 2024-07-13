"""Just a simple list cooprehentions
"""


def list_comprehentions_old():
    """simple list list_comprehentions"""
    sample_list = []

    for i in range(10):
        sample_list.append(i)

    return sample_list


def list_comprehentions_new():
    """simple list list_comprehentions"""
    # return type([x for x in range(100) if x > 3 and x != 4 or x%3]) # return an list

    return [x**2 for x in range(100) if x > 3 and x != 4 or x % 3 == 0]


def list_comprehentions_captitalize(people: list[str]) -> list:
    """simple list list_comprehentions use"""
    return [p.upper() for p in people]
