#pytest .\7demoDebugging.py::test_path_to_datasette
# This will only run that one test. But we can also go a step further and run the test in headed mode. 
# This way, the browser will start up and we'll be able to see what is happening.

# pytest test_e2e.py::test_path_to_datasette --headed
# This might be too fast for comfort though, so let's slow down each step with the --slowmo flag.

# pytest test_e2e.py::test_path_to_datasette --headed --slowmo 1500



from playwright.sync_api import Page, expect


def test_path_to_datasette(page: Page) -> None:
    page.goto("https://calmcode.io/")
    page.get_by_role("button", name="More").click()
    page.locator("#dropdown-button-1").get_by_role("link", name="Datasets").click()
    page.get_by_role("row", name="bigmac logo bigmac.csv An economic indicator? csv 1331 71KB Detailed Info").get_by_role("link", name="Detailed Info").click()
    page.get_by_role("button", name="Explore bigmac.csv").click()
    #riga con errore
    expect(page).to_have_url("https://calmcode-datasette.fly.dev/calmcode/bigmacs", timeout=1000)


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
