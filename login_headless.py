# login_and_save_cookies.py
import asyncio
from playwright.async_api import async_playwright
import json
import os


with open('creds') as file:
    lines = file.readlines()
    username = lines[0].strip()
    password = lines[1].strip()
    email = lines[2].strip()

EMAIL = email
PASSWORD = password
COOKIE_PATH = "cookies.json"

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context()
        page = await context.new_page()

        await page.goto("https://www.myfitnesspal.com/account/login")

        await page.fill('input[name="username"]', EMAIL)
        await page.fill('input[name="password"]', PASSWORD)
        await page.click('button[type="submit"]')

        # Wait until logged in or redirected to dashboard
        await page.wait_for_url("**/dashboard", timeout=15000)

        cookies = await context.cookies()
        with open(COOKIE_PATH, "w") as f:
            json.dump(cookies, f)

        await browser.close()

asyncio.run(main())
