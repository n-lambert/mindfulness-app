"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server
import requests

#os.system is like running a command on the terminal 
#when u run see_database.py and gets to line 14-15, tell command
#to dropdb ratings, runs only when u run seed_database.py
os.system("dropdb database")
os.system('createdb database')

# affirmation_quotes = requests.get('https://www.affirmations.dev/').json()
# for quote in affirmation_quotes:

model.connect_to_db(server.app)
model.db.create_all() #creates all tables

lst_of_activities = ['Go for a walk',
'Listen to music',
'Take photographs',
'Read a newspaper or magazine',
'Take a bath',
'Sit in the sun',
'Watch a movie',
'Laugh']

for n in range(10):
    name = f"user{n}" # unique name
    email = f"user{n}@test.com"  # unique email
    password = "test"

    user = crud.create_user(email=email, password=password, name=name)
    model.db.session.add(user)
    model.db.session.commit()

    q1 = randint(1, 5)
    q2 = randint(1, 5)
    q3 = randint(1, 5)
    q4 = randint(1, 5)
    q5 = randint(1, 5)

    answer = crud.create_survey_answer(user.user_id, q1, q2, q3, q4, q5)
    model.db.session.add(answer)

    journal_response = "My journal entry"

    new_response = crud.create_journal_response(user.user_id, response=journal_response)
    model.db.session.add(new_response)
    
    for _ in range(3):
        random_activity = choice(lst_of_activities)

        activity = crud.create_activity(user.user_id, activity_idea=random_activity)
        model.db.session.add(activity)
        
    model.db.session.commit()

# model.db.session.commit()

