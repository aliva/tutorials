# python -m unittest dijkstra.py


import math
from typing import List
from unittest import TestCase

def get_min_distance(distances: List[int], visited: List[int]):
    min_dist = math.inf

    node_id = None
    for i, distance in enumerate(distances):
        if distance <= min_dist and visited[i] is False:
            min_dist = distance
            node_id = i

    return node_id

def dijkstra(graph: List[List[int]], src: int):
    node_count = len(graph)

    distances = [math.inf] * node_count
    distances[src] = 0

    visited = [False] * node_count
    parents = [None] * node_count

    for _ in range(node_count):
        node_id = get_min_distance(distances, visited)
        visited[node_id] = True

        for j in range(node_count):
            node_id_to_j = graph[node_id][j]
            src_to_j = distances[node_id] + node_id_to_j
            if node_id_to_j > 0 and src_to_j < distances[j]:
                distances[j] = src_to_j
                parents[j] = node_id

    return distances[-1], parents




class TestDijkstras(TestCase):
    def test_first(self):
        graph = [
            [0, 6, 2, 0], # start
            [0, 0, 0, 1], # A
            [0, 3, 0, 5], # B
            [0, 0, 0, 0], # Finish
        ]
        distance, path = dijkstra(graph, 0)
        self.assertEqual(distance, 6)
        self.assertEqual(path, [None, 2, 0, 1])
