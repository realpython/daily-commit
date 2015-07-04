import os
import requests
import moment
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from project import app

# globals

ADDRESS = os.environ["address"]
PASSWORD = os.environ["password"]
PHONE_NUMBER = os.environ["phone_number"]

# routes


@app.route("/ping")
def index():
    return "pong!"


@app.route("/test")
def get_updates():
    git_commits = get_user_commits()
    if git_commits["total_count"] > 0:
        subject = "Great job today, pal. Keep up the good work!"
        send_text(subject)
        return "yay!"
    subject = "You better commit before you go to sleep!"
    send_text(subject)
    return "nay!"


# helper functions

USER = 'mjhea0'  # change me!


def get_user_commits():
    today = moment.now().format("YYYY-M-D")
    base_url = 'https://api.github.com/search/repositories'
    api_endpoint = base_url + '?q=user:{0}+pushed:{1}'.format(USER, today)
    try:
        resp = requests.get(api_endpoint)
        return resp.json()
    except:  # silencing all errors - bad!
        return "yikes! something went wrong!"


def send_text(subject):

    # connect to the server
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(ADDRESS, PASSWORD)

    # prepare message
    msg = MIMEMultipart()
    msg['From'] = ADDRESS
    msg['To'] = PHONE_NUMBER
    msg = MIMEText(subject)

    # send message
    server.sendmail(ADDRESS, PHONE_NUMBER, msg.as_string())
    server.quit()
