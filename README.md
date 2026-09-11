<div align="center">

# 🚀 Automate Job Search

**Smart Internship Monitor** — scrapes AI internships from [Internshala](https://internshala.com), tracks them in SQLite, and flags the ones that are **new**.

![Python](https://img.shields.io/badge/Python-3.13+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![Requests](https://img.shields.io/badge/Requests-2F74C0?style=for-the-badge&logo=python&logoColor=white)
![BeautifulSoup](https://img.shields.io/badge/BeautifulSoup-3A9E3A?style=for-the-badge&logo=python&logoColor=white)

</div>

---

## ✨ Features

| | |
|---|---|
| 🕷️ **Scrapes** | AI internship listings from pages 1–3 of Internshala |
| 📋 **Extracts** | title, company, location, stipend, skills & job URL |
| 🗄️ **Stores** | everything into a local SQLite database |
| 🆕 **Detects new jobs** | only brand-new listings are reported, duplicates skipped |
| 📄 **CSV export** | scraped data saved to `web_scrap_internship.csv` |

---

## 📁 Folder Structure

```
automate-job-search/
├── .intersala/              🐍 Python virtual environment
│   └── Scripts/
│       └── activate.bat     ⚡ Activation script (Windows)
├── .deepeval/               🧪 DeepEval workspace
├── notebook/
│   └── internsala.ipynb     📓 Jupyter notebook for experiments
├── __pycache__/             💾 Python bytecode cache (gitignored)
├── .gitignore
├── database.py              🗄️ SQLite helpers (create_table, is_new_job, save_job)
├── internships.db           📦 SQLite database of scraped internships
├── main.py                  🚀 Entry point: scrape, compare & report new jobs
├── requirements.txt         📦 Python dependencies
├── scraper.py               🕷️ Internshala web scraper
└── web_scrap_internship.csv 📄 Exported scraped internship data
```

---

## 🔧 Prerequisites

- **Python 3.13+**
- **Windows** (activation commands below are Windows-specific)

---

## 🛠️ Setup

### Option 1 — Use the existing virtual environment

```bash
# 1. Activate the virtual environment (Windows)
C:\projects\automate-job-search\.intersala\Scripts\activate.bat

# 2. Install dependencies
pip install -r requirements.txt
```

### Option 2 — Create your own environment

```bash
python -m venv .intersala
.intersala\Scripts\activate
pip install -r requirements.txt
```

---

## ▶️ Usage

Run the scraper:

```bash
python main.py
```

On each run, `main.py`:
1. Creates the `internships` table if it doesn't exist
2. Scrapes internships from Internshala (pages 1–3)
3. Compares each listing against the database
4. Prints `🆕 NEW JOB` for new internships and saves them to `internships.db`
5. Prints a summary of total new internships found

> ### ⏰ Daily Monitoring
>
> Run the script **every day** to catch newly posted internships.
> Any listing that was **not already in your database** will be reported as `NEW JOB`,
> along with a count of how many new internships were found.

---

## 🗄️ Database Schema

**Table:** `internships`

| Column      | Type      | Notes                         |
|-------------|-----------|-------------------------------|
| `id`        | INTEGER   | Primary key, auto-increment   |
| `title`     | TEXT      | Required, internship title    |
| `company`   | TEXT      | Company name                  |
| `location`  | TEXT      | Internship location(s)        |
| `stipend`   | TEXT      | Stipend amount                |
| `skills`    | TEXT      | Required skills               |
| `url`       | TEXT      | Unique job listing URL        |
| `created_at`| TIMESTAMP | Defaults to current timestamp |
| `email_sent`| INTEGER   | Defaults to 0 (reserved)      |

---

## 📦 Dependencies

| Package         | Purpose                        |
|-----------------|--------------------------------|
| `requests`      | HTTP requests to Internshala   |
| `beautifulsoup4`| HTML parsing                   |
| `lxml`          | Fast HTML parser               |
| `pandas`        | CSV export                     |

---

## 📝 Notes

- 🚫 The virtual environment (`.intersala/`) and `__pycache__/` are gitignored.
- ⏳ Scraping respects a **2-second delay** between page requests.
- 🛡️ A browser `User-Agent` header is used to avoid request blocking.

---

<div align="center">

Made with ❤️ for the daily job hunt

</div>