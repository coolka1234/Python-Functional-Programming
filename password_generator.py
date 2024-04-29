import random
import string

class PasswordGenerator:
    def __init__(self, length, count, charset=string.ascii_letters + string.digits):
        self.length = length
        self.count = count
        self.charset = charset
        self.generated = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.generated >= self.count:
            raise StopIteration
        self.generated += 1
        return ''.join(random.choice(self.charset) for _ in range(self.length))