import fresh_tomatoes
import webbrowser

class Movie():
	def __init__(self, movie_title, movie_genre, poster_image_url, trailer_youtube_url):
		self.title = movie_title
		self.movie_genre = movie_genre
		self.poster_image_url = poster_image_url
		self.trailer_youtube_url = trailer_youtube_url

	def show_trailer(self):
		webbrowser.open(self.trailer_youtube)


inside_out = Movie("Inside Out", "Animation", "http://screenrant.com/wp-content/uploads/inside-out-poster.jpg", "https://www.youtube.com/watch?v=seMwpP0yeu4")
interstellar = Movie("Interstellar", "Sci-Fi", "http://www.hollywoodreporter.com/sites/default/files/custom/Blog_Images/interstellar3.jpg", "https://www.youtube.com/watch?v=2LqzF5WauAw")
gone_girl = Movie("Gone Girl","Drama", "http://ia.media-imdb.com/images/M/MV5BMTk0MDQ3MzAzOV5BMl5BanBnXkFtZTgwNzU1NzE3MjE@._V1_SX640_SY720_.jpg", "https://www.youtube.com/watch?v=Ym3LB0lOJ0o")
dallas_Buyers_Club = Movie("Dallas Buyers Club", "Biography", "http://cdn.collider.com/wp-content/uploads/dallas-buyers-club-poster1.jpg", "https://www.youtube.com/watch?v=KDvPcBeOn8E")
big_Hero_6 = Movie("Big Hero 6", "Animation", "http://cdn.collider.com/wp-content/uploads/big-hero-6-poster-baymax-hi-res.jpg", "https://www.youtube.com/watch?v=z3biFxZIJOQ")
nightcrawler = Movie("Nightcrawler", "Thriller", "http://cdn.collider.com/wp-content/uploads/nightcrawler-poster-final.jpg", "https://www.youtube.com/watch?v=u1uP_8VJkDQ")

movies = [inside_out, interstellar, gone_girl, dallas_Buyers_Club, big_Hero_6, nightcrawler]

fresh_tomatoes.open_movies_page(movies)