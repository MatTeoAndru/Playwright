#https://calmcode.io/playwright/codegen.html

from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://calmcode.io/")
    page.get_by_role("link", name="ngrok", exact=True).click()
    page.get_by_role("link", name="3. Installation").click()
    page.get_by_role("link", name="5. Configuration").click()
    page.locator("pre").filter(has_text="authtoken: <YOUR TOKEN> tunnels: streamlit: addr: 8501 proto: http auth: \"vincen").click()

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)
