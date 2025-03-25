import numpy as np
from itertools import combinations

# Define the graph as an adjacency matrix
# Cities are labeled as 0, 1, 2, ..., 6 (City 1 is 0, City 2 is 1, etc.)
graph = np.array([
    [0, 12, 10, 0, 0, 0, 12],  # City 1 (0)
    [12, 0, 8, 12, 0, 0, 0],   # City 2 (1)
    [10, 8, 0, 11, 3, 0, 9],     # City 3 (2)
    [0, 12, 11, 0, 11, 10, 0],    # City 4 (3)
    [0, 0, 3, 11, 0, 6, 7],   # City 5 (4)
    [0, 0, 0, 10, 6, 0, 9],    # City 6 (5)
    [12, 0, 9, 0, 7, 9, 0]    # City 7 (6)
])

def held_karp_tsp(graph): # 
    n = len(graph)  # Number of cities
    C = {}  # DP table to store the cost of reaching a subset of cities

    # Initialize DP table for subsets of size 1 (starting from city 0)
    for k in range(1, n):
        C[(1 << k, k)] = (graph[0][k], [0, k])

    # Iterate over all subset sizes
    for subset_size in range(2, n):
        for subset in combinations(range(1, n), subset_size):
            bits = 0
            for bit in subset:
                bits |= 1 << bit  # Represent the subset as a bitmask

            # Find the minimum cost to reach each city in the subset
            for k in subset:
                prev_bits = bits & ~(1 << k)  # Remove city k from the subset
                res = []
                for m in subset:
                    if m == k:
                        continue
                    if (prev_bits, m) in C:
                        cost, path = C[(prev_bits, m)]
                        res.append((cost + graph[m][k], path + [k]))
                if res:
                    C[(bits, k)] = min(res)

    # Find the minimum cost to complete the tour by returning to city 0
    bits = (1 << n) - 2  # All cities except city 0
    res = []
    for k in range(1, n):
        if (bits, k) in C:
            cost, path = C[(bits, k)]
            res.append((cost + graph[k][0], path + [0]))
    if res:
        min_cost, min_path = min(res)
        return min_cost, min_path
    else:
        return None

# Solve the TSP
min_cost, min_path = held_karp_tsp(graph)
print(f"Total distance: {min_cost}")
print(f"Final Route: {min_path}")