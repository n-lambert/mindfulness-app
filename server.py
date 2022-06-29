"""Server for daily mantras app."""

from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db, db
import crud
import datetime
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
    name = request.form.get("name")
    password = request.form.get("password")
    email = request.form.get("email")
    

    user = crud.get_user_by_email(email)
    if user:
        flash("An account with that email already exists. Try again.")
        return redirect("/create-account")
    else:
        user = crud.create_user(name, email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account successfully created! Please log in.")
        return redirect('/log-in')

@app.route("/log-in")
def show_create_log_in_page():
    """Get request for create account page"""

    return render_template ("log_in.html")

@app.route("/log-in", methods=["POST"])
def login_user():

    user_email = request.form.get("email")
    user_password = request.form.get("password")
    
    existing_user = crud.get_user_by_email(user_email)

    if existing_user and user_password == existing_user.password:
        session["user_email"] = existing_user.email
        session.modified = True
        user_id = existing_user.user_id
        activities = crud.get_all_activities_by_user_id(user_id)
        date = datetime.date.today()
        survey_answers = crud.get_survey_answers_by_user_id_and_date(user_id, date=date)
       
        flash('Logged in!')
        if len(activities) == 0:
            return redirect('/intake-survey')
        elif len(survey_answers) == 0:
            return redirect('/survey')
        else:
            return redirect('/profile-page')
    else:
        flash('Incorrect password!')
        return redirect('/log-in')

@app.route("/welcome-page")
def show_welcome_page():
    """Shows welcome page."""
    #check for entry in db, write if statement in jinja 
    affirmation_quotes = requests.get('https://www.affirmations.dev/').json()
    session_user = crud.get_user_by_email(session['user_email'])
    return render_template('welcome_page.html', session_user=session_user, affirmation_quotes=affirmation_quotes)
    
@app.route("/intake-survey")
def show_intake_survey():
    """Show intake survey."""

    date = datetime.date.today()
    return render_template("intake_survey.html", date=date)

@app.route("/intake-survey", methods=["POST"])
def take_intake_survey():
    """Capture intake survey answers"""

    date = datetime.date.today()
    activity_idea_1 = request.form.get("activity_1")
    activity_idea_2 = request.form.get("activity_2")
    activity_idea_3 = request.form.get("activity_3")
    session_user = crud.get_user_by_email(session['user_email'])
    user_id = session_user.user_id
    activity_1 = crud.create_activity(user_id, activity_idea_1)
    activity_2 = crud.create_activity(user_id, activity_idea_2)
    activity_3 = crud.create_activity(user_id, activity_idea_3)
    db.session.add(activity_1)
    db.session.add(activity_2)
    db.session.add(activity_3)
    db.session.commit()

    flash('Survey Submitted!')

    survey_answers = crud.get_all_survey_answers_by_user_id(user_id)
    if len(survey_answers) == 0:
        return redirect('/survey')
    
    return redirect("/profile-page")

@app.route("/survey")
def show_survey_form():
    """Show daily survey."""

    date = datetime.date.today()
    return render_template('survey.html', date=date)

@app.route("/survey", methods=["POST"])
def take_survey():
    """Capture survey answers"""

    date = datetime.date.today()
    q1 = request.form.get("q1_survey-answer")
    q2 = request.form.get("q2_survey-answer")
    q3 = request.form.get("q3_survey-answer")
    q4 = request.form.get("q4_survey-answer")
    q5 = request.form.get("q5_survey-answer")
    response = request.form.get("journal_prompt")
    session_user = crud.get_user_by_email(session['user_email'])
    user_id = session_user.user_id
    new_answer = crud.create_survey_answer(user_id=user_id, date=date, q1=q1, q2=q2, q3=q3, q4=q4, q5=q5)
    new_thought = crud.create_journal_response(user_id=user_id, date=date, response=response)
    db.session.add(new_thought)
    db.session.add(new_answer)
    db.session.commit()

    flash('Survey Submitted!')
    
    return redirect("/profile-page")

@app.route("/profile-page")
def show_profile_page():
    """Display User homepage."""
    user_email = session['user_email']
    session_user = crud.get_user_by_email(user_email)
    user_name = session_user.name
    affirmation_quotes = requests.get('https://www.affirmations.dev/').json()

    return render_template("profile_page.html", session_user=session_user, affirmation_quotes=affirmation_quotes)

@app.route ("/past-surveys")
def show_all_users_past_surveys():
    """Display past surveys in a list by user."""
    user_email = session['user_email']
    session_user = crud.get_user_by_email(user_email)
    user_name = session_user.name
    user_id = session_user.user_id
    user_survey_answers = crud.get_all_survey_answers_by_user_id(user_id)
    print(user_survey_answers)
    
    return render_template("past_surveys.html", user_survey_answers=user_survey_answers, session_user=session_user)

@app.route('/survey-details/<survey_answer_id>')
def show_user_survey_answers(survey_answer_id):
    """Get survey answers."""

    user_email = session['user_email']
    session_user = crud.get_user_by_email(user_email)
    user_name = session_user.name
    user_id = session_user.user_id
    user_survey_answer = crud.get_survey_answer_by_survey_answer_id(survey_answer_id)
    journal_response = crud.get_journal_entry_by_user_id_and_date(user_id, user_survey_answer.date)
    
    return render_template("survey_details.html", journal_response=journal_response, survey_answer_id=survey_answer_id, session_user=session_user, user_survey_answer=user_survey_answer)

@app.route('/journal')
def show_user_journal_prompts():
    """Get survey answers."""

    user_email = session['user_email']
    session_user = crud.get_user_by_email(user_email)
    user_name = session_user.name
    user_id = session_user.user_id
    journal_responses = crud.get_all_journal_entries_by_user_id(user_id)
    
    return render_template("thoughts.html", journal_responses=journal_responses, session_user=session_user, user_name=user_name)

@app.route("/journal", methods=["POST"])
def update_journal_entries():
    """Update a past journal entry."""

    user_email = session['user_email']
    session_user = crud.get_user_by_email(user_email)
    user_name = session_user.name
    user_id = session_user.user_id

    journal_id = request.json.get("journal_id")
    edits = request.json.get("edits")

    journal_responses = crud.get_journal_entry_by_id(journal_id)
    journal_responses.response = edits
    db.session.commit()

    return ""

   
if __name__ == "__main__":
    # DebugToolbarExtension(app)
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)