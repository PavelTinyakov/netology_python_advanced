


def decor(func):
    def wrapper(*args, **kwargs):
        return func(*args, ** kwargs) + 100
    return wrapper


@decor
def summ(a, b):
    return a + b


print(summ(1, 2))

# find_key_words