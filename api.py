
import requests

def get_github_profile(username):
    base = "https://api.github.com"
    profile_url = f"{base}/users/{username}"
    repos_url = f"{base}/users/{username}/repos"

    try:
        p = requests.get(profile_url, timeout=5)
        p.raise_for_status()
        profile = p.json()

        r = requests.get(repos_url, params={"sort":"updated","per_page":5}, timeout=5)
        r.raise_for_status()
        repos = r.json()

        return {
            "name": profile.get("name"),
            "public_repos": profile.get("public_repos"),
            "bio": profile.get("bio"),
            "top_repos": [{ "name": repo["name"], "stars": repo["stargazers_count"], "url": repo["html_url"] } for repo in repos]
        }
    except requests.exceptions.HTTPError as e:
        print("HTTP error:", e)
    except requests.exceptions.Timeout:
        print("Request timed out")
    except Exception as e:
        print("Error:", e)
    return None

if __name__ == "__main__":
    user = input("Enter GitHub username: ").strip()
    data = get_github_profile(user)
    if data:
        print("Name:", data["name"])
        print("Public repos:", data["public_repos"])
        print("Bio:", data["bio"])
        print("Top 5 repos:")
        for repo in data["top_repos"]:
            print("-", repo["name"], "| stars:", repo["stars"], "|", repo["url"])
    else:
        print("Profile not found or error occurred.")
