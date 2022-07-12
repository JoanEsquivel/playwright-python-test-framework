#to run this: python3 inputs/radio-button.py
import asyncio
from playwright.async_api import async_playwright, expect

async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        page = await browser.new_page()
        await page.set_viewport_size({"width": 1800, "height": 1200})
        await page.goto("https://demoqa.com/select-menu")
        #-Actions
        await page.select_option('select#cars', ['volvo', 'saab', 'audi'])
        await page.screenshot(path="example.png")
        #-Closing browser
        await browser.close()

asyncio.run(main())