"""Server for daily mantras app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect, jsonify)
from model import connect_to_db, db
from random import choice, randint
import crud
from datetime import datetime, timedelta
import requests

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev"
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """View homepage."""

    #if logged in- go to welcome page using redirect

    return render_template('homepage.html')

@app.route("/create-account")
def show_create_account_page():
    """Get request for create account page"""

    return render_template ("create_account.html")

@app.route("/create-account", methods=["POST"])
def create_user():
    """Create a new user."""    

    # gets information from the form and assigns it to a variable
    name = request.form.get("name")
    password = request.form.get("password")
    email = request.form.get("email")

    # gets user by email determine if there is an account with that email
    user = crud.get_user_by_email(email)        
    if user:
        flash("An account with that email already exists. Try again.")
        return redirect("/create-account")

    else:
        # creates new user
        user = crud.create_user(name, email, password)

        # adds user to be committed
        db.session.add(user)

        # commits user to database
        db.session.commit()

        flash("Account successfully created! Please log in.")

        return redirect('/log-in')

@app.route("/log-in")
def show_create_log_in_page():
    """Get request for create account page."""

    return render_template ("log_in.html")

@app.route("/log-in", methods=["POST"])
def login_user():

    user_email = request.form.get("email")      
    user_password = request.form.get("password")
    
    existing_user = crud.get_user_by_email(user_email)

    if existing_user and user_password == existing_user.password:
        # gets user info from flask session
        session["user_email"] = existing_user.email
        session.modified = True
        
        user_id = existing_user.user_id
        date = datetime.now().date()

        # returns list object from database
        activities = crud.get_all_activities_by_user_id(user_id)
        survey_answers = crud.get_survey_answers_by_user_id_and_date(user_id, date=date)
       
        flash('Logged in!')

        #nested if statement for signed in user
        # if no activties are returned this forces the user to take the intake survey only once
        if len(activities) == 0:
            return redirect('/intake-survey')
            
        # checks to see if the survey was filled out for the current day
        elif not survey_answers:
            return redirect('/survey')

        # if the user has taken the intake survey and daily survey, go to profile page
        else:
            return redirect('/profile-page')

    # wrong password path
    else:
        flash('Incorrect password!')
        return redirect('/log-in')

@app.route("/welcome-page")
def show_welcome_page():
    """Shows welcome page."""
    
    # calls API everytime page is loaded for a new mindfulness reminder
    affirmation_quotes = requests.get('https://www.affirmations.dev/').json()

    #defines session user to pass through Jinja
    session_user = crud.get_user_by_email(session['user_email'])

    return render_template('welcome_page.html', session_user=session_user, affirmation_quotes=affirmation_quotes)
    
@app.route("/intake-survey")
def show_intake_survey():
    """Show intake survey."""

    # this ensures that each survey has the correct date stamp of the day it was taken
    date = datetime.now().date()

    return render_template("intake_survey.html", date=date)

@app.route("/intake-survey", methods=["POST"])
def take_intake_survey():
    """Capture intake survey answers"""

    date = datetime.now().date()

    # pulls the input for each activity
    activity_idea_1 = request.form.get("activity_1")
    activity_idea_2 = request.form.get("activity_2")
    activity_idea_3 = request.form.get("activity_3")

    # gets the user id from the session
    session_user = crud.get_user_by_email(session['user_email'])
    user_id = session_user.user_id

    #creates new activities
    activity_1 = crud.create_activity(user_id, activity_idea_1)
    activity_2 = crud.create_activity(user_id, activity_idea_2)
    activity_3 = crud.create_activity(user_id, activity_idea_3)

    # adds each activity individually to avoid adding as a list
    db.session.add(activity_1)
    db.session.add(activity_2)
    db.session.add(activity_3)

    # commits all activities
    db.session.commit()

    flash('Survey Submitted!')

    # checks to see if user has taken daily survey
    survey_answers = crud.get_all_survey_answers_by_user_id(user_id)

    # brings user to daily survey
    if not survey_answers:
        return redirect('/survey')
    
    # if survey has already been taken then they go to profile page
    return redirect("/profile-page")

@app.route("/survey")
def show_survey_form():
    """Show daily survey."""

    date = datetime.now().date()
    return render_template('survey.html', date=date)

@app.route("/survey", methods=["POST"])
def take_survey():
    """Capture survey answers"""

    date = datetime.now().date()

    # pulls input from each survey answer
    q1 = int(request.form.get("q1_survey-answer"))
    q2 = int(request.form.get("q2_survey-answer"))
    q3 = int(request.form.get("q3_survey-answer"))
    q4 = int(request.form.get("q4_survey-answer"))
    q5 = int(request.form.get("q5_survey-answer"))

    # pulls input from the journal response 
    response = request.form.get("journal_prompt")

    # gets the user id from the session
    session_user = crud.get_user_by_email(session['user_email'])
    user_id = session_user.user_id

    # creates new survey answers and journal response
    new_answer = crud.create_survey_answer(user_id=user_id, date=date, q1=q1, q2=q2, q3=q3, q4=q4, q5=q5)
    new_thought = crud.create_journal_response(user_id=user_id, date=date, response=response)

    # data is added to the session
    db.session.add(new_thought)
    db.session.add(new_answer)

    # commits data to the database
    db.session.commit()

    flash('Survey Submitted!')

    # gets activities and puts all value from the form in a list
    activities = crud.get_all_activities_by_user_id(user_id)
    questions = [q1, q2, q3, q4, q5]

    # adds up core for the day and if sum < 10, flash one of their mindfulness activities
    if sum(questions) <= 10:
        flash(f'Try one of these activities to promote mindfulness: {choice(activities).activity_idea}')
        return redirect("/profile-page")
    
    return redirect("/profile-page")

@app.route("/profile-page")
def show_profile_page():
    """Display User homepage."""

    # gets user info from the flask session
    user_email = session['user_email']
    session_user = crud.get_user_by_email(user_email)
    user_name = session_user.name

    # calls API everytime page is loaded for a new mindfulness reminder
    affirmation_quotes = requests.get('https://www.affirmations.dev/').json()

    return render_template("profile_page.html", session_user=session_user,
                            affirmation_quotes=affirmation_quotes)

@app.route ("/past-surveys")
def show_all_users_past_surveys():
    """Display past surveys in a list by user."""

    # gets user info from the flask session
    user_email = session['user_email']
    session_user = crud.get_user_by_email(user_email)
    user_name = session_user.name
    user_id = session_user.user_id

    # gets all survey answers associated with the user
    user_survey_answers = crud.get_all_survey_answers_by_user_id(user_id)
    
    return render_template("past_surveys.html", user_survey_answers=user_survey_answers, session_user=session_user)

@app.route('/survey-details/<survey_answer_id>')
def show_user_survey_answers(survey_answer_id):
    """Get survey answers."""

    # gets user info from the flask session
    user_email = session['user_email']
    session_user = crud.get_user_by_email(user_email)
    user_name = session_user.name
    user_id = session_user.user_id

    # pulls survey answers from the day 
    user_survey_answer = crud.get_survey_answer_by_survey_answer_id(survey_answer_id)
    journal_response = crud.get_journal_entry_by_user_id_and_date(user_id, user_survey_answer.date)
    
    return render_template("survey_details.html", journal_response=journal_response, 
                            survey_answer_id=survey_answer_id, session_user=session_user, 
                            user_survey_answer=user_survey_answer)

@app.route('/journal')
def show_user_journal_prompts():
    """Get survey answers."""

    # pulls user info from flask session
    user_email = session['user_email']
    session_user = crud.get_user_by_email(user_email)
    user_name = session_user.name
    user_id = session_user.user_id

    # queries for all journal responses associated with the session user
    journal_responses = crud.get_all_journal_entries_by_user_id(user_id)
    
    return render_template("thoughts.html", journal_responses=journal_responses, 
                            session_user=session_user, user_name=user_name)

@app.route("/journal", methods=["POST"])
def update_journal_entries():
    """Update a past journal entry."""

    # pulls user info from flask session
    user_email = session['user_email']
    session_user = crud.get_user_by_email(user_email)
    user_name = session_user.name
    user_id = session_user.user_id

    # gets data from the json
    journal_id = request.json.get("journal_id")
    edits = request.json.get("edits")

    # gets journal response by id
    journal_responses = crud.get_journal_entry_by_id(journal_id)

    # after the edits and journal id are captured, reassign value of response with the new edits
    journal_responses.response = edits

    # commits the new changes to the database
    db.session.commit()

    return ""

@app.route('/survey_answers_this_week.json')
def get_survey_answers_for_chart():
    """Get survey data as JSON."""

    user_email = session['user_email']
    session_user = crud.get_user_by_email(user_email)
    user_id = session_user.user_id

    answers_this_week = []
    date = datetime.now().date() 
    for _ in range(7):
        survey_answer_by_user = crud.get_survey_answers_by_user_id_and_date(user_id=user_id, date=date)
        if not survey_answer_by_user:
            continue
        print(user_id)
        print(date)
        answers_this_week.append({'date': date.isoformat(), 
                                'q1_answer': survey_answer_by_user.q1, 
                                'q2_answer': survey_answer_by_user.q2,
                                'q3_answer': survey_answer_by_user.q3,
                                'q4_answer': survey_answer_by_user.q4,
                                'q5_answer': survey_answer_by_user.q5})
        date = date - timedelta(days=1)


    return jsonify({'data': answers_this_week})

@app.route('/recenter')
def show_mindfulness_activtiy():
    """Show a random activity from any user."""

    all_activities = crud.get_all_activities()
    rand_activity = choice(all_activities)

    return render_template("recenter.html", rand_activity=rand_activity)

@app.route('/get-recenter')
def get_new_random_activity():
    """Get new random activity."""

    all_activities = crud.get_all_activities()
    rand_activity = choice(all_activities)

    return rand_activity.activity_idea


   
if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)