
# Automated Testing Project using Selenium and Pytest

This project is an automated testing suite built with Selenium and Pytest, following the Page Object Model architecture. It aims to test the functionalities of the website [https://automationexercise.com/](https://automationexercise.com/) by executing specific test cases provided on the site.

## Test Cases Covered

The test cases covered in this project are:

1. Signup with wrong email
2. Registering a user
3. Logging in with the user
4. Signing up for subscriptions
5. Checkout with product before login
6. Checkout with product after login
7. Deleting Account

## Project Structure

The project follows the Page Object Model architecture, separating page classes from test classes for better maintainability and readability. The test data is stored in external JSON files, allowing for easy modification and scalability.

### Key Features

- Use of Pytest addoptions for browser selection and headless mode
- Use of Module Scope for ordering tests
- Utilization of external files for test data

## How to Run the Project

### Prerequisites

- Python 3.x installed
- Chrome, Firefox, or Edge browser installed (depending on your choice)
- Git installed (for cloning the repository)

### Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your-username/automated-testing-project.git
    ```

2. Navigate to the project directory:

    ```bash
    cd automated-testing-project
    ```

3. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Tests

To run the tests, use the following command:

```bash
pytest --browser_name=chrome --headless=true
```

Replace `chrome` with `firefox` or `edge` depending on the browser you want to test on. Set `headless` to `false` if you want to run the tests in non-headless mode.
You can also play around the test data in `Utils/data.json`

### Options

- `--browser_name`: Specify the browser to run the tests on (chrome, firefox, edge)
- `--headless`: Set to `true` to run tests in headless mode, `false` otherwise

## Contributors

- [Yash Gupta](https://github.com/YashGupta1510)

