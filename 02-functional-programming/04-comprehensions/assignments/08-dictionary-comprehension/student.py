def title_to_director(movies):
    return {movie.title: movie.director for movie in movies}

def director_to_titles(movies):
    director_dict = {}
    for movie in movies:
        if movie.director not in director_dict:
            director_dict[movie.director] = []
        director_dict[movie.director].append(movie.title)
    return director_dict