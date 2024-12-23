# MedAPI

MedAPI is a simple REST API built using **FastAPI**, **SQLAlchemy**, and **PostgreSQL**. It provides CRUD operations for managing patient and doctor data and their corresponding treatments. The application is designed to be easily extended and used in healthcare or clinical environments.

---

## Technologies Used

- **FastAPI** - A modern, fast web framework for building APIs with Python.
- **SQLAlchemy** - ORM for database interaction.
- **PostgreSQL** - The relational database management system used for storing data.
- **Alembic** - A database migration tool for SQLAlchemy.
- **Pydantic** - Data validation and settings management using Python type annotations.

---

## Features

- **Patient Management**: Add, read, update, and delete patient information.
- **Doctor Management**: Manage doctors' data, including their specialization and experience.
- **Treatment Records**: Track treatments associated with patients and doctors, including diagnosis and dates.
- **CRUD Operations**: Full create, read, update, and delete functionality for all entities.
- **Pagination**: Paginated results for large datasets.
- **Search**: Full-text search over treatment records using JSON fields and pg_trgm indexes.

---

## Getting Started

### Prerequisites

Before starting, make sure you have the following installed:

- Python 3.8+  
- PostgreSQL  
- pip (Python package installer)

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/yourusername/medapi.git
    cd medapi
    ```

2. **Set up a Python virtual environment**:

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use 'venv\Scripts\activate'
    ```

3. **Install the dependencies**:

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up the PostgreSQL database**:

    Create a new database in PostgreSQL and configure the `DATABASE_URL` in the `.env` file.

    Example `.env` file:
    ```bash
    DATABASE_URL=postgresql://username:password@localhost/medapi_db
    ```

5. **Initialize the database**:

    Run the following command to create the database schema:

    ```bash
    alembic upgrade head
    ```

6. **Run the application**:

    Start the FastAPI server:

    ```bash
    uvicorn app.main:app --reload
    ```

    Your API will be available at `http://127.0.0.1:8000`.

---

