import unittest
from .models import movie #made our directory a python package we could import using the __init__ file
Movie = movie.Movie

class MovieTest(unittest.TestCase):
	"""
	Test class to test the behaviour of the Movie Class
	"""


	def setUp():
		"""
		Set up method that will run before every Test
		"""
		self.new_movie = Movie(1234,'Python Must Be Crazy','A thrilling new Python Series','https://developers.themoviedb.org/3/getting-started/images/khsjha27hbs',8.5,129993)

	def test_instance(self):
		self.assertTrue(isinstance(self.new_movie,Movie))


if __name__ = '__main__':
	unittest.main()


