from sys import argv
from time import time

dna = open(argv[1], 'r').read().splitlines().pop(0)

def toRNA(base):
    if base == 'T':
        return 'U'
    else:
        return base

start = time()
''.join(map(toRNA, dna))
mapEnd = time() - start

start = time()
dna.replace("T", "U")
replaceEnd = time() - start

print mapEnd - replaceEnd
print mapEnd
print replaceEnd
