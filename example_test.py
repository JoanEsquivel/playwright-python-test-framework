#to run this, just: pytest -> https://playwright.dev/python/docs/test-runners
#pytest --headed
#pytest --browser chromium --browser webkit
#pytest --base-url https://www.saucedemo.com/ --browser chromium --headed

#Configure Mypy typings for auto-completion
from playwright.sync_api import Page

def test_example_is_working(page: Page):
    page.goto("/")
    assert page.inner_text('title') == 'Swag Labs'
    