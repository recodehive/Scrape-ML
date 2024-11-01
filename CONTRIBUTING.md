# Contributing to Scrape-ML 🎯

Thank you for considering contributing to Scrape-ML! We welcome all types of contributions—bug reports, feature suggestions, documentation improvements, and code contributions. To make the process smooth, please follow the guidelines below.

<br>

# Code of Conduct 📃

By participating in this project, you agree to uphold our [Code of Conduct](https://github.com/recodehive/Scrape-ML/blob/main/CODE_OF_CONDUCT.md). Please ensure that your contributions are respectful and considerate of others.

<br>

# <h1 align="center">Star our Repository ⭐</h1>

### <div align = "center" style = "display:flex; justify-content:space-evenly; gap:100px;" > [![Stars](https://img.shields.io/github/stars/recodehive/Scrape-ML?style=for-the-badge&logo=github)](https://github.com/recodehive/Scrape-ML/stargazers) [![Forks](https://img.shields.io/github/forks/recodehive/Scrape-ML?style=for-the-badge&logo=github)](https://github.com/recodehive/Scrape-ML/network/members) [![Issues](https://img.shields.io/github/issues/recodehive/Scrape-ML?style=for-the-badge&logo=github)](https://github.com/recodehive/Scrape-ML/issues) [![PRs Open](https://img.shields.io/github/issues-pr/recodehive/Scrape-ML?style=for-the-badge&logo=github)](https://github.com/recodehive/Scrape-ML/pulls) [![PRs Closed](https://img.shields.io/github/issues-pr-closed/recodehive/Scrape-ML?style=for-the-badge&logo=github&color=2cbe4e)](https://github.com/recodehive/Scrape-ML/pulls?q=is%3Apr+is%3Aclosed)</div>

<br>

# Table of Contents
1. [Code of Conduct](#code-of-conduct)
2. [Project Structure](#project-structure-)
3. [How to Contribute](#how-to-contribute)
    - [First Pull Request](#first-pull-request-)
    - [Alternate Method To Contribute](#alternatively-contribute-using-github-desktop-️)
    - [Pull Request Process](#pull-request-process-)
    - [Reporting Bugs](#reporting-bugs-)
    - [Suggesting Enhancements](#suggesting-enhancements-)
4. [Development Environment Setup](#development-environment-setup-)
5. [Help And Support](#for-help-and-support-)
6. [Good Coding Practices](#good-coding-practices-)

<br>

# Project Structure 📂

```bash
SCRAPE-ML/
├── .github/                                # GitHub-related configurations such as workflows, issue templates, etc
│   
├── .ipynb_checkpoints/                     # The movie review part is included here
│   
├── .vscode/                                # The settings.json file is included here
│   
├── IMDB/                                   # IMDB related trained files are here
│     
├── Movie Genre Classification/             # Movie genre classification file of python is included here
│   
├── Smart_select features/                  # Some .py files are included here
│   
├── Tesseract-OCR/                          # Some .html and .exe files are included here
│   
├── Web_app/                                # All the resources used in the web app are included here
│   
├── assets/                                 # All the assets like images in the project are included here
│   
├── backlog/                                # All the .ipynb files are included here
│   
├── data_scrapped                           # Some .csv files are included here
├──
├── .gitignore
├──
├── CODE_OF_CONDUCT.md                       # Some rules for the contributors
├──           
├── CONTRIBUTING.md                          # Instructions for the contributors
├──
├── LICENSE                                  # A permission to do something
├──
├── Learn.md
├──
├── Movie_review_imdb_scrapping.ipynb
├──
├── Movie_review_rotten_tomatoes.ipynb
├──
├── README.md                                 # Some instructions related to the project
├──
├── image-1.png
├──
├── image-2.png
├──
├── image.png
├──          
├── main.py                                    # The main python file of the project
├──
├── results.csv                                # The results containing file of the project
```

<br>

# How to Contribute 💪

## First Pull Request ✨

1. **Star this repository**
    Click on the top right corner marked as **Stars** at last.

2. **Fork this repository**
    Click on the top right corner marked as **Fork** at second last.

3. **Clone the forked repository**

```bash
git clone https://github.com/<your-github-username>/Scrape-ML.git
```
  
4. **Navigate to the project directory**

```bash
cd Scrape-ML
```

5. **Create a new branch**

```bash
git checkout -b <your_branch_name>
```

6. **To make changes**

```bash
git add .
```

7. **Now to commit**

```bash
git commit -m "add comment according to your changes or addition of features inside this"
```

8. **Push your local commits to the remote repository**

```bash
git push -u origin <your_branch_name>
```

9. **Create a Pull Request** 

10. **Congratulations! 🎉 you've made your contribution**

## Alternatively, contribute using GitHub Desktop 🖥️

1. **Open GitHub Desktop:**
  Launch GitHub Desktop and log in to your GitHub account if you haven't already.

2. **Clone the Repository:**
- If you haven't cloned the project repository yet, you can do so by clicking on the "File" menu and selecting "Clone Repository."
- Choose the project repository from the list of repositories on GitHub and clone it to your local machine.

3.**Switch to the Correct Branch:**
- Ensure you are on the branch that you want to submit a pull request for.
- If you need to switch branches, you can do so by clicking on the "Current Branch" dropdown menu and selecting the desired branch.

4. **Make Changes:**
- Make your changes to the code or files in the repository using your preferred code editor.

5. **Commit Changes:**
- In GitHub Desktop, you'll see a list of the files you've changed. Check the box next to each file you want to include in the commit.
- Enter a summary and description for your changes in the "Summary" and "Description" fields, respectively. Click the "Commit to <branch-name>" button to commit your changes to the local branch.

6. **Push Changes to GitHub:**
- After committing your changes, click the "Push origin" button in the top right corner of GitHub Desktop to push your changes to your forked repository on GitHub.

7. **Create a Pull Request:**
- Go to the GitHub website and navigate to your fork of the project repository.
- You should see a button to "Compare & pull request" between your fork and the original repository. Click on it.

8. **Review and Submit:**
- On the pull request page, review your changes and add any additional information, such as a title and description, that you want to include with your pull request.
- Once you're satisfied, click the "Create pull request" button to submit your pull request.

9. **Wait for Review:**
Your pull request will now be available for review by the project maintainers. They may provide feedback or ask for changes before merging your pull request into the main branch of the project repository.

## Pull Request Process 🚀
- Ensure your code follows the existing code style.
- Update documentation as needed.
- Verify that all existing tests pass and write new tests for new features.
- Mention the issue your pull request addresses (if applicable).

## Reporting Bugs 📌

If you find a bug, please open an issue in our repository. When reporting a bug, provide as much detail as possible, including:
- To open issue, go here :- [Issue](https://github.com/recodehive/Scrape-ML/issues/new/choose)
- Please kindly choose the appropriate template according to your issue.
- The version of Python you’re using.
- Steps to reproduce the issue.
- Screenshots or error logs, if available.

## Suggesting Enhancements 🌐

We are open to feature suggestions and improvements! If you have an idea for enhancing the project, please open an issue with:
- A clear and concise description of the suggested feature.
- How it would be beneficial to the project.
- Any potential implementation details you have in mind.

<br>

# Development Environment Setup 🔧

To contribute to Scrape-ML, follow these steps to set up your development environment:

## Prerequisites

- Python 3.7 or higher
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests](https://docs.python-requests.org/en/latest/)
- Jupyter Notebook

## Setup Instructions

1. Clone the repository:
   
    ```bash
    git clone https://github.com/your-username/Scrape-ML.git
    ```
    
3. Create and activate a virtual environment:
   
    ```bash
    python -m venv env
    ```
    
    ```bash
    .\env\Scripts\activate  # For Windows
    ```

    ```bash
    source env/bin/activate  # For Linux/macOS
    ```
    
4. Install the dependencies:
   
    ```bash
    pip install -r requirements.txt
    ```
    
6. Launch Jupyter Notebook to start contributing:
    ```bash
    jupyter notebook
    ```

<br>

# For Help And Support 💬

- Admin Github Profile:- [Sanjay Viswanathan](https://github.com/sanjay-kv)
- Contact :- [Topmate](https://topmate.io/sanjaykv/)

<br>

# Good Coding Practices 🧑‍💻

1. **Follow the Project's Code Style**

   - Maintain consistency with the existing code style (indentation, spacing, comments).
   - Use meaningful and descriptive names for variables, functions, and classes.
   - Keep functions short and focused on a single task.
   - Avoid hardcoding values; instead, use constants or configuration files when possible.

2. **Write Clear and Concise Comments**

   - Use comments to explain why you did something, not just what you did.
   - Avoid unnecessary comments that state the obvious.
   - Document complex logic and functions with brief explanations to help others understand your thought -process.

3. **Keep Code DRY (Don't Repeat Yourself)**

   - Avoid duplicating code. Reuse functions, methods, and components whenever possible.
   - If you find yourself copying and pasting code, consider creating a new function or component.

4. **Write Tests**

   - Write unit tests for your functions and components.
   - Ensure your tests cover both expected outcomes and edge cases.
   - Run tests locally before making a pull request to make sure your changes don’t introduce new bugs.

5. **Code Reviews and Feedback**

   - Be open to receiving constructive feedback from other contributors.
   - Conduct code reviews for others and provide meaningful suggestions to improve the code.
   - Always refactor your code based on feedback to meet the project's standards.

<br>

# Additional Guidelines 📖
- Make sure to follow clean coding practices.
- Add comments wherever necessary for better code understanding.
- If you are adding new functionality, update the documentation in the README.

<br>

# Thank you for contributing 💗

We truly appreciate your time and effort to help improve our project. Feel free to reach out if you have any questions or need guidance. Happy coding! 🚀

##
