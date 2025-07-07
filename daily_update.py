import os
import requests
from git import Repo
from datetime import datetime

# 🔧 Configure your GitHub topics here
TOPICS = ["serverless", "blockchain", "python"]
RELEASE_LIMIT = 3  # Max repos per topic to avoid rate limits

# 📁 Markdown filename
MARKDOWN_FILE = "ecosystem-daily.md"

def fetch_latest_releases(topic):
    print(f"Fetching for topic: {topic}")
    url = f"https://api.github.com/search/repositories?q=topic:{topic}&sort=updated&order=desc"
    response = requests.get(url)
    data = response.json()

    releases = []
    for repo in data.get("items", [])[:RELEASE_LIMIT]:
        repo_name = repo["full_name"]
        release_url = f"https://api.github.com/repos/{repo_name}/releases/latest"
        rel_res = requests.get(release_url)
        if rel_res.status_code != 200:
            continue
        rel = rel_res.json()
        if not rel.get("tag_name"):
            continue
        releases.append({
            "name": repo_name,
            "tag": rel["tag_name"],
            "published": rel["published_at"][:10] if rel.get("published_at") else "Unknown",
            "url": rel.get("html_url", repo["html_url"]),
            "release_notes": rel.get("html_url", repo["html_url"])
        })
    return releases

def write_markdown(updates):
    today = datetime.utcnow().strftime("%Y-%m-%d")
    content = f"# 🌐 Ecosystem Daily Log – {today}\n\n"
    for topic, rels in updates.items():
        content += f"## 🔹 {topic.capitalize()}\n"
        if not rels:
            content += "- No recent releases found.\n"
        for r in rels:
            content += f"- [{r['name']}]({r['url']}) – `{r['tag']}` (📅 {r['published']})  \n"
            content += f"  🔗 [Release Notes]({r['release_notes']})\n"
        content += "\n"
    with open(MARKDOWN_FILE, "w", encoding="utf-8") as f:
        f.write(content.strip())

def commit_and_push():
    repo = Repo(".")
    repo.git.add(MARKDOWN_FILE)
    repo.index.commit(f"📦 Update ecosystem daily log – {datetime.utcnow().strftime('%Y-%m-%d')}")
    origin = repo.remote(name="origin")
    origin.push()
    print("✅ Pushed to GitHub")

def main():
    updates = {}
    for topic in TOPICS:
        updates[topic] = fetch_latest_releases(topic)
    write_markdown(updates)
    commit_and_push()

if __name__ == "__main__":
    main()
