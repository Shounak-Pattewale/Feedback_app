from datetime import datetime, timedelta
import requests


class Feedback:
    def __init__(self):
        pass

    def send_feedback(res):

        data = {
            "query_noted_feedback": res['query_noted_feedback'],
            "behaviour_feedback": res['behaviour_feedback'],
            "query_resolved_feedback": res['query_resolved_feedback'],
            "rating_feedback": res['rating_feedback'],
            "feedback_suggestion": res['feedback_suggestion']
        }
        try:
            res = requests.post(url='http://127.0.0.1:5001/test', json=data)
            response = res.json()
            response['status_code'] = res.status_code
            return response
        except Exception as ex:
            print("EXCEPTION :::: ",ex)
            return ex
