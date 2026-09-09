import requests
from bs4 import BeautifulSoup
import time

BASE_URL = "https://internshala.com/internships/artificial-intelligence-ai-internship/page-{}/"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36"}

def scrape_internshala():
    jobs = []
    for page in range(1, 4):
        url = BASE_URL.format(page)
        print(f"Scraping page {page}...")
        try:
            response = requests.get(url, headers=HEADERS, timeout=20)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Error: {e}")
            continue

        soup = BeautifulSoup(response.text, "lxml")
        cards = soup.find_all("div", class_="individual_internship")
        print(f"Found {len(cards)} jobs")

        for card in cards:
            title_tag = card.find("a", class_="job-title-href")
            company_tag = card.find("p", class_="company-name")
            location_tag = card.find("div", class_="row-1-item locations")
            stipend_tag = card.find("span", class_="stipend")
            skills_tag = card.find("div", class_="job_skills")

            title = title_tag.get_text(" ", strip=True) if title_tag else ""
            company = company_tag.get_text(" ", strip=True) if company_tag else ""
            location = location_tag.get_text(" ", strip=True) if location_tag else ""
            stipend = stipend_tag.get_text(" ", strip=True) if stipend_tag else ""
            skills = skills_tag.get_text(" ", strip=True) if skills_tag else ""

            link = title_tag.get("href", "") if title_tag else ""
            if link.startswith("/"):
                link = "https://internshala.com" + link

            jobs.append({
                "title": title,
                "company": company,
                "location": location,
                "stipend": stipend,
                "skills": skills,
                "url": link
            })

        time.sleep(2)

    return jobs
