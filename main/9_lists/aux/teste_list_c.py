"""Teste de list_comprehentions
"""


def teste_list() -> list[int]:
    """Crie um list_comprehentions que gere uma lista de 10 numeros"""
    return [x for x in range(10)]


def slicing_lists():
    """"""
    numbers: list[int] = list(range(21))

    print(numbers[::3])
    print(numbers[10::3])
    print(numbers[10:16:2])
    print(numbers[10:])
    print(numbers[:10])
