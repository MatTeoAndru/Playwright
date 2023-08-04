#per generare codice dalla nostra esecuzione usiamo il comando
#playwright codegen https://calmcode.io

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://calmcode.io")
    # Assert the title
    if page.title() == "Code. Simply. Clearly. Calmly.":
        print("Yep! It works :)")
    browser.close()
