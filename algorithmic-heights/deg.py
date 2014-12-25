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


# edge list
data = open(argv[1], 'r').read().splitlines()



edgeList = [map(int, pair.split(' ')) for pair in data]

counts = vertexCounts(edgeList)

degrees = []
vertices = len(counts)
i = 1
while i <= vertices:
    print counts[i],
    i += 1
