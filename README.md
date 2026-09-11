# Automate Job Search

A Python script that scrapes **Artificial Intelligence (AI) internships** from [Internshala](https://internshala.com), stores them in a SQLite database, and reports newly posted internships.

## Features

- Scrapes AI internship listings from the first 3 pages of Internshala
- Extracts title, company, location, stipend, skills, and job URL
- Stores internships in a local SQLite database (`internships.db`)
- Detects and prints only **new** internships on each run (duplicates are skipped)
- Outputs scraped data to a CSV file (`web_scrap_internship.csv`)

## Folder Structure

```
automate-job-search/
├── .intersala/              # Python virtual environment
│   └── Scripts/
│       └── activate.bat     # Activation script (Windows)
├── .deepeval/               # DeepEval workspace
├── notebook/
│   └── internsala.ipynb     # Jupyter notebook for experiments
├── __pycache__/             # Python bytecode cache (gitignored)
├── .gitignore
├── database.py              # SQLite helpers (create_table, is_new_job, save_job)
├── internships.db           # SQLite database of scraped internships
├── main.py                  # Entry point: scrape, compare, and report new jobs
├── requirements.txt         # Python dependencies
├── scraper.py               # Internshala web scraper
└── web_scrap_internship.csv # Exported scraped internship data
```

## Prerequisites

- Python 3.13+
- Windows (venv activation commands below are Windows-specific)

## Setup

```bash
# 1. Activate the virtual environment (Windows)
C:\projects\automate-job-search\.intersala\Scripts\activate.bat

# 2. Install dependencies
pip install -r requirements.txt
```

Alternatively, create your own environment:

```bash
python -m venv .intersala
.intersala\Scripts\activate
pip install -r requirements.txt
```

## Usage

Run the scraper:

```bash
python main.py
```

On each run, `main.py`:
1. Creates the `internships` table if it doesn't exist
2. Scrapes internships from Internshala (pages 1-3)
3. Compares each listing against the database
4. Prints `NEW JOB` for new internships and saves them to `internships.db`
5. Prints a summary of total new internships found

> **Note:** Run the script **every day** to catch newly posted internships. Any listing that was not already in your database will be reported as `NEW JOB` along with a count of new internships found.

## Database Schema

Table: `internships`

| Column      | Type      | Notes                          |
|-------------|-----------|--------------------------------|
| id          | INTEGER   | Primary key, auto-increment    |
| title       | TEXT      | Required, internship title     |
| company     | TEXT      | Company name                   |
| location    | TEXT      | Internship location(s)         |
| stipend     | TEXT      | Stipend amount                 |
| skills      | TEXT      | Required skills                |
| url         | TEXT      | Unique job listing URL         |
| created_at  | TIMESTAMP | Defaults to current timestamp  |
| email_sent  | INTEGER   | Defaults to 0 (reserved)       |

## Dependencies

- `requests` – HTTP requests to Internshala
- `beautifulsoup4` – HTML parsing
- `lxml` – fast HTML parser
- `pandas` – CSV export

## Notes

- The virtual environment (`.intersala/`) and `__pycache__/` are gitignored.
- Scraping respects a 2-second delay between page requests.
- A browser `User-Agent` header is used to avoid request blocking.