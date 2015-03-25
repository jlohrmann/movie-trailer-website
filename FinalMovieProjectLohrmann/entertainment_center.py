# Import fresh_tomatoes, media
# fresh_tomatoes.py will generate the necessary html to provide access to the controls for previewing the move
# media.py is the file that instantiates the Movie class file reating objects for each of the moves to be displayed
import fresh_tomatoes
import media

# Load 6 variables with Movie object
jurassicPark = media.Movie("Jurassic Park", "A Story of dinosaurs brought to life", "images.jpg", "https://www.youtube.com/watch?v=lc0UehYemQA")
spiderMan = media.Movie("Spider-Man 2", "Comic book hero Spider Man battles evil", "images5Y6ZMHGI.jpg", "https://www.youtube.com/watch?v=v8MykckiOiU")
jaws = media.Movie("JAWS", "Shark wants a snack", "imagesROZ4YHMO.jpg", "https://www.youtube.com/watch?v=ucMLFO6TsFM")
thor = media.Movie("THOR", "Super Hero Thor battles evil", "imagesBY1H89JK.jpg", "https://www.youtube.com/watch?v=JOddp-nlNvQ")
worldWarZ = media.Movie("World War Z", "Zombies Attack!", "imagesNKW9PXGN.jpg", "https://www.youtube.com/watch?v=4EC7P5WdUko")
dieHard = media.Movie("Die Hard", "Movie about a cop having a really bad day", "imagesRRST23.jpg", "https://www.youtube.com/watch?v=2TQ-pOvI6Xo")

# Load array moves with movie objects
movies = [jurassicPark, spiderMan, jaws, thor, worldWarZ, dieHard]

# Create html with movie trailers
fresh_tomatoes.open_movies_page(movies)






