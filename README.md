# MindFly

MindFly is a full-stack web app that was created to promote mindfulness and track the user’s mood/progress over time. The app tracks progress over time by having each user take a daily survey. MindFly analyzes the survey each survey, and if the user’s survey answers reflect they are having an off day, the app will alert the user and provide a personal activity they can do to help recenter/ ground themselves. The user’s profile page contains a mindfulness reminder that is achieved by doing API calls to populate the area with new affirmations. The profile page also contains a graph with the user’s survey answers for the week using Chart.js. On the daily survey each user fills out, there is a response box that allows them to write down any thoughts or feelings associated with the day. MindFly takes those responses to create a personal journal tab that they are able to go back to and edit. It's all about letting your mind fly!


# Table of Contents
* [Technologies Used](#technologiesused)
* [How to locally run MindFly](#run)
* [How to use MindFly](#use)


## <a name="technologiesused"></a>Technologies Used

* Python
* Flask
* PostgresSQL
* SQLAlchemy
* Javascript
* AJAX
* HTML
* CSS
* Jinja2
* Chart.js
* Bootstrap
* Affirmations API

(dependencies are listed in requirements.txt)

## <a name="run"></a>How to locally run MindFly

There and Back Again has not yet been deployed, so here is how to run the app locally on your machine.

  * Set up and activate a python virtualenv:
    * `virtualenv env`
    * `source env/bin/activate`
   * Install all ependencies:
	    * `pip3 install -r requirements.txt`
  * Run script to seed database with data:
  (this will create the database for you and add fake users)
  	* `python3 seed_database.py`
  * Start up the flask server:
    * `python server.py`
  * Go to localhost:5000 to see the web app

 ## <a name="use"></a>How to use MindFly
 ###Creating an Account
Create an account by clicking `Create An Account`. You will then be directed to take a one-time intake survey. After filling that survey, you will be directed to take the daily survey. Both of these are accomplished by doing SQLAlchemy queries to see if there is any data associated with the user. On the profile page underneath the greating, there is a mindfulness reminder that is achieved by doing API calls in an affirmations API. So everytime the user visits the homepage, they get a new affirmation. Underneath that you will see a graph implememted using chart.js. On hover over the plotted points of the graph you are able to see more details. 

###Signing in as a Test User
Click `Sign In` and use the email `user0@test.com` and the password `test`. Simulate a bad day by submitting a bad day on the daily survey. When directed to the homepage, you will notice a flashed message at the top with one of the 3 activties the user submitted in their intake survey. This is accomplished by doing a SQLAlchemy query to get the results of the survey and if it hits the criteria, the server will flash the message. Since this is an existing user, there will be more points on the graph with their data. The data is rendered by using DOM manipulation and AJAX calls. You can also go to the `Thought's Time Capsule` or `Past Surveys` tab to see more data.

## <a name="author"></a>Author
Nicole Lambert is a software engineer in Dallas, TX. Her passions include helping others and solving problems. Nicole's goal is to write code that changes the world for the better.