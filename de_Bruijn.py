class Edge:
    def __init__(self, f, t=None, w=1):
        self.to = t
        self.weight = w
        self.frm = f

    def __str__(self):
        return str(self.frm) + ":" + str(self.to) + ", " + str(self.weight)

    def __repr__(self):
        return str(self.frm) + ":" + str(self.to) + ", " + str(self.weight)

    def __hash__(self):
        return hash((self.frm, self.to))

    def __eq__(self, other):
        return (self.frm == other.frm) & (self.to == other.to)


class Node:
    def __init__(self, l=None, r=None, lab=None):
        self.lhs = l
        self.rhs = r
        self.label = lab

    def __str__(self):
        return "\nNode:" + str(self.label) + ", LHS:" + str(self.lhs) \
               + ", RHS:" + str(self.rhs)

    def __repr__(self):
        return "\nNode:" + str(self.label) + ", LHS:" + str(self.lhs) \
               + ", RHS:" + str(self.rhs)

    def __hash__(self):
        return hash(self.label)

    def __eq__(self, other):
        return self.label == other.label


def de_bruijn_ify(st, k):
    edges = set()
    nodes = set()
    for i in xrange(len(st) - k + 1):
        node1 = Node(st[i:i+1], st[i+k-2:i+k-1],st[i:i+k-1])
        node2 = Node(st[i+1:i+2], st[i+k-1:i+k],st[i+1:i+k])
        edge = Edge(node1.label, node2.label, 1)
        if edge not in edges:
            edges.add(edge)
        nodes.add(node1)
        nodes.add(node2)
    return nodes, edges


def build_de_bruijn(kmers):
    graph = {}
    for kmer in kmers:
        node = Node(kmer[:-1], kmer[-1:], kmer)
        edge = Edge(node.lhs, node.rhs, kmers[node.label])
        if edge in graph:
            graph[node].append(edge)
        else:
            graph[node] = [edge]
    return graph


    


print de_bruijn_ify("100010101001010101110101", 3)
print len("100010101001010101110101")
print
# print build_de_bruijn({((0, 0), (0, 0)),
#                        ((0, 0), (0, 1)),
#                        ((0, 0), (1, 0)),
#                        ((0, 0), (1, 1)),
#                        ((0, 1), (0, 0)),
#                        ((0, 1), (0, 1)),
#                        ((0, 1), (1, 0)),
#                        ((0, 1), (1, 1)),
#                        ((1, 0), (0, 0)),
#                        ((1, 0), (0, 1)),
#                        ((1, 0), (1, 0)),
#                        ((1, 0), (1, 1)),
#                        ((1, 1), (0, 0)),
#                        ((1, 1), (0, 1)),
#                        ((1, 1), (1, 0)),
#                        ((1, 1), (1, 1))})

for value in build_de_bruijn({((0, 0), (0, 0)): 0,
                              ((0, 0), (0, 1)): 1,
                              ((0, 0), (1, 0)): 1,
                              ((0, 0), (1, 1)): 0,
                              ((0, 1), (0, 0)): 1,
                              ((0, 1), (0, 1)): 0,
                              ((0, 1), (1, 0)): 0,
                              ((0, 1), (1, 1)): 0,
                              ((1, 0), (0, 0)): 1,
                              ((1, 0), (0, 1)): 0,
                              ((1, 0), (1, 0)): 0,
                              ((1, 0), (1, 1)): 0,
                              ((1, 1), (0, 0)): 0,
                              ((1, 1), (0, 1)): 0,
                              ((1, 1), (1, 0)): 0,
                              ((1, 1), (1, 1)): 0}).itervalues():
    print value
