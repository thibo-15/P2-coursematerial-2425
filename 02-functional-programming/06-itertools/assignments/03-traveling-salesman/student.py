from itertools import permutations

def find_shortest_path(distance, city_count):
    cities = range(1, city_count)
    shortest_path = None
    shortest_dist = float('inf')

    for perm in permutations(cities):
        tour = [0] + list(perm) + [0]

        total_dist = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) -1))

        if total_dist < shortest_dist:
            shortest_dist = total_dist
            shortest_path = tour
    return  shortest_path
