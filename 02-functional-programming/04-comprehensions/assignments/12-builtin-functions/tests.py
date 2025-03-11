import sys
sys.path.append('..')
import pytest
from movie import *
import student


def movie_count(movies, director):
    return len([movie for movie in movies if movie.director == director])


def longest_movie_runtime_with_actor(movies, actor):
    return max([movie.runtime for movie in movies if actor in movie.actors])


def has_director_made_genre(movies, director, genre):
    return any(genre in movie.genres and movie.director == director for movie in movies)


def is_prime(n):
    return all(n % k != 0 for k in range(2, n)) and n >= 2


def is_increasing(ns):
    return all(x <= y for x, y in zip(ns, ns[1:]))


def count_matching(xs, ys):
    return sum(1 for x, y in zip(xs, ys) if x == y)


def weighted_sum(ns, weights):
    return sum(n * w for n, w in zip(ns, weights))


def alternating_caps(string):
    chars = [char.upper() if index % 2 == 0 else char.lower() for index, char in enumerate(string)]
    return "".join(chars)


def find_repeated_words(sentence):
    import re
    words = [word.lower() for word in re.findall('[a-zA-Z]+', sentence)]
    return {word1 for word1, word2 in zip(words, words[1:]) if word1 == word2}

def directors():
    return {movie.director for movie in movies}

def actors():
    return {actor for movie in movies for actor in movie.actors
    }

def genres():
    return {
        genre
        for movie in movies
        for genre in movie.genres
    }


functions = {
    'movie_count': movie_count,
    'longest_movie_runtime_with_actor': longest_movie_runtime_with_actor,
    'has_director_made_genre': has_director_made_genre,
    'is_prime': is_prime,
    'is_increasing': is_increasing,
    'count_matching': count_matching,
    'weighted_sum': weighted_sum,
    'alternating_caps': alternating_caps,
    'find_repeated_words': find_repeated_words,
}

@pytest.mark.parametrize("director", directors())
def test_movie_count(director):
    function_name = 'movie_count'
    args = [movies, director]

    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name} in student module")

    solution_function = functions[function_name]
    student_function = getattr(student, function_name)

    solution_result = solution_function(*args)
    student_result = student_function(*args)

    assert student_result == solution_result


@pytest.mark.parametrize("actor", actors())
def test_longest_movie_runtime_with_actor(actor):
    function_name = 'longest_movie_runtime_with_actor'
    args = [movies, actor]

    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name} in student module")

    solution_function = functions[function_name]
    student_function = getattr(student, function_name)

    solution_result = solution_function(*args)
    student_result = student_function(*args)

    assert student_result == solution_result


@pytest.mark.parametrize("director", directors())
@pytest.mark.parametrize("genre", genres())
def test_has_director_made_genre(director, genre):
    function_name = 'has_director_made_genre'
    args = [movies, director, genre]

    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name} in student module")

    solution_function = functions[function_name]
    student_function = getattr(student, function_name)

    solution_result = solution_function(*args)
    student_result = student_function(*args)

    assert student_result == solution_result


@pytest.mark.parametrize("n", range(0, 100))
def test_is_prime(n):
    function_name = 'is_prime'
    args = [n]

    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name} in student module")

    solution_function = functions[function_name]
    student_function = getattr(student, function_name)

    solution_result = solution_function(*args)
    student_result = student_function(*args)

    assert student_result == solution_result


@pytest.mark.parametrize("n", range(0, 100))
def test_is_prime(n):
    function_name = 'is_prime'
    args = [n]

    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name} in student module")

    solution_function = functions[function_name]
    student_function = getattr(student, function_name)

    solution_result = solution_function(*args)
    student_result = student_function(*args)

    assert student_result == solution_result


@pytest.mark.parametrize("ns", [
    [],
    [1],
    [1, 2],
    [2, 1],
    [1, 1, 2, 3],
    [1, 2, 3, 3, 4, 5, 6],
    [1, 3, 6, 8, 9],
    [7, 5, 4, 3, 2, 1],
    [1, 3, 2, 4],
    [2, 1, 4, 5, 6],
    [1, 2, 4, 7, 6, 8],
    [1, 2, 3, 4, 7, 6],
])
def test_is_increasing(ns):
    function_name = 'is_increasing'
    args = [ns]

    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name} in student module")

    solution_function = functions[function_name]
    student_function = getattr(student, function_name)

    solution_result = solution_function(*args)
    student_result = student_function(*args)

    assert student_result == solution_result


@pytest.mark.parametrize("xs", [
    [],
    [1],
    ['a', 'b', 'c', 'd', 'e'],
    ['b', 'a', 'c', 'e', 'd'],
    ['a', 'x', 'c', 'x', 'e'],
])
@pytest.mark.parametrize("ys", [
    [],
    [1],
    ['a', 'b', 'c', 'd', 'e'],
    ['b', 'a', 'c', 'e', 'd'],
    ['a', 'x', 'c', 'x', 'e'],
])
def test_count_matching(xs, ys):
    function_name = 'count_matching'
    args = [xs, ys]

    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name} in student module")

    solution_function = functions[function_name]
    student_function = getattr(student, function_name)

    solution_result = solution_function(*args)
    student_result = student_function(*args)

    assert student_result == solution_result


@pytest.mark.parametrize("ns", [
    [],
    [1],
    [0, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 1, 1, 1],
    [1, 2, 3, 4],
    [4, 3, 2, 1],
])
@pytest.mark.parametrize("weights", [
    [],
    [1],
    [0, 0, 0, 0],
    [1, 0, 0, 0],
    [1, 1, 1, 1],
    [1, 2, 3, 4],
    [4, 3, 2, 1],
])
def test_weighted_sum(ns, weights):
    function_name = 'weighted_sum'
    args = [ns, weights]

    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name} in student module")

    solution_function = functions[function_name]
    student_function = getattr(student, function_name)

    solution_result = solution_function(*args)
    student_result = student_function(*args)

    assert student_result == solution_result


@pytest.mark.parametrize("string", [
    "",
    "a",
    "abc",
    "hello world",
])
def test_alternating_caps(string):
    function_name = 'alternating_caps'
    args = [string]

    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name} in student module")

    solution_function = functions[function_name]
    student_function = getattr(student, function_name)

    solution_result = solution_function(*args)
    student_result = student_function(*args)

    assert student_result == solution_result


@pytest.mark.parametrize("string", [
    "",
    "test",
    "test test",
    "this is is a test",
    "this is is a test this is also a test",
    "this is IS a test this is also a test",
    "this is  is a test this is also a test",
    "this is, is a test this is also a test",
    "abc a bc   a. a =",
    "abc a bc   a. a = a a a",
    "A a",
])
def test_find_repeated_words(string):
    function_name = 'find_repeated_words'
    args = [string]

    if not hasattr(student, function_name):
        pytest.skip(f"Missing function {function_name} in student module")

    solution_function = functions[function_name]
    student_function = getattr(student, function_name)

    solution_result = solution_function(*args)
    student_result = student_function(*args)

    assert student_result == solution_result
