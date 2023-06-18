import requests
import datetime
import json
# GitHub API base URL
base_url = "https://api.github.com"

# Configure your GitHub repository
repository = "a-patel/LiteXCache"
REPO_OWNER = "a-patel"
REPO_NAME = "LiteXCache"
#url = f'{base_url}/repos/{repository}/pulls'
url = f"{BASE_URL}/repos/{REPO_OWNER}/{REPO_NAME}/pulls"
# Generate a datetime object for the last week
last_week = datetime.datetime.now() - datetime.timedelta(days=7)

# Convert datetime to ISO 8601 format
last_week_iso = last_week.isoformat(timespec='seconds')

# Get pull requests
params = {
    "state": "all",
    "sort": "created",
    "direction": "desc",
    "per_page": 100,
    "since": last_week_iso
}

headers = {
    "Accept": "application/vnd.github.v3+json"
}

response = requests.get(url, params=params, headers=headers)

if response.status_code == 200:
    pull_requests = response.json()

    # Initialize counters
    opened_count = 0
    closed_count = 0
    draft_count = 0

    # Print summary to console
    print("Summary of Pull Requests in the Last Week")
    print("========================================")

    for pr in pull_requests:
        pr_state = pr["state"]
        if pr_state == "open":
            opened_count += 1
        elif pr_state == "closed":
            closed_count += 1
        elif pr_state == "draft":
            draft_count += 1

        print(f"Pull Request #{pr['number']}: {pr['title']}")
        print(f"State: {pr_state}")
        # print(f"Commit Messages:")
        
        # # Get commit messages for the pull request
        # commits_url = pr["commits_url"].split("{")[0]
        # commits_response = requests.get(commits_url, headers=headers)

        # if commits_response.status_code == 200:
        #     commits = commits_response.json()
        #     for commit in commits:
        #         print(f"- {commit['commit']['message']}")
        # else:
        #     print(f"Failed to retrieve commits for Pull Request #{pr['number']}.")

        # print()

    print(f"Opened: {opened_count}")
    print(f"Closed: {closed_count}")
    print(f"Draft: {draft_count}")

else:
    print(f"Failed to retrieve pull requests. Status code: {response.status_code}")