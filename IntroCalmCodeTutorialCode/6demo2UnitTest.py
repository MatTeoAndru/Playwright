#Unit test per controllare che un'immagine sia presente nella pagina
#Possiamo farlo usando il pick locator rimuovendo la funzione del .click() ed assegnandola ad una variabile come riga 31


from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://calmcode.io/")
    page.get_by_role("button", name="More").click()
    page.locator("#dropdown-button-1").get_by_role("link", name="Datasets").click()
    page.get_by_role("row", name="bigmac logo bigmac.csv An economic indicator? csv 1331 71KB Detailed Info").get_by_role("link", name="Detailed Info").click()
    page.get_by_role("button", name="Explore bigmac.csv").click()
    #utility scritta a mano , non è possibile registrarla . Timeout di default della libreria a 5000 
    expect(page).to_have_url("https://calmcode-datasette.fly.dev/calmcode/bigmac", timeout=1000) and expect(page).not_to_have_url("calmcode.io" , timeout = 1000)




def test_navigation_img_and_link(page: Page) -> None:
    page.goto("https://calmcode.io/")

    # Use img to navigate
    page.locator(".flex-grow").click()
    page.get_by_role("link", name="args kwargs logo").click()
    img_elem = page.get_by_role("img", name="Calmcode -")
    expect(img_elem).to_be_visible()

    # Use link to navigate
    page.goto("https://calmcode.io/")
    page.get_by_role("link", name="args kwargs", exact=True).click()
    img_elem = page.get_by_role("img", name="Calmcode -")
    expect(img_elem).to_be_visible()

