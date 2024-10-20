# Global Email Blacklist Microservice

## Overview

This is a microservice developed for a multinational company to manage its global email blacklist. The service allows multiple internal systems to add emails to the global blacklist and query whether a specific email is blacklisted. This project aims to centralize and improve the handling of email blacklists, which has been a pain point for the company, leading to legal and operational issues.

The microservice exposes two main RESTful endpoints:

- **POST `/blacklists`**: Add an email to the global blacklist.
- **GET `/blacklists/<email>`**: Check if an email is in the global blacklist.

## Components and Structure

The application is built using Python 3.10 and Flask, with several extensions to provide functionality for SQLAlchemy ORM, Marshmallow for serialization, and JWT for authorization.

### Project Structure

```bash
blacklist_service/
│
├── application.py          # Main entry point for the Flask app
├── config.py               # Configuration for the app (Database URI, JWT secret, etc.)
├── models.py               # SQLAlchemy models (defines the Blacklist table)
├── schemas.py              # Marshmallow schemas for serializing and deserializing data
├── routes.py               # Flask-RESTful routes for adding to and checking the blacklist
├── extensions.py           # Initialization of extensions (SQLAlchemy, JWT, Marshmallow)
├── requirements.txt        # Python dependencies for the project
└── migrations/             # Database migrations folder (auto-generated with Flask-Migrate)
```

### Key Components

- **Flask**: The web framework used to build the application.
- **Flask SQLAlchemy**: SQLAlchemy ORM used to interact with the PostgreSQL database.
- **Flask RESTful**: Provides easy creation of REST API endpoints.
- **Flask Marshmallow**: Handles request and response data serialization.
- **Flask JWT Extended**: Manages authorization using JSON Web Tokens (JWT).
- **PostgreSQL**: The relational database used to store the email blacklist data.

### API Endpoints

Inside the [`collections`](./collections/) folder in the project root, you will find the necessary postman collections and environments to use this application

## Setup Instructions

### Prerequisites

1. **Python 3.10+**
2. **PostgreSQL Database**: Ensure PostgreSQL is installed and running. You will need to create a database and configure the connection string in `config.py`.
3. **Pip**: Make sure you have `pip` installed to manage Python packages.

### Step-by-Step Setup

1. **Clone the repository**:

   ```bash
   git clone https://github.com/your-repo/blacklist_service.git
   cd blacklist_service
   ```

2. **Create a virtual environment**:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:

   - Create a `.env` file or set the following environment variables:
     ```bash
     export DATABASE_URL="postgresql://user:password@localhost/blacklist_db"
     export SECRET_KEY="your_secret_key"
     export JWT_SECRET_KEY="your_jwt_secret_key"
     ```

5. **Set up the database**:

   - Initialize the database and apply migrations.

   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   ```

6. **Run the app**:
   ```bash
   python application.py
   ```
   The service will be available at `http://127.0.0.1:5000`.
