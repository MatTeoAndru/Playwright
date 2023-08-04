# https://calmcode.io/playwright/first-demo.html

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # Load the Chrome browser and see it
    # Set headless true/false per vedere interazione browser con azione
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://calmcode.io")
    # Grab the title
    print(page.title())
    # Make a screenshot
    page.screenshot(path="example.png")
    
    

    browser.close()


