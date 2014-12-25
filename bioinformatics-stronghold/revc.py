from sys import argv


dna = open(argv[1], 'r').read().splitlines().pop(0)

complements = {
    'A': 'T',
    'T': 'A',
    'C': 'G',
    'G': 'C'
    }

reverse_complement = []

for base in reversed(dna):
    reverse_complement.append(complements[base])

print ''.join(reverse_complement)
