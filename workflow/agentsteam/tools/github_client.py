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
    def __init__(self, token: str, username: str):
        self.username = username
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
        }

    def _base(self, repo: str) -> str:
        return f"https://api.github.com/repos/{self.username}/{repo}"

    def update_description(self, repo: str, description: str) -> None:
        r = requests.patch(self._base(repo), headers=self.headers, json={"description": description})
        r.raise_for_status()

    def update_topics(self, repo: str, topics: list[str]) -> None:
        r = requests.put(f"{self._base(repo)}/topics", headers=self.headers, json={"names": topics})
        r.raise_for_status()

    def update_visibility(self, repo: str, visibility: str) -> None:
        r = requests.patch(self._base(repo), headers=self.headers, json={"visibility": visibility})
        r.raise_for_status()

    def update_readme(self, repo: str, content: str) -> None:
        # GitHub requires the file SHA when updating an existing file
        existing = requests.get(f"{self._base(repo)}/contents/README.md", headers=self.headers)
        sha = existing.json().get("sha") if existing.status_code == 200 else None
        payload = {
            "message": "docs: update README via profile agent",
            "content": base64.b64encode(content.encode()).decode(),
        }
        if sha:
            payload["sha"] = sha
        r = requests.put(f"{self._base(repo)}/contents/README.md", headers=self.headers, json=payload)
        r.raise_for_status()

