"""
Escape Pods
===========

You've blown up the LAMBCHOP doomsday device and broken the bunnies out of Lambda's prison - and now you need to escape from the space station as quickly and as orderly as possible! The bunnies have all gathered in various locations throughout the station, and need to make their way towards the seemingly endless amount of escape pods positioned in other parts of the station. You need to get the numerous bunnies through the various rooms to the escape pods. Unfortunately, the corridors between the rooms can only fit so many bunnies at a time. What's more, many of the corridors were resized to accommodate the LAMBCHOP, so they vary in how many bunnies can move through them at a time.

Given the starting room numbers of the groups of bunnies, the room numbers of the escape pods, and how many bunnies can fit through at a time in each direction of every corridor in between, figure out how many bunnies can safely make it to the escape pods at a time at peak.

Write a function answer(entrances, exits, path) that takes an array of integers denoting where the groups of gathered bunnies are, an array of integers denoting where the escape pods are located, and an array of an array of integers of the corridors, returning the total number of bunnies that can get through at each time step as an int. The entrances and exits are disjoint and thus will never overlap. The path element path[A][B] = C describes that the corridor going from A to B can fit C bunnies at each time step.  There are at most 50 rooms connected by the corridors and at most 2000000 bunnies that will fit at a time.

For example, if you have:
entrances = [0, 1]
exits = [4, 5]
path = [
  [0, 0, 4, 6, 0, 0],  # Room 0: Bunnies
  [0, 0, 5, 2, 0, 0],  # Room 1: Bunnies
  [0, 0, 0, 0, 4, 4],  # Room 2: Intermediate room
  [0, 0, 0, 0, 6, 6],  # Room 3: Intermediate room
  [0, 0, 0, 0, 0, 0],  # Room 4: Escape pods
  [0, 0, 0, 0, 0, 0],  # Room 5: Escape pods
]

Then in each time step, the following might happen:
0 sends 4/4 bunnies to 2 and 6/6 bunnies to 3
1 sends 4/5 bunnies to 2 and 2/2 bunnies to 3
2 sends 4/4 bunnies to 4 and 4/4 bunnies to 5
3 sends 4/6 bunnies to 4 and 4/6 bunnies to 5

So, in total, 16 bunnies could make it to the escape pods at 4 and 5 at each time step.  (Note that in this example, room 3 could have sent any variation of 8 bunnies to 4 and 5, such as 2/6 and 6/6, but the final answer remains the same.)

Languages
=========

To provide a Python solution, edit solution.py
To provide a Java solution, edit solution.java

Test cases
==========

Inputs:
    (int list) entrances = [0]
    (int list) exits = [3]
    (int) path = [[0, 7, 0, 0], [0, 0, 6, 0], [0, 0, 0, 8], [9, 0, 0, 0]]
Output:
    (int) 6

Inputs:
    (int list) entrances = [0, 1]
    (int list) exits = [4, 5]
    (int) path = [[0, 0, 4, 6, 0, 0], [0, 0, 5, 2, 0, 0], [0, 0, 0, 0, 4, 4], [0, 0, 0, 0, 6, 6], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
Output:
(int) 16
"""
import unittest


class TestEscapePods(unittest.TestCase):
    def test_1(self):
        entrances = [0]
        exits = [3]
        path = [[0, 7, 0, 0],
                [0, 0, 6, 0],
                [0, 0, 0, 8],
                [9, 0, 0, 0]]
        self.assertEqual(answer(entrances, exits, path), 6)

    def test_2(self):
        entrances = [0, 1]
        exits = [4, 5]
        path = [[0, 0, 4, 6, 0, 0],
                [0, 0, 5, 2, 0, 0],
                [0, 0, 0, 0, 4, 4],
                [0, 0, 0, 0, 6, 6],
                [0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0]]
        self.assertEqual(answer(entrances, exits, path), 16)


# This class represents a directed graph using adjacency matrix representation
class Graph:
    def __init__(self, graph):
        self.graph = graph  # residual graph
        self.ROW = len(graph)
        # self.COL = len(gr[0])

    '''Returns true if there is a path from source 's' to sink 't' in
    residual graph. Also fills parent[] to store the path '''

    def bfs(self, s, t, parent):

        # Mark all the vertices as not visited
        visited = [False] * (self.ROW)

        # Create a queue for BFS
        queue = []

        # Mark the source node as visited and enqueue it
        queue.append(s)
        visited[s] = True

        # Standard BFS Loop
        while queue:

            # Dequeue a vertex from queue and print it
            u = queue.pop(0)

            # Get all adjacent vertices's of the dequeued vertex u
            # If a adjacent has not been visited, then mark it
            # visited and enqueue it
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u

        # If we reached sink in BFS starting from source, then return
        # true, else false
        return True if visited[t] else False

    # Returns the maximum flow from s to t in the given graph
    def fordfulkerson(self, source, sink):

        # This array is filled by BFS and to store path
        parent = [-1] * self.ROW

        max_flow = 0  # There is no flow initially

        # Augment the flow while there is path from source to sink
        while self.bfs(source, sink, parent):

            # Find minimum residual capacity of the edges along the
            # path filled by BFS. Or we can say find the maximum flow
            # through the path found.
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            # Add path flow to overall flow
            max_flow += path_flow

            # update residual capacities of the edges and reverse edges
            # along the path
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]
        return max_flow


def answer(entrances, exits, path):
    graph = Graph(path)
    flow_tot = 0
    for entrance in entrances:
        for exit in exits:
            flow_tot += graph.fordfulkerson(entrance, exit)
    return flow_tot


if __name__ == '__main__':
    unittest.main()
