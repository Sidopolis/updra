# 🌐 Updra — Automated Daily GitHub Ecosystem Tracker

**Updra** is your personal robot assistant that checks the latest releases in your favorite tech topics on GitHub every day, writes a neat report, and saves it to this repository — all by itself!

---

## 🚀 What does it do?

- **Every day, automatically:**
  - Looks up the latest GitHub releases for topics you care about (like `ai-ethics`, `quantum-computing`, `edge-computing`, `webassembly`, `green-software`).
  - Writes a daily summary in a Markdown file: `ecosystem-daily.md`.
  - Pushes the update to this repository — you don't have to lift a finger!

---

## 🛠️ How does it work?

- **Python script** (`daily_update.py`) fetches and writes the daily report.
- **GitHub Actions** (`.github/workflows/daily.yml`) runs the script every day and handles all git operations.
- **No manual work needed** after setup.

---

## 📦 What do you need to use or modify it?

1. **Clone this repo** (or fork it).
2. **Install dependencies** (if you want to run locally):
   ```
   pip install -r requirements.txt
   ```
3. **Change the topics** you want to track:
   - Edit the `TOPICS` list in `daily_update.py`.
4. **Push your changes** — GitHub Actions will take care of the rest!

---

## 🕒 How is it automated?

- The workflow file (`.github/workflows/daily.yml`) is set to run every day at 6 AM UTC.
- It installs dependencies, runs the script, and pushes the new report.

---

## 📋 Example output

Every day, you'll see a file like this:

```
# 🌐 Ecosystem Daily Log – 2025-07-07

## 🔹 AI-Ethics
- No recent releases found.

## 🔹 Quantum-Computing
- No recent releases found.

## 🔹 Edge-Computing
- No recent releases found.

## 🔹 WebAssembly
- No recent releases found.

## 🔹 Green-Software
- No recent releases found.
```

When new releases are found, they'll be listed with links and details.

---

## 💡 Why is this useful?

- Stay up to date with the latest in your tech ecosystem.
- Keep your repo active and informative.
- No manual work — just set and forget!

---

## 📝 Want to customize?

- Change the topics in `daily_update.py`.
- Adjust the schedule in `.github/workflows/daily.yml` if you want a different time.

---

**Enjoy your automated GitHub ecosystem tracker!** 