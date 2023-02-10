import spacy

# Load language model, English, size: medium
nlp = spacy.load('en_core_web_md')

planet_hulk_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a "\
"shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is "\
"sold into slavery and trained as a gladiator."

planet_hulk_description_tokenised = nlp(planet_hulk_description)

# Initialise list with place-holder values
most_similar_movie = ["Movie X", "Description X", 0]

# Iterate through movies in text file, comparing their descriptions to that of Planet Hulk using SpaCy. If similarity is greater than the 
# place-holder and any previously compared movies, clear list and replace with values relating to that more similar movie
with open('movies.txt', 'r') as f:
    for line in f:
        line_split = line.split(':')
        movie_identifier = line_split[0].strip()
        movie_description = line_split[1]
        movie_description_tokenised = nlp(movie_description)
        similarity = movie_description_tokenised.similarity(planet_hulk_description_tokenised)
        if similarity > most_similar_movie[2]:
            most_similar_movie.clear()
            most_similar_movie.extend((movie_identifier, movie_description, similarity))  # https://stackoverflow.com/questions/20196159/how-to-append-multiple-values-to-a-list-in-python, accessed 10/2/2023 at 13:10

print(f"The most similar movie to Planet Hulk is {most_similar_movie[0]}, with a similarity score of {most_similar_movie[2]}\n")
print(f"Planet Hulk: {planet_hulk_description}\n")
print(f"{most_similar_movie[0]}: {most_similar_movie[1]}")