import requests
import json

def get_code_review(repo_owner, repo_name, pull_request_number):
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/pulls/{pull_request_number}/reviews"
    headers = {"Authorization": "token YOUR_GITHUB_TOKEN"}
    response = requests.get(url, headers=headers)
    reviews = json.loads(response.text)
    return reviews

# Example usage
reviews = get_code_review("owner", "repo", 1)
for review in reviews:
    print(f"Review by {review['user']['login']}: {review['state']}")
