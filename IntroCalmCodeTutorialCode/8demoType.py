#A volte il codice generato da codegen può fallire
# sostituiamo il fill un text field con un .type
# There are pros and cons here. On one hand the typing action feels nicer because it mimics the user more closely.
# However, the delay of typing will also make the test a fair bit slower.

from playwright.sync_api import Page, expect

# OLD CODE
# def test_search(page: Page) -> None:
#     page.goto("/")
#     page.get_by_role("link", name="Search").click()
#     page.get_by_placeholder("Search calmcode content").click()
#     page.get_by_placeholder("Search calmcode content").fill("pur")
#     page.get_by_role("link", name="pur.py").click(timeout=1000)
#     page.get_by_text("pur.py").click()


#Solution 1

def test_search(page: Page) -> None:
    page.goto("/")
    page.get_by_role("link", name="Search").click()
    page.get_by_placeholder("Search calmcode content").click()
    page.get_by_placeholder("Search calmcode content").fill("pur")
    page.get_by_placeholder("Search calmcode content").press("Enter")
    page.get_by_role("link", name="pur.py").click(timeout=1000)
    page.get_by_text("pur.py").click()


#Solution 2

def test_search2(page: Page) -> None:
    page.goto("/")
    page.get_by_role("link", name="Search").click()
    page.get_by_placeholder("Search calmcode content").click()
    page.get_by_placeholder("Search calmcode content").type("pur", delay=150)
    page.get_by_role("link", name="pur.py").click(timeout=1000)
    page.get_by_text("pur.py").click()
