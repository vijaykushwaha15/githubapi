import datetime
import requests
import smtplib
import argparse
import json
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

BASE_URL = "https://api.github.com"
REPO_OWNER = "idealo"
REPO_NAME = "mongodb-performance-test"
AUTH_TOKEN = "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"
def get_pull_requests():
    url = f"{BASE_URL}/repos/{REPO_OWNER}/{REPO_NAME}/pulls"
    headers = {"Authorization": f"Token {AUTH_TOKEN}"}
    last_week = datetime.datetime.now() - datetime.timedelta(days=7)
    last_week_str = last_week.strftime('%Y-%m-%dT%H:%M:%SZ')
    params = {"state": "all", "sort": "created", "direction": "desc", 'since': last_week_str}
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        pull_requests = response.json()
        filter_pull_requests(pull_requests)
def filter_pull_requests(pull_requests):
       # Filter pull requests by state (opened, closed, draft)
        opened_prs = [pr for pr in pull_requests if pr['state'] == 'open']
        closed_prs = [pr for pr in pull_requests if pr['state'] == 'closed']
        draft_prs = [pr for pr in pull_requests if pr['draft'] is True]
        print(closed_prs)


# def create_email_content(pull_requests):
#     content = "Pull Requests Summary\n\n"
#     for pr in pull_requests:
#         content += "Title: {pr['title']}\n"
#         content += "State: {pr['state']}\n"
#         content += "Author: {pr['user']['login']}\n"
#         content += "URL: {pr['html_url']}\n"
#         content += "\n"
#     return content
# def send_email(sender, recipient, subject, content):
#     msg = MIMEMultipart()
#     msg["From"] = sender
#     msg["To"] = recipient
#     msg["Subject"] = subject
#     body = MIMEText(content)
#     msg.attach(body)
#     with smtplib.SMTP("smtp.gmail.com", 587) as server:
#         server.starttls()
#         server.login("vijaykushvknk@gmail.com", "Vijay@321")
#         server.send_message(msg)
get_pull_requests()
# if __name__ == "__main__":
#     # Construct the argument parser
#     ap = argparse.ArgumentParser()
#     # Add the arguments to the parser
#     ap.add_argument("-gt", "--githib_token", required=True,
#     help="github token")
#     ap.add_argument("-ro", "--repo_owner", required=True,
#     help="owner of the repository")
#     ap.add_argument("-rn", "--repo_name", required=True,
#     help="name of the repository")
#     args = vars(ap.parse_args())
#     project = str(args['project']).lower()
#     env = str(args['environment']).lower()
#     githib_token = args['githib_token']
#     repo_owner = args['repo_owner']
#     repo_name = args['repo_name']
    

    