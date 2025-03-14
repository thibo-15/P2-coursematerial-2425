def closest(points, target_point):
    return min(points, key=lambda p: ((p[0] - target_point[0]) ** 2 + (p[1] - target_point[1]) ** 2) ** 0.5)
    