import os
import sys
import requests
from datetime import datetime, timezone

# 🔧 All topics — rotated each run based on execution count
ALL_TOPICS = [
    "ai-ethics", "quantum-computing", "edge-computing", "webassembly", "green-software",
    "machine-learning", "devops", "blockchain", "serverless", "python",
    "rust", "typescript", "kubernetes", "open-source", "cybersecurity",
    "data-science", "cloud-native", "llm", "neural-network", "robotics"
]

RELEASE_LIMIT = 3
MARKDOWN_FILE = "ecosystem-daily.md"
GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")

def get_headers():
    if GITHUB_TOKEN:
        return {"Authorization": f"token {GITHUB_TOKEN}"}
    return {}

def pick_topics(execution_count, n=5):
    """Rotate topic selection based on execution count so each commit has different content."""
    start = (execution_count * n) % len(ALL_TOPICS)
    indices = [(start + i) % len(ALL_TOPICS) for i in range(n)]
    return [ALL_TOPICS[i] for i in indices]

def fetch_latest_releases(topic):
    print(f"Fetching: {topic}")
    headers = get_headers()
    url = f"https://api.github.com/search/repositories?q=topic:{topic}&sort=updated&order=desc"
    response = requests.get(url, headers=headers)
    data = response.json()

    releases = []
    for repo in data.get("items", [])[:RELEASE_LIMIT]:
        repo_name = repo["full_name"]
        rel_res = requests.get(f"https://api.github.com/repos/{repo_name}/releases/latest", headers=headers)
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
        })
    return releases

def write_markdown(updates, execution_count):
    now = datetime.now(timezone.utc)
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S UTC")
    today = now.strftime("%Y-%m-%d")

    content = f"# 🌐 Ecosystem Log – {today}\n\n"
    content += f"> 🔄 Execution #{execution_count} — Last updated: `{timestamp}`\n\n"

    for topic, rels in updates.items():
        content += f"## 🔹 {topic.replace('-', ' ').title()}\n"
        if not rels:
            content += "- No recent releases found.\n"
        for r in rels:
            content += f"- [{r['name']}]({r['url']}) – `{r['tag']}` (📅 {r['published']})\n"
        content += "\n"

    with open(MARKDOWN_FILE, "w", encoding="utf-8") as f:
        f.write(content.strip())

def main():
    execution_count = int(os.environ.get("EXECUTION_COUNT", 0))
    topics = pick_topics(execution_count)
    print(f"Run #{execution_count} | Topics: {topics}")

    updates = {}
    for topic in topics:
        updates[topic] = fetch_latest_releases(topic)

    write_markdown(updates, execution_count)
    print("Done.")

if __name__ == "__main__":
    main()
