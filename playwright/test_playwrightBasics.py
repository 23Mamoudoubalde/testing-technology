from playwright.sync_api import Page, Playwright


def test_playwrightBasics(playwright):
    browser = playwright.chromium.launch(headless= False)
    context = browser.new_context() # is like new cookies, cache and all 
    page = context.new_page()
    page.goto("https://rahulshettyacademy.com")

#page has an assumption that you would be using chromiminum as the previous assignment was it. if new then define a new page.
def test_playwrightShortcut(page:Page):
    page.goto("https://google.com")

