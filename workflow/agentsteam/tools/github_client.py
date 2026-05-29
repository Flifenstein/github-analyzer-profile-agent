import requests
import base64
#shoot, i have to read https://docs.github.com/en/rest?apiVersion=2026-03-10
#reminder TODP to define later the def _get for the 3 repetitive requests API lines

class GitHubReader:
    def __init__(self, token: str, username: str):
        self.token = token
        self.username = username
        self.headers = {"Authorization": f"Bearer {token}"} 
    
    def list_repos(self) -> list[dict]:
         url = f"https://api.github.com/user/repos?per_page=100&affiliation=owner"
         response = requests.get(url, headers=self.headers)
         response.raise_for_status()
         return response.json()
         
    def get_readme(self, repo: str):
        url = f"https://api.github.com/repos/{self.username}/{repo}/readme"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 404:
            print(f"Repo {repo} does not have a README")
            return None
        response.raise_for_status()
        data = response.json()
        return data
    
    def get_repo_details(self, repo: str):
        url = "https://api.github.com/repos/{self.username}/{repo}"
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()
        data = response.json()
        return base64.b64decode(data["content"]).decode("utf-8")

    def get_file_tree(self, repo: str):
        url = f"https://api.github.com/repos/{self.username}/{repo}/git/trees/HEAD?recursive=1"
        response = requests.get(url, headers = self.headers)
        response.raise_for_status()
        data = response.json()
        return [item["path"] for item in data["tree"]]
    
    def get_commits(self, repo: str):
         url = f"https://api.github.com/repos/{self.username}/{repo}/commits?per_page=20"
         response = requests.get(url, headers = self.headers)
         response.raise_for_status()
         data = response.json()
         return [item["commit"]["message"] for item in data]

        

class GitHubWriter:

