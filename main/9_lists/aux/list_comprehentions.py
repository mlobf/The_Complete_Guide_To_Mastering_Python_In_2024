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
    return [x for x in range(10) if x > 3 and x != 4]
