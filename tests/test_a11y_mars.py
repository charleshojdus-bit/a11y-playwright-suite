from playwright.sync_api import Page
from axe_core_python.sync_playwright import Axe


def test_critical_violation_detected(violations):
    
    expected_ids = {"image-alt", "button-name", "duplicate-id-aria",
    "select-name"}
    critical_ids = [v["id"] for v in violations if v["impact"] == "critical"]

    for v in violations:
        
        print(f"- [{v['impact']}] {v['id']}: {v['description']}")
        
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
        
    
   