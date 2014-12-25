from os import path

rosalind_id = path.basename(__file__).split('.').pop(0)
dataset = "../datasets/rosalind_{}.txt".format(rosalind_id)
data = open(dataset, 'r').read().splitlines()
