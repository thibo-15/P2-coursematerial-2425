def movie_count(movies, director):
    return sum(1 for movie in movies if movie.director == director)

def longest_movie_runtime_whit_actor(movies, actor):
    return max((movie.runtime for movie in movies if actor in movie.actors), default=0)

def has_directors_made_genre(movies, director, genre):
    return any(genre in movie.genre for movie in movies if movie.director in director)

def is_prime(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n**0.5) + 1))

def is_increasing(ns):
    return all(ns[i] <= ns[i + 1] for i in range(len(ns) - 1))

def count_matching(xs, ys):
    return sum(1 for x, y in zip(xs, ys) if x == y)

def weighted_sum(ns, weights):
    return sum(n * w for n,w in zip(ns, weights))

def alternating_caps(string):
    result = []
    upper = True  # Start alternation with uppercase letters
    
    for char in string:
        if char.isalpha():  # Check if the character is a letter
            if upper:
                result.append(char.upper())
            else:
                result.append(char.lower())
            upper = not upper  # Toggle the case for the next letter
        else:
            result.append(char)  # Keep non-alphabetic characters unchanged
    
    return ''.join(result)

import re
def find_repeated_words(sentance):
    words = re.findall(r'\b\w+\b', sentance.lower())
    return{words[i] for i in range(len(words) -1) if words[i] == words[i + 1]}

