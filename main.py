from scraper import scrape_internshala
from database import create_table, is_new_job, save_job

def main():
    print("Starting Internshala monitor...")
    create_table()
    jobs = scrape_internshala()
    print(f"\nTotal jobs scraped: {len(jobs)}")
    new_jobs = []

    for job in jobs:
        if is_new_job(job):
            print(f"NEW JOB: {job['title']} | {job['company']}")
            save_job(job)
            new_jobs.append(job)
        else:
            print(f"Already exists: {job['title']}")

    print("\n" + "=" * 60)
    print(f"New internships found: {len(new_jobs)}")
    print("=" * 60)

if __name__ == "__main__":
    main()
