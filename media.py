# Importing the webbrowser module to open the youtube url
# class Movie creates movie object with required details
import webbrowser


class Movie:
    """ Template for creating movie object

    methods:
    show_trailer()
    """
    def __init__(self, title, story, img_url, trailer_url):
    	""" Movie constructor
        This is called when the Movie instance is created

        Args:
            title (str): Movie title
            storyline (str): Movie Storyline
            poster_image_url (str): url of image/poster
            trailer_youtube_url (str): link to youtube

        Returns:
            instance of the Movie class
        """
        self.title = title
        self.storyline = story
        self.poster_image_url = img_url
        self.trailer_youtube_url = trailer_url

    def show_trailer(self):
    	""" function show trailer

        Args:
            None
        Returns:
            None
        """
        webbrowser.open(self.trailer)

