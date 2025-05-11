# CodeBin - Code Sharing Platform

CodeBin is a Django-based web application that allows users to share code snippets with others. The platform supports syntax highlighting for various programming languages and provides user authentication to control who can create, edit, and delete snippets.

## Features

- **User Authentication**: Register, login, and manage your profile
- **Code Snippet Management**: Create, read, update, and delete code snippets
- **Syntax Highlighting**: Beautiful syntax highlighting for over 20 programming languages
- **Public/Private Snippets**: Choose whether your snippets are public or private
- **Search Functionality**: Search for snippets by keywords or filter by programming language
- **User Profiles**: View all public snippets by a specific user
- **Responsive Design**: Works on desktop, tablet, and mobile devices

## Tech Stack

- **Backend**: Django 4.2
- **Frontend**: Bootstrap 5, JavaScript, CSS
- **Database**: SQLite (development), PostgreSQL (production)
- **Syntax Highlighting**: Prism.js
- **Deployment**: GitHub (source code), PythonAnywhere (hosting)

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:

```bash
git clone https://github.com/huber233/codebin.git
cd codebin
```

2. Create a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Apply migrations:

```bash
python manage.py migrate
```

5. Initialize the database with programming languages:

```bash
python initialize_db.py
```

6. Create a superuser (admin):

```bash
python manage.py createsuperuser
```

7. Run the development server:

```bash
python manage.py runserver
```

8. Visit http://127.0.0.1:8000/ in your browser

## Deployment to PythonAnywhere

1. Sign up for a PythonAnywhere account
2. Create a new web app with Django configuration
3. Clone your GitHub repository in PythonAnywhere
4. Set up your virtual environment and install requirements
5. Configure your WSGI file to point to your project
6. Set up your database (PostgreSQL recommended for production)
7. Apply migrations and initialize the database
8. Configure your static files
9. Reload the web app

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add some feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.