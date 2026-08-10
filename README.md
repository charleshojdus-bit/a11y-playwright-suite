# A11y Playwright Suite

Automated accessibility (a11y) testing suite built with **Python, Playwright, pytest, and axe-core-python**, targeting [Deque's Mars Commuter demo site](https://dequeuniversity.com/demo/mars/) — a site intentionally built with accessibility violations for testing purposes.

This is the third project in a QA automation portfolio, following:
1. Selenium/Python/pytest suite (Sauce Demo e-commerce site) with GitHub Actions CI
2. Playwright test suite (in progress)

## Purpose

Demonstrate automated accessibility testing skills: integrating axe-core with Playwright, interpreting WCAG violation reports, and building a reusable a11y test suite.

## Tech Stack

- Python
- Playwright
- pytest / pytest-playwright
- axe-core-python

## Setup

```bash
python -m venv venv
venv\Scripts\activate      # Windows PowerShell
pip install -r requirements.txt
playwright install
```

## Running Tests

```bash
pytest
```

## Project Status

🔄 In progress — currently building out core test flow against the Mars Commuter demo site and validating axe-core violation detection.

## Notes / Learnings

- Confirmed correct target URL is `/demo/mars/` (not `/demo/mars/1`, which redirects to a Deque 404 page — an accessible page that returns 0 false-negative violations if scanned by mistake).
