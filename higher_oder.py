def forall(pred, iterable):
    return all(map(pred, iterable))

def exists(pred, iterable):
    return any(map(pred, iterable))

def atleast(n, pred, iterable):
    return len(list(filter(pred, iterable))) >= n

def atmost(n, pred, iterable):
    return len(list(filter(pred, iterable))) <= n