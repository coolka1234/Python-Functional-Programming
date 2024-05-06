def acronym(words):
    return ''.join(map(lambda word: word[0].upper(), words))
def median(lst):
    n = len(lst)
    s = sorted(lst)
    return (s[n//2] if n % 2 == 1 else (s[n//2 - 1] + s[n//2]) / 2)
def pierwiastek(x, epsilon=0.1, guess=1.0):
    if abs(guess**2 - x) < epsilon:
        return guess
    else:
        return pierwiastek(x, epsilon, (guess + x / guess) / 2)
    
def make_alpha_dict(s):
    words = s.split()
    #dla posortowanego zbioru znaków z napisu s zwraca słownik w którym kluczem jest znak a wartością lista słów, w których ten znak występuje
    return {char: list(filter(lambda word: char in word, words)) for char in sorted(set(s)) if char.isalpha()}
def flatten(lst):
    for x in lst:
        if isinstance(x, (list, tuple)):
            yield from flatten(x)
        else:
            yield x