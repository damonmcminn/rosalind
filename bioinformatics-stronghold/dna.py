from sys import argv

dna = open(argv[1], 'r').read().splitlines()[0]

bases = {
    'A': 0,
    'C': 0,
    'G': 0,
    'T': 0
    }

for base in dna:
    bases[base] += 1

print bases['A'],bases['C'],bases['G'],bases['T']
