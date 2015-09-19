class Movie() :
    """ This class provides a way to store movie related data """
    
    VALID_RESTRICTIONS = ["G", "PG", "PG-13", "R"]
    
    def __init__(self, title, storyline, image_poster, youtube_trailer, rating, restriction) :
        self.title = title
        self.storyline = storyline
        self.image_poster = image_poster
        self.youtube_trailer = youtube_trailer

        if(Movie.check_rating(rating)) :
        	self.rating = rating
        else :
        	self.rating = "N/A"

        if(Movie.check_restriction(restriction)) :
        	self.restriction = restriction.upper()
        else :
        	self.restriction = "N/A"

   	'''this static method provides a way to check if the movies's age restriction is valid '''
    @staticmethod
    def check_restriction(restriction) :
    	for static_restriction in Movie.VALID_RESTRICTIONS :
            if(static_restriction == restriction.upper()) :
                return True

    	return False

    '''this static method provides a way to check if the movies's rating is valid '''
    @staticmethod
    def check_rating(rating) :
   		if(rating >= 0 and rating <= 5) :
   			return True

   		return False
