import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
BASE_URL = (
    "https://internshala.com/"
    "internships/artificial-intelligence-ai-internship/page-{}/"
)

HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/140.0.0.0 Safari/537.36"
    )
}

jobs = []

for page in range(1, 4):
    url = BASE_URL.format(page)
    print(f"\nScraping page {page}...")
    print(url)
    try:
        response = requests.get(url,headers=HEADERS,timeout=20)
        response.raise_for_status()

    except requests.RequestException as e:
        print(f"Error scraping page {page}: {e}")
        continue
    soup = BeautifulSoup(response.text, "lxml")
    cards = soup.find_all("div",class_="individual_internship")
    print(f"Found {len(cards)} internship cards")

    for card in cards:

        title = ""
        company = ""
        location = ""
        stipend = ""
        skills = ""
        link = ""
        title_tag = card.find("a",class_="job-title-href")

        if title_tag:
            title = title_tag.get_text(
                " ",
                strip=True
            )
        company_tag = card.find("p",class_="company-name")
        if company_tag:
            company = company_tag.get_text(" ",strip=True)

        # location

        location_tag = card.find("div",class_="row-1-item locations")
        if location_tag:
            location = location_tag.get_text(" ",strip=True)

        # stepend

        stipend_tag = card.find("span",class_="stipend")

        if stipend_tag:
            stipend = stipend_tag.get_text(" ",strip=True)

        # skills

        skills_tag = card.find(
            "div",
            class_="job_skills"
        )

        if skills_tag:
            skills = skills_tag.get_text(
                " ",
                strip=True
            )
        if title_tag and title_tag.get("href"):

            link = title_tag["href"]

            # Convert relative URL → absolute URL
            if link.startswith("/"):
                link = "https://internshala.com" + link

        # create a object job
        job = {
            "title": title,
            "company": company,
            "location": location,
            "stipend": stipend,
            "skills": skills,
            "url": link
        }


        # Add to jobs list
        jobs.append(job)
    time.sleep(2)

df = pd.DataFrame(jobs)

df.drop_duplicates(
    subset=["url"],
    inplace=True
)

print("\n" + "=" * 80)
print("TOTAL INTERNSHIPS:", len(df))
print("=" * 80)
print(df.to_string(index=False))

# save to pdf

df.to_csv(
    "internshala_ai_internships.csv",
    index=False
)

print("\nCSV saved successfully!")
