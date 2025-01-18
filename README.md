# Receipe Manager

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

Receipe Manager is a Django-based web application that allows users to create, manage, and share recipes. Users can add ingredients, instructions, and categorize their recipes for easy access and sharing.

## Getting Started <a name = "getting_started"></a>

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See [deployment](#deployment) for notes on how to deploy the project on a live system.

### Prerequisites

You will need the following software installed on your machine:

- Python 3.10 or higher
- Django 5.1.4
- pip (Python package installer)

### Installing

A step-by-step series of instructions to get your development environment running:

1. Clone the repository:
    ```sh
    git clone https://github.com/krishna-shah-07/receipemanager.git
    cd receipemanager
    ```

2. Create a virtual environment:
    ```sh
    python -m venv venv
    ```

3. Activate the virtual environment:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

5. Apply the migrations:
    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

6. Run the development server:
    ```sh
    python manage.py runserver
    ```

## Usage <a name = "usage"></a>

To use the application, navigate to `http://127.0.0.1:8000` in your web browser. You can create, view, and manage recipes through the web interface.

## Deployment <a name = "deployment"></a>

To deploy this project on a live system, follow these steps:

1. Set up a production-ready database (e.g., PostgreSQL).
2. Configure the database settings in `settings.py`.
3. Collect static files:
    ```sh
    python manage.py collectstatic
    ```
4. Set up a web server (e.g., Gunicorn) and a reverse proxy (e.g., Nginx).
5. Configure the server to serve the Django application.

For detailed deployment instructions, refer to the Django documentation.

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct, and the process for submitting pull requests to us.
