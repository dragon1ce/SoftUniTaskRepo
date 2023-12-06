def movie_organizer(*args):
    work = dict(args)
    genre = dict()
    for k, v in work.items():
        if v not in genre:
            genre[v] = []
        genre[v].append(k)
    sorted_genre = dict(sorted(genre.items(), key=lambda x: (-len(x[1]), x[0])))
    formatted_output = []
    for k, v in sorted_genre.items():
        formatted_output.append(f"{k} - {len(v)}\n")
        for name in sorted(v):
            formatted_output.append(f"* {name}\n")
    return "".join(formatted_output)

print(movie_organizer(
    ("The Matrix", "Sci-fi")))
print()
print(movie_organizer(
    ("The Godfather", "Drama"),
    ("The Hangover", "Comedy"),
    ("The Shawshank Redemption", "Drama"),
    ("The Pursuit of Happiness", "Drama"),
    ("The Hangover Part II", "Comedy")))
print()

print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
print()
