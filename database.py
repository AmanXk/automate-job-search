import sqlite3
DB_NAME = "internships.db"

def create_table():
    conn = sqlite3.connect(DB_NAME)

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS internships (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            company TEXT,
            location TEXT,
            stipend TEXT,
            skills TEXT,
            url TEXT UNIQUE,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
            email_sent INTEGER DEFAULT 0
        )
    """)

    conn.commit()
    conn.close()


def is_new_job(job):
    """
    Returns True if internship doesn't already exist.
    """

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT id FROM internships WHERE url = ?",
        (job["url"],)
    )

    result = cursor.fetchone()
    conn.close()
    return result is None


def save_job(job):
    """
    Save a new internship into database.
    """

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT OR IGNORE INTO internships
        (title, company, location, stipend, skills, url)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        job["title"],
        job["company"],
        job["location"],
        job["stipend"],
        job["skills"],
        job["url"]
    ))
    conn.commit()
    conn.close()
