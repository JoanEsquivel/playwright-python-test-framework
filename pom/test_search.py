from pageObjects.SearchPage import SearchPage
from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    search_page = SearchPage(page)
    search_page.navigate()
    search_page.search("search query")
    page.screenshot(path="example.png")
    print(page.title())
    browser.close()
    

