#Project 1: Movie Trailer Website

The code included in this project is used to create a RESTful server and client in order to display the movies.

The server is powered by **flask** whilst the client is powered by **Angular.JS** with **bootsrap** for the modal & css styling.

#Get started

To launch the project:
    
1. **SSH** into the vagrant machine & **CD** into the project directory
2. Execute **python fresh_tomatoes.py**
3. Open your browser & navigate to **0.0.0.0:8000** (whatever the forwarded port and URL are. They should be the adjacent)

The program executes as follows:

1. Set some constants (Path to index.html and the path to the database).
2. Instantiate the Entertainment Center. Here, the database is read and the movie objects are subsequently instantiated.
3. Start the web server on port 8000 (forwarded via vagrant)
E37: No write since last change (add ! to override)
4. server your web content (Only GET requests)

#The Client

The client is a simple angular application. All of the content is contained within the index.html. The few dependencies needed (Angular, Jquery, Bootstrap, Font Awesome) are hosted on CDN's' 

###Controllers

There is one controller, **MainCtrl**, it is responsible for asynchrously accessing data from the Python server to fetch the movies first, and a second GET request, to fetch the count of the movies.

Once the raw JSON object for the movies is fetched, it is converted to an array of **Movie** objects (see Factories later) that is then sub-divided into rows of 3 for ease of the ng-repeat directive used inside the view (see Views later).

This controller is also responsible for attaching to methods to the scope, namely **showTrailer** which opens up the modal using the **modalService** and plays the youtube trailer. There is a second scope method, **showStoryline**. This function is responsible for displaying the movie storyline in a modal using the **modalService**

###Factories

There is one factory, **movieFactory**, that is responsible for constructing a movie object that holds all the attributes a movie should have.

The use of this factory allows for further expansion in terms of integrating custom methods and other attributes that the client should be able to control. However, this should be kept to a minimal and instead endpoints on the server should be created and all processing should be handled by the server. The client should remain stateless.

The factory implements one method using **prototype**. This method is a client side validation to check if the movie rating is a valid integer rating.

###Services

There is one service, **modalService**, that is responsible for handling the bootstrap modal hard coded into the view. This could have been better abstracted into a directive, however this seemed slightly unneccessary and overkill.

The service has some basic functions for showing, hiding and setting the content of the modal.

###Views

The view comprises of 2 ng-repeat directives to loop through the 2 dimensional movies array. These ng-repeats are nested in order to allow multiple rows of 3 movies. This is best explained by viewing the code.

Within the second ng-repeat is a code block that is repeated for every movie essentially and displays the title, thumbnail and has two links (one for the trailer and one for the storyline). Each link calls a scope method (showTrailer and showStoryline) that trigger the modal with the respective content. Both methods take one parameter (the youtube video ID & the storyline text respectively).

##The server

The server is a basic python application that uses a **virtual environment** to create it's own instance of python as well as **flask** (a python web micro-framework). It uses the flask CORS module to allow cross domain requests (from the client).

The server is hosted on: **http://0.0.0.0:8000**

E.G http://0.0.0.0:8000/api/v1/count or http://0.0.0.0:8000/api/v1/movies will return the json data, http://0.0.0.0:8000 will return the index file.

###Endpoints

The server has only 2 end points, **count** and **movies**. Both endpoints only take **GET** requests. Count returns the total number of movies & movies returns a list of all movies.

###Entertainment Center

####Constructor
The center reads in the movie data from a JSON file. This content is then converted into movie objects and stored in a list. This would allow further development by allowing developers to edit the **Movie** class to add extra functionality and then generate new endpoints to handle this.

####GetCount
This is a simple method that returns the number of movies in the movies array. This is used as one of the endpoints.

###toString
This is a simple method that returns the array of movies in JSON format by first converting them into dictionaries for the **json** library to handle.

###Media

####Constructor
The constructor only contains the necessary inputs to generate the movie object. It also checks that the restrictions and ratings passed in are valid. **Any invalid rating or restriction is set to "N/A"**

####valid_rating
This method takes one parameter, a rating between 0 and 5 and simply checks exactly this.

####valid_restriction
This method takes one parameter, a restriction and checks if it is within the VALID_RESTRICTIONS static variable to ensure that the inputted restriction is valid.


