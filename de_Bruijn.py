def de_bruijn_ify(st, k):
    edges = {}
    nodes = set()
    for i in xrange(len(st) - k + 1):
        if st[i:i+k-1]+st[i+2:i+k] in edges:
            edges[st[i:i+k-1]+st[i+2:i+k]] += 1
        else:
            edges[st[i:i+k-1]+st[i+2:i+k]] = 1
        nodes.add(st[i:i+k-1])
        nodes.add(st[i+1:i+k])
    return nodes, edges

def build_de_bruijn(kmers):
    nodes = set()
    edges = {}


print de_bruijn_ify("100010101001010101110101", 3)
print len("100010101001010101110101")