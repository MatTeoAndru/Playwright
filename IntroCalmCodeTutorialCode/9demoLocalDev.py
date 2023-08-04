#Local dev server <------------- test
# py test base url plugin per local dev

#python -m pip install pytest-base-url
# pytest playwright/test_e2e.py --base-url http://localhost:5000


from playwright.sync_api import Page, expect


def test_path_to_datasette(page: Page) -> None:
    page.goto("/")
    page.get_by_role("button", name="More").click()
    page.locator("#dropdown-button-1").get_by_role("link", name="Datasets").click()
    page.get_by_role("row", name="bigmac logo bigmac.csv An economic indicator? csv 1331 71KB Detailed Info").get_by_role("link", name="Detailed Info").click()
    page.get_by_role("button", name="Explore bigmac.csv").click()
    expect(page).to_have_url("https://calmcode-datasette.fly.dev/calmcode/bigmac", timeout=1000)


def test_navigation_img_and_link(page: Page) -> None:
    page.goto("/")

    # Use img to navigate
    page.locator(".flex-grow").click()
    page.get_by_role("link", name="args kwargs logo").click()
    img_elem = page.get_by_role("img", name="Calmcode -")
    expect(img_elem).to_be_visible()

    # Use link to navigate
    page.goto("/")
    page.get_by_role("link", name="args kwargs", exact=True).click()
    img_elem = page.get_by_role("img", name="Calmcode -")
    expect(img_elem).to_be_visible()


def test_search(page: Page) -> None:
    page.goto("/")
    page.get_by_role("link", name="Search").click()
    page.get_by_placeholder("Search calmcode content").click()
    page.get_by_placeholder("Search calmcode content").fill("pur")
    page.get_by_placeholder("Search calmcode content").press("Enter")
    page.get_by_role("link", name="pur.py").click(timeout=1000)
    page.get_by_text("pur.py").click()
