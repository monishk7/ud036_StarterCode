# Importing the webbrowser module to open the youtube url
# class Movie creates movie object with required details
import webbrowser


class Movie:
    # constructor for Movie object
    def __init__(self, title, story, img_url, trailer_url):
        self.title = title
        self.storyline = story
        self.poster_image_url = img_url
        self.trailer_youtube_url = trailer_url

    # method to show the trailer
    def show_trailer(self):
        webbrowser.open(self.trailer)
