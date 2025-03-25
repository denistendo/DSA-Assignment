# Adjacency list representation of the TSP graph
adj_list = {
    "City 1": {"City 2": 12, "City 3": 10, "City 7": 12},
    "City 2": {"City 1": 12, "City 3": 8, "City 4": 12},
    "City 3": {"City 1": 10, "City 2": 8, "City 4": 11, "City 5": 3, "City 7": 12},
    "City 4": {"City 2": 12, "City 3": 11, "City 5": 11, "City 6": 10},
    "City 5": {"City 3": 3, "City 4": 11, "City 6": 6, "City 7": 9},
    "City 6": {"City 4": 10, "City 5": 6, "City 7": 9},
    "City 7": {"City 1": 12, "City 3": 12, "City 5": 9, "City 6": 9}
}

def get_distance(city1, city2):
    """Returns distance between two cities or infinity if no direct path exists"""
    return adj_list[city1].get(city2, float('inf'))