from os import path

rosalind_id = path.basename(__file__).split('.').pop(0)
dataset = "../datasets/rosalind_{}.txt".format(rosalind_id)
months, litter_size = map(int, open(dataset, 'r').read().split(' '))


def totalPairs(n, k):
    pairs = {0: 0, 1: 1}
    for i in xrange(n):
        month = i + 1
        if not month in pairs:
            # Rabbits take one month to reach reproductive maturity
            pairs[month] = pairs[month-1] + (k * pairs[month-2])
    return pairs

print(months, litter_size)
print(totalPairs(months, litter_size)[months])
