#!movie_server/bin/python
from flask import Flask;
from flask import send_from_directory
import webbrowser;
import entertainment_center;
import os;


'''the PATH global variabbles are used to help locate the data source file & 
    the client angular app'''
DATABASE = os.path.dirname(os.path.realpath(__file__)) + "/datasource.json"
CLIENT = os.path.dirname(os.path.realpath(__file__)) + "/static/"

''' Initiate Flask & fetch the list of movies. Also ensure that the server 
    allows cross origin domain requests so that
    our client can get JSON data from the server (it\'s hosted on a seperate
    server. '''

app = Flask(__name__, static_url_path=CLIENT)
Center = entertainment_center.Entertainment_Center(DATABASE)

'''route a GET request through the API to return the number of movies in the 
    list '''

@app.route('/api/v1/movies', methods=['GET'])
def get_movies():
    return "{ \"movies\": " + Center.toString() + "}";

'''route a GET request through the API to return the number of movies in the 
    list '''

@app.route('/api/v1/count', methods=['GET'])
def get_count() :
    return "{\"count\": \"" + str(Center.getCount()) +"\"}"

'''open the output file in the browser (in a new tab, if possible)
the index.html file is responsible for querying the above end points and 
fetching the python data strucutres to populate the website'''

@app.route('/', methods=['GET'])
def index():
    return send_from_directory(CLIENT, 'index.html')

if __name__ == '__main__':
	app.run(debug=True, use_reloader=True, host='0.0.0.0', port=8000)
    

    