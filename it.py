from itertools import imap, ifilter
from func import Function

class Itpy(object):

    # Thanks to https://github.com/jxnl/itpy for inspiration

    def __init__(self, i):
        self._iter = i

    def map(self, f):
        return Itpy(imap(f, self))

    def filter(self, f):
        return Itpy(ifilter(f, self))

    def collect(self):
        return list(self)

    def __iter__(self):
        for elem in self._iter:
            yield elem

print Itpy(range(10)).map(lambda x: x + 1).filter(lambda x: x % 2 == 0).collect()

print Itpy(range(100)).map(Function("""
result = arg0 + 2
""")).filter(Function("""
# Primes
result = True
from math import sqrt
for n in xrange(2, int(sqrt(arg0)) + 1):
    if arg0 % n == 0:
        result = False
""")).collect()

print Itpy(range(10)).map(Function("""
# Factorial
result = 1
for n in xrange(arg0, 1, -1):
    result *= n
""")).collect()