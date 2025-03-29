
# Return the movie titles
def titles(movies):
    return [movie.title for movie in movies]

# Return the movie titles with their year
def titles_and_years(movies):
    return [(movie.title, movie.year) for movie in movies]

# Return the movie titles with the number of actors
def titles_and_actor_counts(movies):
    return [(movie.title, len(movie.actors)) for movie in movies]

# Return the words of the sentence, reversing each word
def reverse_words(sentence):
    return ' '.join(word[::-1] for word in sentence.split())


