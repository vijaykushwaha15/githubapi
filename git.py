import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# GitHub API endpoint for pull requests
url = 'https://github.com/tariqbuilds/linux-dash/pulls'

# GitHub repository details
owner = 'tariqbuilds'
repo = 'linux-dash'

# Email details
from_email = 'vijaykushvknk@gmail.com'
to_email = '15.vijaykushwaha@example.com'
subject = 'Pull Request Summary'
smtp_server = 'smtp.gmail.com'
smtp_port = 587
smtp_username = 'vijaykushvknk@gmail.com'
smtp_password = 'Vijay@321'

# Get the last week's date
# You may need to adjust the date format based on the GitHub API response
import datetime
last_week = datetime.datetime.now() - datetime.timedelta(days=7)
last_week_str = last_week.strftime('%Y-%m-%dT%H:%M:%SZ')

# Make a request to GitHub API to fetch pull requests
params = {'state': 'all', 'since': last_week_str}
response = requests.get(url.format(owner=owner, repo=repo), params=params)

if response.status_code == 200:
    pull_requests = response.json()
    
    # Filter pull requests by state (opened, closed, draft)
    opened_prs = [pr for pr in pull_requests if pr['state'] == 'open']
    closed_prs = [pr for pr in pull_requests if pr['state'] == 'closed']
    draft_prs = [pr for pr in pull_requests if pr['draft'] is True]
    
    # Create the email content
    content = f"Opened Pull Requests ({len(opened_prs)}):\n"
    content += '\n'.join([f"- {pr['title']} ({pr['html_url']})" for pr in opened_prs])
    content += f"\n\nClosed Pull Requests ({len(closed_prs)}):\n"
    content += '\n'.join([f"- {pr['title']} ({pr['html_url']})" for pr in closed_prs])
    content += f"\n\nDraft Pull Requests ({len(draft_prs)}):\n"
    content += '\n'.join([f"- {pr['title']} ({pr['html_url']})" for pr in draft_prs])

    # Create the email message
    message = MIMEMultipart()
    message['From'] = from_email
    message['To'] = to_email
    message['Subject'] = subject
    message.attach(MIMEText(content, 'plain'))

    # Send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(message)
        server.quit()
        print("Email sent successfully!")
    except smtplib.SMTPException as e:
        print("Failed to send email:", str(e))
else:
    print("Failed to fetch pull requests from GitHub API:", response.text)