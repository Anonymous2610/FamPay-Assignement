# FamPay YouTube API Project

This project fetches and displays the latest YouTube videos based on a predefined query using Django, Celery, and Redis.

## Getting Started

These instructions will guide you on how to set up and run the project on your local machine.

### Prerequisites

- Python 3.x
- Django
- Celery
- Redis

### Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/fampay-youtube-api.git
    ```

2. **Navigate to the project directory:**

    ```bash
    cd fampay-youtube-api
    ```

3. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

4. **Set up Django database:**

    ```bash
    python manage.py migrate
    ```

5. **Run the Celery worker:**

    ```bash
    celery -A fampay worker -l info
    ```

6. **Run the Celery Beat scheduler:**

    ```bash
    celery -A fampay beat -l info
    ```

7. **Start the Django development server:**

    ```bash
    python manage.py runserver
    ```

### Create Superuser

To access the Django admin dashboard, you can create a superuser with the following steps:

1. **Create a superuser:**

    ```bash
    python manage.py createsuperuser
    ```

2. **Follow the prompts to set a username, email, and password for the superuser.**

### Access Admin Dashboard

1. **Start the Django development server if it's not running:**

    ```bash
    python manage.py runserver
    ```

2. **Visit [http://localhost:8000/admin/](http://localhost:8000/admin/) in your web browser.**

3. **Log in using the credentials of the superuser you created.**

Now, you can use the Django admin dashboard to manage your application data.
