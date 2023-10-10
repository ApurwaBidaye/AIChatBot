# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher


class ActionCollectIDPwd(Action):

     def name(self) -> Text:
         return "action_collect_id_pwd"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         
         AgencyID=tracker.latest_message['text']
         Password=tracker.latest_message['text']

         return [SlotSet("AgencyID",AgencyID),SlotSet("Password",Password)]

