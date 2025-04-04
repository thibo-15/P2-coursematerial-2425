def genres(movies):
    return {genre for movie in movies for genre in movie.genres}

def actors(movies):
    return {actor for movie in movies for actor in movie.actors}

def repeat_consecutive(xs, n):
     return [x for x in xs for _ in range(n)]

def repeat_alternating(xs, n):
    lst = []
    for _ in range(n):
        for x in xs:
            lst.append(x)
    return lst

from util import Card

def cards(values, suits):
    return {Card(value, suit) for value in values for suit in suits}

