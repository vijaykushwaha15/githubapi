import datetime
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

BASE_URL = "https://api.github.com"
REPO_OWNER = "idealo"
REPO_NAME = "mongodb-performance-test"
AUTH_TOKEN = "<your-github-token>"
def get_pull_requests():
    url = f"{BASE_URL}/repos/{REPO_OWNER}/{REPO_NAME}/pulls"
    headers = {"Authorization": f"Token {AUTH_TOKEN}"}
    params = {"state": "all", "sort": "created", "direction": "desc"}
    response = requests.get(url, headers=headers, params=params)
    return response.json()

def filter_pull_requests(pull_requests):
    last_week = datetime.datetime.now() - datetime.timedelta(weeks=1)
    filtered_prs = []
    for pr in pull_requests:
        created_at = datetime.datetime.strptime(pr["created_at"], "%Y-%m-%dT%H:%M:%SZ")
        if created_at >= last_week:
            filtered_prs.append(pr)
    return filtered_prs
def create_email_content(pull_requests):
    content = "Pull Requests Summary\n\n"
    for pr in pull_requests:
        content += f"Title: {pr['title']}\n"
        content += f"State: {pr['state']}\n"
        content += f"Author: {pr['user']['login']}\n"
        content += f"URL: {pr['html_url']}\n"
        content += "\n"
    return content
def send_email(sender, recipient, subject, content):
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = subject
    body = MIMEText(content)
    msg.attach(body)
    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login("<your-email>", "<your-password>")
        server.send_message(msg)