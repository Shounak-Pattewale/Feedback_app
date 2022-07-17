import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

from config import DefaultConfig
from datetime import datetime, timedelta, timezone

# Use a service account
cred = credentials.Certificate(DefaultConfig.SERVICE_ACCOUNT_JSON)
firebase_admin.initialize_app(cred)

db = firestore.client()

class Feedback:
    def __init__(self):
        pass

    def addData(res,username,record_id):

        utc_date_time = datetime.utcnow() + timedelta(hours=5.5)
        date = utc_date_time.strftime("%m/%d/%Y")
        time = utc_date_time.strftime("%H:%M:%S")
        utc_timestamp = datetime.now(timezone.utc).replace(tzinfo=timezone.utc).timestamp()

        doc_ref = db.collection(u'test').document(username)
        doc_ref.set({
            "question1": res['question1'],
            "question2": res['question2'],
            "question3": res['question3'],
            "question4": res['question4'],
            "question5": res['question5'],
            "record_id": record_id,
            "date" : date,
            "time" : time,
            "timestamp": utc_timestamp
        })

        # print("Data Added => ",username,record_id)

        return True