import webbrowser
class movies :
    def __init__(self,movie_title,poster_image,trailer_youtuber):
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtuber
    def show_trailer (self):
        webbrowser.open(self.trailer)