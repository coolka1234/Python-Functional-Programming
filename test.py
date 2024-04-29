from functions import *
from higher_oder import *
from password_generator import *
from generator_maker import *
from decorator import *
print(acronym(["Zakład", "Ubezpieczeń", "Społecznych"]))  # Outputs: ZUS
print(median([1,1,19,2,3,4,4,5,1]))  # Outputs: 3
print(pierwiastek(3, epsilon = 0.1))  # Outputs: 1.7321428571428572
print(make_alpha_dict("on i ona"))  
# Outputs: {'a': ['ona'], 'i': ['i'], 'n': ['on', 'ona'], 'o': ['on', 'ona']}
print(list(flatten([1, [2, 3], [[4, 5], 6]])))  # Outputs: [1, 2, 3, 4, 5, 6]
print(forall(lambda x: x > 0, [1, 2, 3]))  # Outputs: True
print(exists(lambda x: x > 0, [-1, -2, 3]))  # Outputs: True
print(atleast(2, lambda x: x > 0, [-1, 2, 3]))  # Outputs: True
print(atmost(2, lambda x: x > 0, [1, 2, 3]))  # Outputs: False
# Fibonacci sequence
def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b

fib_gen = make_generator(fibonacci)
for _ in range(10):
    print(next(fib_gen))

# Arithmetic sequence
arith_gen = make_generator(lambda x: 2 * x)
for _ in range(10):
    print(next(arith_gen))

# Geometric sequence
geom_gen = make_generator(lambda x: 2 ** x)
for _ in range(10):
    print(next(geom_gen))
# Fibonacci sequence with memoization
fib_gen = make_generator_mem(fibonacci)
for _ in range(10):
    print(next(fib_gen))
@log(logging.INFO)
def add(x, y):
    return x + y

@log(logging.INFO)
class MyClass:
    def __init__(self, x):
        self.x = x

add(1, 2)  # Logs the call to add
mc = MyClass(1)  # Logs the instantiation of MyClass