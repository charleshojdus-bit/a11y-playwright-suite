from playwright.sync_api import Page
from axe_core_python.sync_playwright import Axe

<<<<<<< HEAD

def test_critical_violation_detected(violations):
    
    expected_ids = {"image-alt", "button-name", "duplicate-id-aria",
    "select-name"}
    critical_ids = [v["id"] for v in violations if v["impact"] == "critical"]
=======
def test_axe_scan_mars_commuter(page: Page):
    page.goto("https://dequeuniversity.com/demo/mars/")
    page.wait_for_load_state("networkidle")
    page.screenshot(path="debug_screenshot.png")

    axe = Axe()
    results = axe.run(page)

    violations = results["violations"]
    print(f"\n{len(violations)} violations found\n")
>>>>>>> d6738f3d65ba5d234001d00e507feea0fdc2c9ea

    for v in violations:
        
        print(f"- [{v['impact']}] {v['id']}: {v['description']}")
<<<<<<< HEAD
        
    assert expected_ids.issubset(set(critical_ids))

def test_serious_violations_detected(violations):
    
    expected_ids = {"color-contrast", "duplicate-id-active", "frame-title", 
    "html-has-lang", "link-name", "tabindex"}
    serious_ids = [v["id"] for v in violations if v["impact"] == "serious"]
    
    for v in violations:

        print(f"- [{v['impact']}] {v['id']}: {v['description']}")
        
    assert expected_ids.issubset(set(serious_ids))

def test_moderate_violations_detected(violations):

    expected_ids = {"landmark-unique", "region", "landmark-one-main"}
    moderate_ids = [v["id"] for v in violations if v["impact"] == "moderate"]

    for v in violations:

        print(f"- [{v['impact']}] {v['id']}: {v['description']}")
       
    assert expected_ids.issubset(set(moderate_ids))

def test_minor_violations_detected(violations):
    
    expected_ids = {"duplicate-id"}
    minor_ids = [v["id"] for v in violations if v["impact"] == "minor"]

    for v in violations:

        print(f"- [{v['impact']}] {v['id']}: {v['description']}")
        
    assert expected_ids.issubset(set(minor_ids))
        
    
   
=======

        print("Result Keys:", results.keys())
>>>>>>> d6738f3d65ba5d234001d00e507feea0fdc2c9ea
