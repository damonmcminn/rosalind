from sys import argv

def vertexCounts(xs):
    # @xs list: edge list
    # @return dict: map of vertex counts

    firstLine = xs.pop(0)
    vertices,edges = firstLine

    counts = {}
    while vertices > 0:
        counts[vertices] = 0
        vertices -= 1
    for x in xs:
        v1,v2 = x
        counts[v1] += 1
        counts[v2] += 1
    return counts


def vertexNeighbours(xs):
    # @xs list: edge list
    # @return dict: map of list of vertex neighbours

    vertices = xs.pop(0).pop(0)
    neighbours = {}

    while vertices > 0:
        neighbours[vertices] = []
        vertices -= 1

    for pair in xs:
        v1,v2 = pair
        if v2 not in neighbours[v1]:
            neighbours[v1].append(v2)
        if v1 not in neighbours[v2]:
            neighbours[v2].append(v1)
    return neighbours

# edge list
data = open(argv[1], 'r').read().splitlines()

edgeList = [map(int, pair.split(' ')) for pair in data]
d1 = list(edgeList)
d2 = list(edgeList)

counts = vertexCounts(d1)
neighbours = vertexNeighbours(d2)

# this assumes ^ neighbours keys are sorted...
for vertex,neighbours in neighbours.iteritems():
    total = 0
    for neighbour in neighbours:
        total += counts[neighbour]
    print total,
