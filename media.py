import webbrowser

class Movie():
	"""This class defines a movie's characteristics and opens a trailer

	Attributes:
		title:  A string that is the movie's title
		storyline: A string that contains a summary of the movie
		poster_image_url: A string that contains the url to a wikimedia movie cover poster_image
		trailer_youtube_url:  A string that contains the youtube url to the movie's trailer
	"""
	
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		"""initializes the class Movie with certain characteristics"""
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url =trailer_youtube

	def show_trailer(self):
		"""show a trailer using the youtube url defined in __init__"""
		webbrowser.open(self.trailer_youtube_url)
