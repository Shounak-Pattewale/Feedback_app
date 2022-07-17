import os

from flask import Flask, redirect, url_for, render_template, request, session, flash, jsonify
from werkzeug.exceptions import HTTPException

from services.app_services import Feedback
from services import db

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

# Feedback form
@app.get('/Record/<string:username>/Uploads/<string:record_id>/Feedback')
def get_feedback(username,record_id):
    try:    
        # print("ARGS 1 => ",username,record_id)
        return render_template("feedback.html",username=username,record_id=record_id)
    except Exception as ex:
        return render_template("errors/exception_error.html", exception=ex)

@app.post('/Record/<string:username>/Uploads/<string:record_id>/Feedback')
def post_feedback(username,record_id):
    try:
        res = request.form
        try:
            # print("ARGS 2 => ",username,record_id)
            if db.Feedback.addData(res,username,record_id):
                flash("Feedback submitted successfully", "success")
                return redirect(url_for('get_feedback',username=username,record_id=record_id))
            else:
                flash("Something went wrong", "danger")
                return redirect(url_for('get_feedback',username=username,record_id=record_id))
        except:
            flash("Something went wrong", "danger")
            return redirect(url_for('get_feedback',username=username,record_id=record_id))
    except Exception as ex:
        return render_template("errors/exception_error.html", exception=ex)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT',5001)), debug=True)