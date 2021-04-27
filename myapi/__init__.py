import firebase_admin
from firebase_admin import credentials

from quiz.newcron import sendMessage, sendFirebaseMessage

cred = credentials.Certificate("service_account.json")
firebase_admin.initialize_app(cred)
sendFirebaseMessage()
