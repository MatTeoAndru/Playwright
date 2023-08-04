#https://github.com/microsoft/playwright-pytest/blob/main/.github/workflows/python-publish.yml 
from playwright.async_api import Page, expect, async_playwright
import re
import pytest
from variable import BASE_URL
import asyncio

# Define a pytest fixture to provide test parameters
#@pytest.fixture(params=["firefox", "chromium", "webkit" , "msedge"])
@pytest.fixture(params=["firefox", "chromium", "webkit"])
def browser_type(request):
    return request.param



# Updated test_login function to use the Playwright Async API
@pytest.mark.asyncio
async def test_login(browser_type: str):
    async with async_playwright() as playwright:
        if browser_type == "firefox":
            browser = await playwright.firefox.launch(headless=True)
        elif browser_type == "chromium":
            browser = await playwright.chromium.launch(headless=True)
        elif browser_type == "msedge":
            browser = await playwright.webkit.launch(headless=True)
        else:
            browser = await playwright.chromium.launch(channel="msedge" , headless=True)

                
        context = await browser.new_context()

        await context.tracing.start(screenshots=True, snapshots=True, sources=True)


        page = await context.new_page()



        await page.goto(BASE_URL)
        await page.get_by_role("button", name=" Impostazioni").click(timeout=10000)
        await page.get_by_role("button", name=" Aggiungi un nuovo server").click(timeout=3000)
        await page.locator("label").filter(has_text="Installazione live").click(timeout=3000)
        await page.get_by_placeholder("Nome").click(timeout=3000)
        await page.get_by_placeholder("Nome").fill("")
        await page.get_by_placeholder("Dominio").click(timeout=3000)
        await page.get_by_placeholder("Dominio").fill("")
        await page.locator("div").filter(has_text=re.compile(r"^Azienda \*$")).nth(3).click(timeout=3000)
        await page.get_by_placeholder("Azienda").fill("")
        await page.get_by_role("button", name=" Salva e torna indietro").click(timeout=3000)
        await page.get_by_role("button", name=" Indietro").click(timeout=3000)
        await page.get_by_placeholder("Username").click(timeout=3000)
        await page.get_by_placeholder("Username").fill("")
        await page.get_by_placeholder("Password").click(timeout=3000)
        await page.get_by_placeholder("Password").fill("")
        await page.locator("div").filter(has_text=re.compile(r"^Welcome server \*$")).nth(2).click(timeout=3000)
        await page.get_by_text("").click(timeout=3000)
        await page.get_by_role("button", name=" Login").click(timeout=3000)
        
        
        await context.tracing.stop(path = "traceLogin.zip")



        try:
            await expect(page).not_to_have_url( "",timeout=3000)
            print(f"Login test passed! on {browser_type} browser")
        except Exception as e:
            pytest.fail(f"Login test failed on {browser_type} browser: {e}")
        finally:
            await context.close()




# Add the following block to invoke the test function
# if __name__ == "__main__":
#     test_login(browser_type="firefox")
#     test_login(browser_type="chromium")
#     test_login(browser_type="webkit")
