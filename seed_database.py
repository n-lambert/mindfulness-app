"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server
import requests

os.system("dropdb database")
os.system('createdb database')

model.connect_to_db(server.app)

# creates all tables
model.db.create_all()

# list of activities randomly picked from for test users
lst_of_activities = ['Go for a walk',
'Listen to music',
'Take photographs',
'Read a newspaper or magazine',
'Take a bath',
'Sit in the sun',
'Watch a movie',
'Laugh']

for n in range(10):

    # creates unique name and email for test users
    name = f"user{n}"
    email = f"user{n}@test.com"
    password = "test"

    # makes a user and adds to session
    user = crud.create_user(email=email, password=password, name=name)
    model.db.session.add(user)

    # commits each user create in loop
    model.db.session.commit()

    # gives value to each question
    q1 = randint(1, 5)
    q2 = randint(1, 5)
    q3 = randint(1, 5)
    q4 = randint(1, 5)
    q5 = randint(1, 5)

    # creates survey answers for each test user
    answer = crud.create_survey_answer(user.user_id, q1, q2, q3, q4, q5)

    # adds survey answers to the session to be committed
    model.db.session.add(answer)

    journal_response = "My journal entry"

    new_response = crud.create_journal_response(user.user_id, response=journal_response)
    model.db.session.add(new_response)
    
    for _ in range(3):
        # gives each user a random activity
        random_activity = choice(lst_of_activities)

        activity = crud.create_activity(user.user_id, activity_idea=random_activity)
        model.db.session.add(activity)
    
    # commits survey answers, journal response, and activities
    model.db.session.commit()

