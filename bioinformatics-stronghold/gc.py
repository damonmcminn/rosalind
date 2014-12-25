from os import path

rosalind_id = path.basename(__file__).split('.').pop(0)
dataset = "../datasets/rosalind_{}.txt".format(rosalind_id)
data = open(dataset, 'r').read().split('>')
# First element of the list is an empty string
data.pop(0)

def dna(x):
    x = x.splitlines()
    dna =  {
        'id': x.pop(0),
        }
    dna_string = str().join(x)
    #dna['dna_string'] = dna_string

    gc_count = 0
    for base in dna_string:
        if base == 'G' or base == 'C':
            gc_count += 1

    dna['gc_content'] = (float(gc_count)/len(dna_string))*100
    return dna

# key=lambda x: x['gc_content']
# from operator import attrgetter
# key=attrgetter('gc_content')
highest_gc_content = sorted(map(dna, data), key=lambda x: x['gc_content']).pop(-1)

print(highest_gc_content['id'])
print(highest_gc_content['gc_content'])
