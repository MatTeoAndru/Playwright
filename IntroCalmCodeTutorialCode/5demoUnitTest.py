#https://calmcode.io/playwright/playwright-in-pytest.html

#python -m pip install pytest-playwright
#dopo aver mandato playwright codegen per registrare gli step , possiamo utilizzare "Pytest" come output del codice
#per eseguire il tutto scriviamo pytest <nomefile.py>
#The output should look familiar to the one using script, it's just that right now the browser is running in the background on your behalf.

from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://calmcode.io/")
    page.get_by_role("button", name="More").click()
    page.locator("#dropdown-button-1").get_by_role("link", name="Datasets").click()
    page.get_by_role("row", name="bigmac logo bigmac.csv An economic indicator? csv 1331 71KB Detailed Info").get_by_role("link", name="Detailed Info").click()
    page.get_by_role("button", name="Explore bigmac.csv").click()
    #utility scritta a mano , non è possibile registrarla . Timeout di default della libreria a 5000 
    expect(page).to_have_url("https://calmcode-datasette.fly.dev/calmcode/bigmac", timeout=1000) and expect(page).not_to_have_url("calmcode.io" , timeout = 1000)

