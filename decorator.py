import logging
import time

def log(level):
    def decorator(func):
        if callable(func):
            def wrapper(*args, **kwargs):
                start = time.time()
                logging.log(level, f"Calling function {func.__name__} with arguments {args} and {kwargs}")
                result = func(*args, **kwargs)
                end = time.time()
                logging.log(level, f"Function {func.__name__} returned {result} in {end - start} seconds")
                return result
            return wrapper
        else:
            class Wrapper(func):
                def __init__(self, *args, **kwargs):
                    logging.log(level, f"Instantiating class {func.__name__} with arguments {args} and {kwargs}")
                    super().__init__(*args, **kwargs)
            return Wrapper
    return decorator