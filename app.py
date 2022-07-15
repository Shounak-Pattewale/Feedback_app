from datetime import datetime

from flask import Flask, redirect, url_for, render_template, request, session, flash, jsonify
from werkzeug.exceptions import HTTPException

from services.app_services import Feedback
from config import DefaultConfig

app = Flask(__name__)

# Load default configuration for the application (common across environments)
app.config.from_object(DefaultConfig)

@app.errorhandler(Exception)
def handle_exception(e):
    # HTTP errors
    if isinstance(e, HTTPException):
        res = {
            "status_code": e.code,
            "error_name": e.name,
            "error_description": e.description,
        }
        return render_template("errors/error.html", res=res), e.code

# HOME PAGE : Feedback form
@app.get('/')
def get_feedback():
    try:    
        return render_template("feedback.html")
    except Exception as ex:
        return render_template("errors/exception_error.html", exception=ex)

@app.post('/')
def post_feedback():
    try:
        res = request.form
        response = Feedback.send_feedback(res)
        print("Form Response == >> ",response)
        try:
            if response['status_code'] == 200:
                flash("Feedback submitted successfully", "success")
                return redirect(url_for('get_feedback'))
            else:
                flash("Something went wrong", "danger")
                return render_template('/')
        except:
            flash("Something went wrong", "danger")
            return render_template('/')
    except Exception as ex:
        return render_template("errors/exception_error.html", exception=ex)

# API Test
@app.post('/test')
def test():
    body = request.get_json()
    print("API BODY == >>",body)
    return body

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)