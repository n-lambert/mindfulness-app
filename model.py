"""Models for mantra app."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
#creating a sqlachemy object

class User(db.Model):
    """A user."""

    __tablename__ = "users"

    user_id = db.Column(db.Integer,
                        autoincrement=True,
                        primary_key=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    name = db.Column(db.String)

    # survey_answers magic attribute
    # journal_responses magic attribute
    # activities magic attribute
    
    def __repr__(self):
        return f'<User user_id={self.user_id} name={self.name} email={self.email}>'


class SurveyAnswer(db.Model):
    """Survey asnwers."""

    __tablename__ = "survey_answers"

    survey_answer_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    date = db.Column(db.Date)
    q1 = db.Column(db.Integer)
    q2 = db.Column(db.Integer)
    q3 = db.Column(db.Integer)
    q4 = db.Column(db.Integer)
    q5 = db.Column(db.Integer)
    
    user = db.relationship("User", backref="survey_answers")

    def __repr__(self):
        return f"<SurveyAnswer survey_answer_id={self.survey_answer_id} q1={self.q1} date={self.date}>"


class JournalPrompt(db.Model):
    """Journal prompt responses."""

    __tablename__ = "journal_responses"

    journal_response_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    date = db.Column(db.Date)
    response = db.Column(db.Text)

    user = db.relationship("User", backref="journal_responses")

    def __repr__(self):
        return f"<JournalPrompt journal_response_id={self.journal_response_id} date={self.date}>"


class Activity(db.Model):
    """Activities for mindfulness."""

    __tablename__ = "activities"

    activity_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    activity_idea = db.Column(db.Text)

    user = db.relationship("User", backref="activities")



    def __repr__(self):
        return f"<Activity activity_id={self.activity_id} activity_idea={self.activity_idea}>"

# ask for more explanation lines 78-86
def connect_to_db(flask_app, db_uri="postgresql:///database", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)