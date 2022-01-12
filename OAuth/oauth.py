"""
OAuth is not an API or a service: it’s an open standard for authorization and anyone can implement it.
More specifically, OAuth is a standard that apps can use to provide client applications with “secure delegated access”.
OAuth works over HTTPS and authorizes devices, APIs, servers, and applications with access tokens rather than credentials.
"""

import json
import requests

MY_USERNAME = "subash-kc"  # Make sure you put your own username in here!

def create_repo(repo_name: str, token: str) -> str:
    """
    This will create a repo for your GitHub account.
    """
    repo_data = {"name": repo_name}
    json_data = json.dumps(repo_data)
    headers = {"Authorization": f"token {token}"}
    r = requests.post(f"https://api.github.com/user/repos", data=json_data, headers=headers)
    response_code = r.status_code
    response = r.text
    print(response_code, response)
    return response

def show_repos(username: str, token: str) -> list:
    """
    This will list out all of the repos associated with your GitHub account.
    """
    url = f"https://api.github.com/users/{username}/repos"
    headers = {"Authorization": f"token {token}"}
    r = requests.get(url, headers=headers)
    resp_headers = r.headers
    print(f"""Rate - \n            Limit: {resp_headers['X-RateLimit-Limit']}
            Used: {resp_headers['X-RateLimit-Used']}
            Remaining: {resp_headers['X-RateLimit-Remaining']}""")
    repos = list(r.json())
    for repo in repos:
        print(repo['name'])
    return repos

def get_token() -> str:
    # Read token in from file
    with open("C:\\Users\\mksubash\\Desktop\\token") as f:
        token = f.read().rstrip("\n")
        return token

if __name__ == "__main__":
    tkn = get_token()
    show_repos(MY_USERNAME, tkn)
    create_repo("learning_oauth", tkn)