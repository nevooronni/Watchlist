from flask import render_template #module takes our template and renders it
from app import app#app instance
from .request import get_movies

#views
@app.route('/movie/<int:movie_id>')#int: converts dynamic part into integer defaul is a string <> means it is dynamic response of a movie.html file
def movie(movie_id):

	"""
	view movie page function that returns the movie details page and its data
	"""
	return render_template('movie.html',id = movie_id)

def index():
	"""
	view root page function that returns the index page and its data
	"""
	popular_movies = get_movies('popular')
	print(popular_movies)
	title = 'Home - Welcome to The best Movie Review Website online'
	return render_template('index.html',title = title,popular = popular_movies)