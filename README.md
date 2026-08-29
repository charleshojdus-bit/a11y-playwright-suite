# A11y Playwright Suite
![CI](https://github.com/charleshojdus-bit/a11y-playwright-suite/actions/workflows/ci.yml/badge.svg)

Automated accessibility (a11y) testing suite built with Python, Playwright, pytest, and axe-core-python, targeting Deque's Mars Commuter demo site — a site intentionally built with accessibility violations for testing purposes.

This is the third project in a QA automation portfolio, following:
- Selenium/Python/pytest suite (Sauce Demo e-commerce site) with GitHub Actions CI
- Playwright test suite (in progress)

## Purpose
Demonstrate automated accessibility testing skills: integrating axe-core with Playwright, interpreting WCAG violation reports, and building a reusable a11y test suite.

## Tech Stack
- Python
- Playwright
- pytest / pytest-playwright
- axe-core-python
- GitHub Actions (CI)

## Setup
python -m venv venv
venv\Scripts\activate      # Windows PowerShell
pip install -r requirements.txt
playwright install

## Running Tests
pytest

## Project Status
✅ Core suite complete — four tests validate known Mars Commuter violations split by axe-core impact severity (critical, serious, moderate, minor), using a shared pytest fixture for scan setup. CI runs the full suite on every push via GitHub Actions.

## Notes / Learnings
- Confirmed correct target URL is /demo/mars/ (not /demo/mars/1, which redirects to a Deque 404 page — an accessible page that returns 0 false-negative violations if scanned by mistake).
- A test with no assertion (only print statements) will always pass regardless of what axe-core finds — an early lesson in this project.
