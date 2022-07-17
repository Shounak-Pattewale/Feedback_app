import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from config import DefaultConfig

# Use a service account
cred = credentials.Certificate(DefaultConfig.SERVICE_ACCOUNT_JSON)
firebase_admin.initialize_app(cred)

db = firestore.client()

class Feedback:
    def __init__(self):
        pass

    def addData(res,username,record_id):
        doc_ref = db.collection(u'test').document(username)
        doc_ref.set({
            "question1": res['question1'],
            "question2": res['question2'],
            "question3": res['question3'],
            "question4": res['question4'],
            "question5": res['question5'],
            "record_id": record_id
        })

        # print("Data Added => ",username,record_id)

        return True