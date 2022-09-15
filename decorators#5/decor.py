from datetime import datetime


def logger(path):
    def logger_(some_function):
        def wrapper(*args, **kwargs):
            date = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
            func_name = some_function.__name__
            result = some_function(*args, **kwargs)
            with open(f'{path}/{func_name}_log', 'a') as file:
                file.write(f'{date} | {func_name} | args={args}, kwargs={kwargs}| {result}\n')
            return result
        return wrapper
    return logger_
