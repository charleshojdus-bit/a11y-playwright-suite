from playwright.sync_api import Page
from axe_core_python.sync_playwright import Axe

def test_axe_scan_mars_commuter(page: Page):
    page.goto("https://dequeuniversity.com/demo/mars/")
    page.wait_for_load_state("networkidle")
    page.screenshot(path="debug_screenshot.png")

    axe = Axe()
    results = axe.run(page)

    violations = results["violations"]
    print(f"\n{len(violations)} violations found\n")

    for v in violations:
        
        print(f"- [{v['impact']}] {v['id']}: {v['description']}")

        print("Result Keys:", results.keys())