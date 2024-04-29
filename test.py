from functions import *
from higher_oder import *
from password_generator import *
from generator_maker import *
from decorator import *
print(acronym(["Zakład", "Ubezpieczeń", "Społecznych"]))  
print(median([1,1,19,2,3,4,4,5,1]))  
print(pierwiastek(3, epsilon = 0.1))  
print(make_alpha_dict("on i ona"))  
print(list(flatten([1, [2, 3], [[4, 5], 6]])))  
print(forall(lambda x: x > 0, [1, 2, 3]))  
print(exists(lambda x: x > 0, [-1, -2, 3]))  
print(atleast(2, lambda x: x > 0, [-1, 2, 3]))  
print(atmost(2, lambda x: x > 0, [1, 2, 3]))  
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
 
arith_gen = make_generator(lambda x: 2 * x)
for _ in range(10):
    print(next(arith_gen))

geom_gen = make_generator(lambda x: 2 ** x)
for _ in range(10):
    print(next(geom_gen))
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

add(1, 2)  
mc = MyClass(1) 