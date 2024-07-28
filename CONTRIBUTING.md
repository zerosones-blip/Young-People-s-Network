# Contributing to Young People's Network

Thank you for your interest in contributing to the **Young People's Network**! We welcome contributions from everyone, whether you're a seasoned developer or new to open source. This document will guide you through the process of contributing to our project.

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
  - [Reporting Bugs](#reporting-bugs)
  - [Suggesting Enhancements](#suggesting-enhancements)
  - [Submitting Pull Requests](#submitting-pull-requests)
- [Development Setup](#development-setup)
- [Style Guides](#style-guides)
  - [Git Commit Messages](#git-commit-messages)
  - [Python Style Guide](#python-style-guide)
  - [Django Style Guide](#django-style-guide)
  - [JavaScript Style Guide](#javascript-style-guide)
- [License](#license)

---

## Code of Conduct

By participating in this project, you agree to abide by our [Code of Conduct](CODE_OF_CONDUCT.md). Please read it to understand the expectations we have for everyone involved in our community.

---

## How Can I Contribute?

### Reporting Bugs

If you find a bug, please report it by opening an issue in our [GitHub repository](https://github.com/zerosones-blip/Young-People-s-Network/issues). Include as much detail as possible to help us understand and reproduce the problem. Be sure to include:

- A clear and descriptive title
- Steps to reproduce the bug
- Expected and actual behavior
- Screenshots, if applicable
- Information about your environment (e.g., browser version, operating system)

### Suggesting Enhancements

We welcome suggestions for new features and improvements! To suggest an enhancement, please open an issue in our [GitHub repository](https://github.com/zerosones-blip/Young-People-s-Network/issues) and provide the following information:

- A clear and descriptive title
- A detailed description of the proposed enhancement
- Any related issues or discussions

### Submitting Pull Requests

Before submitting a pull request, please ensure you've done the following:

1. **Fork the Repository**: Create a personal copy of the repository by forking it on GitHub.
2. **Create a Branch**: Create a new branch for your changes. Use a descriptive name, such as `feature/add-new-event-type` or `bugfix/fix-login-issue`.
3. **Implement Your Changes**: Make your changes in the new branch.
4. **Test Your Changes**: Ensure that your changes do not break existing functionality and that they meet our quality standards.
5. **Commit Your Changes**: Write clear and concise commit messages (see [Git Commit Messages](#git-commit-messages)).
6. **Push to Your Fork**: Push your changes to your fork on GitHub.
7. **Open a Pull Request**: Open a pull request from your branch to the `main` branch of the original repository. Provide a detailed description of your changes and reference any related issues.

---

## Development Setup

To set up the development environment for the Young People's Network, follow these steps:

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/zerosones-blip/Young-People-s-Network.git
    cd Young-People-s-Network
    ```

2. **Create a Virtual Environment**:
    ```sh
    python3 -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Apply Migrations**:
    ```sh
    python manage.py migrate
    ```

5. **Create a Superuser**:
    ```sh
    python manage.py createsuperuser
    ```

6. **Run the Development Server**:
    ```sh
    python manage.py runserver
    ```

7. **Run Tests**:
    ```sh
    python manage.py test
    ```

---

## Style Guides

### Git Commit Messages

- Use the present tense ("Add feature" not "Added feature").
- Use the imperative mood ("Move cursor to..." not "Moves cursor to...").
- Limit the subject line to 50 characters or less.
- Include a detailed description in the body, if necessary.

### Python Style Guide

- Follow the [PEP 8](https://pep8.org/) style guide.
- Use 4 spaces per indentation level.
- Write docstrings for all public modules, functions, classes, and methods.

### Django Style Guide

- Follow the [Django coding style](https://docs.djangoproject.com/en/dev/internals/contributing/writing-code/coding-style/).
- Use meaningful names for models, views, and templates.
- Ensure migrations are generated and included with model changes.

### JavaScript Style Guide

- Follow the [Airbnb JavaScript Style Guide](https://github.com/airbnb/javascript).
- Use `const` and `let` instead of `var`.
- Prefer arrow functions (`() => {}`) for anonymous functions.

---

## License

By contributing to the Young People's Network, you agree that your contributions will be licensed under the [MIT License](LICENSE).

---

Thank you for contributing to the Young People's Network! We appreciate your support and look forward to working with you to build an amazing platform for young people.
