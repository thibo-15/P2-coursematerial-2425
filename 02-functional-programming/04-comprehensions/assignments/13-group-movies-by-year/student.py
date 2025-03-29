def group_movies_by_year(movies):
    movies_dict = {}
    for movie in movies:
        if movie.year not in movies_dict:
            movies_dict[movie.year] = []
        movies_dict[movie.year].append(movie.title)
    return movies_dict