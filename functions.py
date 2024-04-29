def acronym(words):
    return ''.join(map(lambda word: word[0].upper(), words))
def median(lst):
    n = len(lst)
    s = sorted(lst)
    return (s[n//2] if n % 2 == 1 else (s[n//2 - 1] + s[n//2]) / 2)