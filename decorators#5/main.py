import os

from decor import logger


path = os.path.dirname(os.path.realpath(__file__))


@logger(path)
def flat_generator(some_list):
    for element in some_list:
        if isinstance(element, list):
            yield from flat_generator(element)
        else:
            yield element


if __name__ == "__main__":
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None],
    ]

    for i in flat_generator(nested_list):
        print(i)
