"""CRUD operations."""
from model import db, User, SurveyAnswer, JournalPrompt, Activity, connect_to_db
import datetime

#-------------------User functions---------------------

def create_user(name, email, password):
    """Create and return a new user."""

    user = User(name=name, email=email, password=password)

    return user

def get_users():
    """Return all users."""

    return User.query.all()

def get_user_by_id(user_id):
    """Get user info."""

    return User.query.get(user_id)

def get_user_by_email(email):
    """Returns a user based off their email."""

    return User.query.filter(User.email == email).first() 

#-------------------Survey functions---------------------
sample_date = datetime.date(2022,6,16)

def create_survey_answer(user_id, q1, q2, q3, q4, q5, date=datetime.date.today()):
    """Create and return survey answers."""

    answer = SurveyAnswer(user_id=user_id, date=date, q1=q1, q2=q2, q3=q3, q4=q4, q5=q5)

    return answer

def get_all_survey_answers():
    """Returns all survery answers."""

    return SurveyAnswer.query.all()

def get_all_survey_answers_by_user_id(user_id):
    """Returns survey answers according to user."""

    return SurveyAnswer.query.filter(SurveyAnswer.user_id == user_id).all() 

def get_all_survey_answers_by_date(date):
    """Returns every users survey answers on a given day."""

    return  SurveyAnswer.query.filter(SurveyAnswer.date == date).all()

def get_survey_answers_by_user_id_and_date(user_id, date):
    """Returns a specific user's survey answers on a specific day."""

    return SurveyAnswer.query.filter(SurveyAnswer.user_id == user_id, SurveyAnswer.date == date).first()

def get_survey_answer_by_survey_answer_id(survey_answer_id):

    return SurveyAnswer.query.get(survey_answer_id)

#-------------------Journal functions---------------------

def create_journal_response(user_id, response, date=datetime.date.today()):
    """Create and return a response to a journal."""

    journal_response = JournalPrompt(user_id=user_id, date=date, response=response)

    return journal_response

def get_journal_prompts():
    """Returns all journal prompts."""

    return JournalPrompt.query.all()

def get_all_journal_entries_by_user_id(user_id):
    """Returns all journal prompts according to user."""

    return JournalPrompt.query.filter(JournalPrompt.user_id == user_id).order_by(JournalPrompt.date).all() 

def get_journal_entry_by_id(journal_response_id):
    """Returns every users journal entry on a given day."""

    return JournalPrompt.query.filter(JournalPrompt.journal_response_id == journal_response_id).first()

def get_journal_entry_by_user_id_and_date(user_id, date):
    """Returns a specific user's entry on a specific day."""
    
    return JournalPrompt.query.filter(JournalPrompt.user_id == user_id, JournalPrompt.date == date).first()

#-------------------Activity functions---------------------

def create_activity(user_id, activity_idea):
    """Create and return user's idea."""

    activity = Activity(user_id=user_id, activity_idea=activity_idea)

    return activity

def get_all_activities():
    """Returns all activities."""

    return Activity.query.all()

def get_all_activities_by_user_id(user_id):
    """Returns survey answers according to user."""

    return Activity.query.filter(Activity.user_id == user_id).all() 

#-------------------End of functions---------------------

if __name__ == '__main__':
    from server import app
    connect_to_db(app)