def only_numbers_allowed(func):
    def wrapper(*args):
        for value in list(args):
            if not isinstance(value, (int, float)):
                raise TypeError("All parameters must be numbers")
        return func(*args)
    return wrapper

@only_numbers_allowed
def add(a, b):
    return a + b

print(add(6, "c")) 