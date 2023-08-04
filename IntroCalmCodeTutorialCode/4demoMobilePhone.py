#https://calmcode.io/playwright/codegen-settings.html

# Emulate screen size and color scheme.
#playwright codegen --viewport-size=800,600 --color-scheme=dark <url>


from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.webkit.launch(headless=False)
    context = browser.new_context(**playwright.devices["iPhone 11"])
    page = context.new_page()
    page.goto("https://calmcode.io/")
    page.get_by_role("link", name="ngrok", exact=True).click()
    page.get_by_role("link", name="3").click()
    page.get_by_role("link", name="5").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)



