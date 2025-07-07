# Updra — Daily Ecosystem Tracker

## 📌 Overview
Updra is a fully automated tool that fetches the latest releases from GitHub repositories in selected topics and commits a daily Markdown digest to this repository.  
This project requires no manual input once set up.

---

## 🎯 What This Project Does
- Every day at a fixed time:
  - Fetch the most recent **GitHub releases** for selected topics (for example: `serverless`, `blockchain`, `python`).
  - Generate a Markdown file named `ecosystem-daily.md`.
  - For each release, include:
    - Repository name and link
    - Release tag or version
    - Release publication date
    - Link to release notes
  - Commit and push the update automatically to this repo.

✅ Fully automated.  
✅ No manual work required after initial configuration.  
✅ Keeps the repository looking active and up-to-date.

---

## 🛠️ Tech Stack
- **Language:** Python 3.x
- **Libraries:**
  - `requests` (to fetch GitHub API data)
  - `GitPython` (to commit and push updates)
- **Automation:** GitHub Actions (to run the script every day)

---

## 🧩 Features
1. **Fetch Releases**
   - Use GitHub REST API (public) to get the most recent release per repository in each topic.
2. **Generate Markdown**
   - Append or create a section with:
     ```
     # Daily Ecosystem Update - YYYY-MM-DD

     ## Topic Name

     - [Repository Name](repo_url) - v1.2.3 (Published: YYYY-MM-DD)
       [Release Notes](release_url)
     ```
3. **Commit and Push**
   - Automatically stage, commit, and push changes.
   - Use a clear commit message:
     ```
     Update ecosystem daily log - YYYY-MM-DD
     ```
4. **Scheduled Automation**
   - GitHub Actions workflow to run once daily at a fixed time (e.g., 6 AM UTC).

---

## ⚙️ Project Structure
```
updra/
├── daily_update.py           # Main Python script
├── requirements.txt          # Python dependencies
├── .github/
│   └── workflows/
│       └── daily.yml         # GitHub Actions workflow
└── README.md                 # Project description
```

---

## 📝 Requirements
**Functional Requirements:**
- The script must pull the latest releases from GitHub by topic.
- The script must update `ecosystem-daily.md`.
- The script must commit and push the file.
- The workflow must run automatically every 24 hours.

**Non-Functional Requirements:**
- All libraries and services used must be free/open.
- The script should handle API rate limits gracefully.
- The Markdown output should be clean, minimal, and easy to read.

---

## 📈 Example Topics to Track
These topics can be configured inside the script:
- `serverless`
- `blockchain`
- `python`
- `machine-learning`
- `devops`

---

## ✅ Success Criteria
- A commit is created every day automatically.
- The Markdown file includes the most recent releases.
- No manual intervention is needed once deployed.

---

## 🎯 What You Should Do
After setting this up:
- **Install dependencies** (`pip install -r requirements.txt`)
- **Configure GitHub Actions** (`.github/workflows/daily.yml`)
- **Customize the list of topics you care about**

---

## 📝 Notes
- You may add a GitHub token if you want to track more topics or avoid rate limits.
- You can choose whether to append entries (growing file) or create one file per day.
- This project is named **Updra**.

