# Contributing to Scrape-ML

Thank you for considering contributing to Scrape-ML! We welcome all types of contributions—bug reports, feature suggestions, documentation improvements, and code contributions. To make the process smooth, please follow the guidelines below.

## Table of Contents
1. [Code of Conduct](https://github.com/recodehive/Scrape-ML/blob/main/CODE_OF_CONDUCT.md)
2. [How to Contribute](#how-to-contribute)
    - [Reporting Bugs](#reporting-bugs)
    - [Suggesting Enhancements](#suggesting-enhancements)
    - [Submitting Code Changes](#submitting-code-changes)
3. [Pull Request Process](#pull-request-process)
4. [Development Environment Setup](#development-environment-setup)

## Code of Conduct
By participating in this project, you agree to uphold our [Code of Conduct](CODE_OF_CONDUCT.md). Please ensure that your contributions are respectful and considerate of others.

## How to Contribute

### Reporting Bugs
If you find a bug, please open an issue in our repository. When reporting a bug, provide as much detail as possible, including:
- The version of Python you’re using.
- Steps to reproduce the issue.
- Screenshots or error logs, if available.

### Suggesting Enhancements
We are open to feature suggestions and improvements! If you have an idea for enhancing the project, please open an issue with:
- A clear and concise description of the suggested feature.
- How it would be beneficial to the project.
- Any potential implementation details you have in mind.

### Submitting Code Changes

1. **Fork the repository:**
   - Click the "Fork" button in the top right corner of the repository page on GitHub.

2. **Clone the forked repository locally:**
```sh
   git clone https://github.com/your-username/Scrape-ML.git
   cd scrape-ml
```
4. **Create a new branch for your changes:**

```sh
git checkout -b your-feature-branch
```

5. **Make your changes:**
   
* Ensure code quality and update documentation as necessary.

6.  **Test your changes thoroughly:**

* Run existing tests and verify that everything works as expected.

7. **Commit your changes with a descriptive message:**

```sh
git add .
git commit -m "Add a brief description of the changes made"
```

8. **Push to your fork and submit a pull request:**

```sh
git push origin your-feature-branch
```
9. **Go to the original repository on GitHub and click on "New Pull Request."**

* Select your branch from the dropdown and create the pull request.

## Pull Request Process
- Ensure your code follows the existing code style.
- Update documentation as needed.
- Verify that all existing tests pass and write new tests for new features.
- Mention the issue your pull request addresses (if applicable).

## Development Environment Setup

To contribute to Scrape-ML, follow these steps to set up your development environment:

### Prerequisites
- Python 3.7 or higher
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests](https://docs.python-requests.org/en/latest/)
- Jupyter Notebook

### Setup Instructions
1. Clone the repository:
    ```sh
    git clone https://github.com/your-username/scrape-ml.git
    ```
2. Create and activate a virtual environment:
    ```sh
    python -m venv env
    source env/bin/activate  # For Linux/macOS
    .\env\Scripts\activate  # For Windows
    ```
3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```
4. Launch Jupyter Notebook to start contributing:
    ```sh
    jupyter notebook
    ```

## Additional Guidelines
- Make sure to follow clean coding practices.
- Add comments wherever necessary for better code understanding.
- If you are adding new functionality, update the documentation in the README.

We are excited to see your contributions and collaborate with you!
