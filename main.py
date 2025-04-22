import myfitnesspal
import requests
import json
from datetime import datetime



with open('creds') as file:
    lines = file.readlines()
    username = lines[0].strip()
    password = lines[1].strip()

COOKIE_PATH = "cookies.json"

def load_cookies(path):
    with open(path, "r") as f:
        cookie_data = json.load(f)
    return {cookie["name"]: cookie["value"] for cookie in cookie_data}

def fetch_nutrition_data():
    cookies = load_cookies(COOKIE_PATH)

    today = datetime.today().strftime("%Y-%m-%d")
    url = f"https://www.myfitnesspal.com/reports/printable_diary?from={today}&to={today}"

    headers = {
        "User-Agent": "Mozilla/5.0",
        "Accept-Language": "en-US",
    }

    res = requests.get(url, headers=headers, cookies=cookies)
    if res.status_code != 200:
        print("Failed to fetch diary page")
        print(res.text)
        return

    html = res.text

    # Simple scrape (for example purposes)
    # You might use BeautifulSoup or regex to pull out actual calorie/protein totals

    print("Fetched diary page — ready to parse!")


fetch_nutrition_data()
