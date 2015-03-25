#Import webbrowser library
import webbrowser

# class Movie
# Input variables:
# movie_title = (String)movie title
# movie_storyline = (String)short description of move
# poster_image = (String)file name containing poster image
# trailer_youtube = (String)URL referencing the link to the preview for the movie

class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    # function show_trailer
    # uses webbrowser library to open link to preview in a web browser
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
