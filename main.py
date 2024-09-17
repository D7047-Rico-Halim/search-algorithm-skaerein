from graphs import bfs, dfs, ucs, greedy_bfs, a_star

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('C', 2), ('D', 5)],
    'C': [('D', 1), ('E', 5)],
    'D': [('F', 2)],
    'E': [('F', 1)],
    'F': [('G', 3)],
    'G': []
}

heuristics = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 3,
    'E': 2,
    'F': 1,
    'G': 0
}
