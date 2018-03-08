from app import app
import urllib.request,json #json modules to forman json response and urllib help us create a connectino to our api url 
from .models import movie

Movie = movie.Movie #movie class import here

#Getting the api key
api_key = app.config('MOVIE_API_KEY')

#Getting the movie base_url
base_url = app.config('MOVIE_API_BASE_URL')

def process_results(movie_list):
	"""
	Function that processes the movie result and transform them to a list of objects
	
	Args:
		movie_list: A list of dictionaries that contain movie details

	Returns:
		movie_results: A list of movie objects
	"""
	movie_results = []
	for movie_item in movie_list:
		id = movie_item.get('id')
		title = movie_item.get('original_tile')
		overview = movie_item.get('overview')
		poster = movie_item.get('poster_path')
		vote_average = movie_item.get('vote_average')
		vote_count = movie_item.get('vote_count')

		if poster:#some movie items might not have a poster this might give us an error
				movie_object = Movie(id,title,overview,poster,vote_average,vote_count)
				movie_results.append(movie_object)

				return movie_results

def get_movies(category):
	"""
	Function that gets the json response to our url request
	"""
	get_movies_url = base_url.format(category,api_key)#take category and append it replacing the {} in the end of the api key 

	with urllib.request.urlopen(get_movies_url) as url:#take the get_movies_url as the final as the request url
		get_movies_data = url.read()#use read function to read the json response
		get_movies_response = json.loads(get_movies_data)#convert the json to a python dictonary using json.loads()

		movie_results = None#set a variable movie_result to contain nothing

		if get_movies_response('results'):#check if the response has any results
			movie_results_list = get_movies_response['results']#creates a list of dictonary objects
			movie_results = process_results(movie_results_list)#returns a list of movie objects

			return movie_results
