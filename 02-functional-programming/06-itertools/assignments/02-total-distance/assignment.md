## Task

Rely on the [`pairwise`](https://docs.python.org/3/library/itertools.html#itertools.pairwise) function to solve this exercise.

Say that you have a map with several cities.
To keep things simple, the cities are simply numbered: `0`, `1`, `2`, etc.

There is a road between every two cities.
You can query the distance between two cities `a` and `b` using `distance(a, b)`.

A _path_ is a sequence of cities, for example, `[0, 5, 3, 4]`.
The total distance of a path is the sum of all the lengths of the roads between the cities: `distance(0, 5) + distance(5, 3) + distance(3, 4)`.

We ask of you to write a function `total_distance(path, distance)` which computes the total distance of `path`.

* The `path` parameter is an iterator of cities.
* The `distance` parameter is a function that you can use to determine the distance between two cities.
