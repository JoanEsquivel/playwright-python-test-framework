
#Extracted from: https://playwright.dev/python/docs/api/class-apirequestcontext#api-request-context-get

import asyncio
from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    # This will launch a new browser, create a context and page. When making HTTP
    # requests with the internal APIRequestContext (e.g. `context.request` or `page.request`)
    # it will automatically set the cookies to the browser page and vise versa.
    # browser = await playwright.chromium.launch()
    # context = await browser.new_context(base_url="https://api.github.com")
    # api_request_context = context.request
    # page = await context.new_page()

    # Alternatively you can create a APIRequestContext manually without having a browser context attached:
    api_request_context = await playwright.request.new_context(base_url="http://localhost:3000")
    data = {
        "completed": False,
        "title": "test",
        "id": "500",
    }

    # Create a repository.
    response = await api_request_context.post(
        "/todos",
        data=data,
    )
    assert response.ok
    print(f"todo Var: {response}")

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())