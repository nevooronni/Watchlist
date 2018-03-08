class Config:
	"""
	Genrela configuration parent class
	"""
	MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key{}'
	MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
  SECRET_KEY = os.environ.get('SECRET_KEY')
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://nevo:toel@localhost/watchlist'

class prodConfig(Config):
	"""
	Production configuration child class


	Args:
		Config: The parent configuration class with Genreal configuration settings
	"""
	pass

class DevConfig(Config):
	"""
	Development configuration child class

	Args:
		Config: The parent configuration class with Genreal configuration settings
	"""

	DEBUG = True #this enables debug mode in our application