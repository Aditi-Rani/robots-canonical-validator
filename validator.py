import requests
from bs4 import BeautifulSoup

def check_robots_txt(url):
    try:
        robots_url = url.rstrip("/") + "/robots.txt"
        response = requests.get(robots_url)
        if response.status_code == 200:
            print("✅ robots.txt found and fetched")
            print(response.text[:500] + "\n...")  # show first 500 chars
        else:
            print("❌ robots.txt not found")
    except Exception as e:
        print(f"❌ Error fetching robots.txt: {e}")

def check_canonical_tag(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        canonical = soup.find("link", rel="canonical")
        if canonical and canonical.get("href"):
            print(f"✅ Canonical tag found: {canonical.get('href')}")
        else:
            print("❌ Canonical tag not found")
    except Exception as e:
        print(f"❌ Error checking canonical tag: {e}")

if __name__ == "__main__":
    site_url = input("Enter the website URL (e.g., https://example.com): ").strip()
    check_robots_txt(site_url)
    check_canonical_tag(site_url)
