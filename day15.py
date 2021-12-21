import numpy as np
from collections import defaultdict


class Graph:

    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, index):
        self.nodes.add(index)

    def add_edge(self, fromNode, toNode, dist):
        self.edges[fromNode].append(toNode)
        self.distances[(fromNode, toNode)] = dist


def dijkstra(graph, initial):
    # dijkstra algorithm https://pythonwife.com/dijkstras-algorithm-in-python/
    visited = {initial: 0}
    path = defaultdict(list)

    nodes = set(graph.nodes)

    while nodes:
        minNode = None
        for node in nodes:
            if node in visited:
                if minNode is None:
                    minNode = node
                elif visited[node] < visited[minNode]:
                    minNode = node
        if minNode is None:
            break

        nodes.remove(minNode)
        currentWeight = visited[minNode]

        for edge in graph.edges[minNode]:
            weight = currentWeight + graph.distances[(minNode, edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode)

    return visited


def prepare_data(contents_split, graph):
    full_arr = []
    for line in contents_split:
        arr = [char for char in line]
        full_arr.append(arr)

    full_arr = np.array(full_arr)
    for i in range(len(full_arr) - 1):
        for j in range(len(full_arr[i]) - 1):
            graph.add_node(f"{i},{j}")
            graph.add_edge(f"{i},{j}", f"{i},{j + 1}", int(full_arr[i][j + 1]))
            graph.add_edge(f"{i},{j}", f"{i + 1},{j}", int(full_arr[i + 1][j]))

    return f"0,0", full_arr[0][0], f"{i + 1},{j + 1}", full_arr[i + 1][j + 1]


def test():
    file = open("data/day15_test.txt")
    file_contents = file.read()
    contents_split = file_contents.splitlines()
    graph = Graph()
    root, root_data, destination, destination_data = prepare_data(contents_split, graph)

    ans = puzzle(graph, root, root_data, destination, destination_data)
    assert ans == 40


def puzzle(graph, root, root_data, destination, destination_data):
    visited = dijkstra(graph, root)
    print(destination)
    i = int(destination.split(',')[0])
    j = int(destination.split(',')[1])
    min_path = min([visited[x] for x in visited if x == f"{i - 1},{j}" or x == f"{i},{j - 1}"])
    print(visited)
    # root not counted
    return int(min_path) + int(destination_data)


if __name__ == "__main__":
    test()
    file = open("data/day15.txt")
    file_contents = file.read()
    contents_split = file_contents.splitlines()
    graph = Graph()
    root, root_data, destination, destination_data = prepare_data(contents_split, graph)
    print(puzzle(graph, root, root_data, destination, destination_data))
