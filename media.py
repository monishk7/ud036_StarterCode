import webbrowser

class Movie:
    def __init__(self, title, story, img_url, trailer_url):
        self.title = title
        self.storyline = story
        self.poster_image_url = img_url
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
        webbrowser.open(self.trailer)
