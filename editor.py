# https://playwright.dev/python/docs/auth#reuse-authentication-state
# https://jadala-ajay16.medium.com/why-do-we-write-await-async-in-playwright-javascript-typescript-fa3c92f82841#:~:text=Synchronous%20%3A%20your%20program%20will%20execute,even%20before%20the%20first%20line.

from playwright.async_api import Page, expect, async_playwright
import re
import pytest
from variable import BASE_URL
import asyncio


# Define a pytest fixture to provide test parameters
@pytest.fixture(params=["firefox", "chromium", "webkit"])
#(params=["firefox", "chromium", "webkit" , "msedge"])
def browser_type(request):
    return request.param


# Updated test_login function to use the Playwright Async API
@pytest.mark.asyncio
async def test_editor(browser_type: str):
    async with async_playwright() as playwright:
        if browser_type == "firefox":
            browser = await playwright.firefox.launch(headless=False)
        elif browser_type == "chromium":
            browser = await playwright.chromium.launch(headless=False)
        elif browser_type == "webkit":
            browser = await playwright.webkit.launch(headless=False)
        # else:
        #     browser = await playwright.chromium.launch(channel="msedge" , headless=True)
        
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
        
        #FINE LOGIN , INIZIO EDITOR
        await page.get_by_label("Passepartout Welcome").get_by_role("button", name=" Chiudi").click()
        
        await page.get_by_text("Cambio turno memo").click()
        await page.locator("div").filter(has_text=re.compile(r"^Chiudi$")).click()
        await page.get_by_role("button", name=" Chiudi").click()

        await page.get_by_placeholder("Cerca funzionalità").click()
        await page.get_by_placeholder("Cerca funzionalità").press("CapsLock")
        await page.get_by_placeholder("Cerca funzionalità").fill("C")
        await page.get_by_placeholder("Cerca funzionalità").press("CapsLock")
        await page.get_by_placeholder("Cerca funzionalità").fill("Configura ")
        await page.get_by_placeholder("Cerca funzionalità").press("CapsLock")
        await page.get_by_placeholder("Cerca funzionalità").fill("Configura P")
        await page.get_by_placeholder("Cerca funzionalità").press("CapsLock")
        await page.get_by_placeholder("Cerca funzionalità").fill("Configura Piatti")
        await page.get_by_placeholder("Cerca funzionalità").press("Enter")
        await page.get_by_role("link", name="Configura piatti").click()
        await page.get_by_role("button", name="").click()
        await page.get_by_role("textbox", name="Descrizione").click()
        await page.get_by_role("textbox", name="Descrizione").press("CapsLock")
        await page.get_by_role("textbox", name="Descrizione").fill("M")
        await page.get_by_role("textbox", name="Descrizione").press("CapsLock")
        await page.get_by_role("textbox", name="Descrizione").fill("53211alfredo")
        await page.locator("#app-view-select-1").get_by_role("link").click()
        await page.locator("#mat-dialog-2").get_by_text("Antipasti").click()
        await page.get_by_label("Prezzo").click()
        await page.get_by_label("Prezzo").fill("11")
        await page.get_by_label("Quantità massima per persona").click()
        await page.get_by_label("Quantità massima per persona").fill("2")
        await page.locator(".mat-checkbox-inner-container").first.click()
        await page.locator("#div-scroller-route div").filter(has_text="Variazione").nth(3).click()
        await page.get_by_role("button", name="Salva").click()
        await page.locator("#mat-input-24").click()
        await page.locator("#mat-input-24").press("Tab")
        await page.locator("#mat-input-25").press("Tab")
        await page.locator("#mat-input-26").press("Tab")
        await page.locator("#mat-input-27").press("Tab")
        await page.locator("#mat-input-28").press("Tab")
        await page.locator("#mat-input-29").press("Tab")
        await page.locator("#mat-input-30").press("Tab")
        await page.locator("#mat-input-31").press("Tab")
        await page.get_by_role("button", name="Annulla").press("Tab")
        await page.get_by_role("button", name="Elimina").press("Tab")
        await page.get_by_role("button", name="Salva").click()
        await page.locator("div").filter(has_text=re.compile(r"^DescrizioneCategoria$")).first.click()
        await page.get_by_label("Descrizione").click()
        await page.get_by_label("Descrizione").fill("53211alfredo")
        
        await page.get_by_label("Descrizione").press("Enter")
        await page.get_by_role("columnheader", name="Descrizione").click()


        await page.get_by_role("button", name="edit").first.click()
        await page.locator("#mat-input-35").click()
        await page.locator("#mat-input-35").press("Tab")
        await page.locator("#mat-input-36").press("Tab")
        await page.locator("#mat-input-37").press("Tab")
        await page.locator("#mat-input-38").press("Tab")
        await page.locator("#mat-input-39").press("Tab")
        await page.locator("#mat-input-40").press("Tab")
        await page.locator("#mat-input-41").press("Tab")
        await page.locator("#mat-input-42").press("Tab")
        await page.get_by_role("button", name="Annulla").press("Tab")
        await page.get_by_role("button", name="Elimina").click()
            
            
            
            




        #CONTROLLARE che non ci siano item restituiti

        #await expect(page.locator('h1[role="heading"][innerText="Nessun piatto trovato"]')).to_be_visible() 

        #element = page.locator('heading', name='Nessun piatto trovato')


        #elementAdded = await page.query_selector('h1[role="heading"][innerText="Nessun piatto trovato"]')


        #get_by_role("heading", name="Nessun piatto trovato")

        await page.get_by_role("heading", name="Nessun piatto trovato").click()

        
        await context.tracing.stop(path = "traceEditor.zip")

        try:
            
            await expect(page).to_have_url( "",timeout=3000) 
            
            print(f"Editor test passed! on {browser_type} browser")
        except Exception as e:
                pytest.fail(f"Editor menu  failed on {browser_type} browser: {e}")
        finally:
                await context.close()
