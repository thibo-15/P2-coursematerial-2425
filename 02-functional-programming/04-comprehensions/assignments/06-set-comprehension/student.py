def directors(movies):
    return {movie.director for movie in movies}

def common_elements(xs, ys):
    return set(xs) & set(ys)

