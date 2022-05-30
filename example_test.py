#to run this, just: pytest -> https://playwright.dev/python/docs/test-runners
#pytest --headed
#pytest --browser chromium --browser webkit
#pytest --base-url https://www.saucedemo.com/ --browser chromium --headed
def test_example_is_working(page):
    page.goto("/")
    assert page.inner_text('title') == 'Swag Labs'
    