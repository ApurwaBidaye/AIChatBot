# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
import psycopg2
import sqlite3
from sqlalchemy import select, create_engine, Table, Column, Integer, String, MetaData
import sqlalchemy as db

engine = db.create_engine('postgresql://postgres:root@localhost:5432/onyxdatabase')
conn = engine.connect()

metadata = db.MetaData()

class ValidateLoginForm(FormValidationAction):
    
    def name(self) -> Text:
        return "validate_login_form"
    
    def validate_AgencyID(self, value, dispatcher, tracker, domain):

        table = db.Table('agency_user_table', metadata, autoload=True, autoload_with=engine)
        stmt = db.select([table.columns.agency_id]).where(table.columns.agency_id == value)

        results = conn.execute(stmt).fetchall()

        if results:
            print("Valid Agency ID")
            return {"AgencyID": value}
        else:
            print("Invalid Agency ID")
            dispatcher.utter_message("Invalid Agency ID. Please try again.")
            return {"AgencyID": None}

    def validate_Password(self, value, dispatcher, tracker, domain):

        value = str(value)
        agency_id = tracker.get_slot("AgencyID")

        table = db.Table('agency_user_table', metadata, autoload=True, autoload_with=engine)
        stmt = db.select([table.columns.agency_id]).where(table.columns.agency_id == agency_id, table.columns.password == value)

        results = conn.execute(stmt).fetchall()

        if results:
            print("Valid Password")
            dispatcher.utter_message("Login Successful")
            return {"Password": value}
        else:
            print("Invalid Password")
            dispatcher.utter_message("Invalid Password. Please try again.")
            return {"Password": None}
            

    


