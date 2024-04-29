from functions import *
from higher_oder import *
print(acronym(["Zakład", "Ubezpieczeń", "Społecznych"]))  # Outputs: ZUS
print(median([1,1,19,2,3,4,4,5,1]))  # Outputs: 3
print(pierwiastek(3, epsilon = 0.1))  # Outputs: 1.7321428571428572
print(make_alpha_dict("on i ona"))  
# Outputs: {'a': ['ona'], 'i': ['i'], 'n': ['on', 'ona'], 'o': ['on', 'ona']}
print(list(flatten([1, [2, 3], [[4, 5], 6]])))  # Outputs: [1, 2, 3, 4, 5, 6]