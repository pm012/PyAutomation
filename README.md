1. Create environment: python3 -m venv pywebdriver
2. Activate environment: source pywebdriver/bin/activate
3. Install libraries: pip install -r requirements.txt
4. To run specificly marked tests (login) with report: pytest -m login --html=reports/report.html
5. To run all tests: pytest without report
6. To run tests in another browser: pytest -m login --html=reports/report.html --browser=firefox
7. To run tests in paralel (set number of paralel exec as n parameter - not more that number of cores in CPU): pytest -m login --html=reports/report.html -n=6

# PyAutomation

Sandbox WebDriver automation with Python programming language
