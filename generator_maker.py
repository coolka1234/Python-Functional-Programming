def make_generator(f):
    def generator():
        i = 1
        while True:
            yield f(i)
            i += 1
    return generator()
import functools

def make_generator_mem(f):
    @functools.lru_cache(maxsize=None)
    def memoized_f(n):
        return f(n)

    def generator():
        i = 1
        while True:
            yield memoized_f(i)
            i += 1
    return generator()
