# QA Automation Framework

Pet project for API and UI test automation.

## Tech Stack

- Python 3.11
- PyTest
- Playwright (in progress)
- Docker + PostgreSQL
- GitHub Actions (CI/CD)
- Allure

## How to run

### 1. Clone repo

````
bash
git clone https://github.com/antonlahunou/beautiful_framework.git
cd beautiful_framework
````

### 2. Install dependencies
```bash
pip install -r requirements.txt
```
### 3. Set .env file
Create .env file:
````
text
ACCESS_TOKEN=your_gorest_token
BASE_URL=https://gorest.co.in/public/v2
````
### 4. Start PostgreSQL (optional)
````
bash
docker-compose up -d
````
### 5. Run tests
````
bash
pytest tests/ -v
````
### 6. Allure report
````
bash
pytest tests/ --alluredir=allure-results
allure serve allure-results
````
CI/CD
GitHub Actions runs tests on every push.

Status: https://github.com/antonlahunou/beautiful_framework/actions/workflows/run-tests.yml/badge.svg

### What's done
API tests for /users (CRUD)

Pydantic validation

Allure reports

GitHub Actions pipeline

PostgreSQL in Docker

### Next steps
API tests for /posts, /comments

Playwright UI tests

Integration tests with PostgreSQL

Better Allure reports

Contact
GitHub: antonlahunou

LinkedIn: https://www.linkedin.com/in/anton-lahunou/