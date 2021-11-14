from functools import wraps


def decorator_name(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # 1. Code to execute BEFORE calling the decorated function

        # 2. Calling the func and returns her values
        #
             return func(*args, **kwargs)

    # 3. Code to execute instead of calling
    return wrapper
