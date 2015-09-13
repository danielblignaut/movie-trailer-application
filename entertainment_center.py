import json;
import media;

class Entertainment_Center() :
	""" This class provides a way to manage all stored movie instances """
	

	'''this function is responsible for reading in the data source. It takes the absolute file path as a json_string
	and returns a list of movie objects. '''
	def __init__(self, file_name) :
		data_file = open(file_name);
		data = json.load(data_file);
		self.Movies = [];

		for movie_raw in data["movies"] :
			temp = media.Movie(movie_raw["title"], movie_raw["storyline"], 
				movie_raw["image_poster"], movie_raw["youtube_trailer"], movie_raw["rating"], movie_raw["restriction"]);
			self.Movies.append(temp);

	'''this function returns the count of all of the movies in the movies array'''
	def getCount(self) :
		return len(self.Movies);

	'''a simple utility function to help convert the list of movie objects into dictionaries
	so that the json.dumps function can handle it. It taks in an object and returns a dictionary'''
	def obj_dict(self, obj):
	    return obj.__dict__;

	'''the toString function is responsible for converting the array of movies into a JSON string and returning it'''
	def toString(self) :
		return json.dumps(self.Movies, default=self.obj_dict);