# FamPay YouTube API Project

This project fetches and displays the latest YouTube videos based on a predefined query using Django, Celery, and Redis.

## Architecture Overview

### Components

1. **Django Framework:**
   - Django is a high-level Python web framework that follows the model-view-controller (MVC) architectural pattern.
   - It is used to handle HTTP requests, manage the application's data models, and serve dynamic web content.

2. **Celery:**
   - Celery is an asynchronous task queue/job queue system that distributes tasks across multiple worker processes or servers.
   - In this project, Celery is employed to handle background tasks asynchronously, such as fetching and processing the latest YouTube videos at regular intervals.

3. **Redis:**
   - Redis is an in-memory data structure store, acting as a broker for Celery to facilitate communication between Django and Celery.
   - It stores task messages between the Django application and Celery workers, ensuring seamless task execution.

### Workflow

1. **User Interaction:**
   - Users interact with the Django application through the defined API endpoints.

2. **Django API Endpoints:**
   - Django exposes RESTful API endpoints to serve requests for fetching the latest YouTube videos and managing API keys.

3. **Celery Background Tasks:**
   - Celery is scheduled to run periodic background tasks using the Celery Beat scheduler.
   - The main background task involves querying the YouTube Data API to fetch the latest videos based on a predefined query.

4. **Redis as a Message Broker:**
   - Redis acts as a message broker, facilitating communication between the Django application and Celery workers.
   - It stores task messages and ensures that background tasks are executed efficiently.

5. **Database (Django Models):**
   - Django models represent the data structure of the application.
   - The `YoutubeVideos` model stores information about the fetched YouTube videos.
   - The `APIKeys` model manages API keys and their usage.

6. **Django Admin Dashboard:**
   - Django provides an admin dashboard for managing application data, accessible through a superuser account.
   - Superusers can log in to the admin dashboard to view and manage videos, API keys, and other relevant data.

### Task Flow

1. Users make requests to the defined API endpoints.
2. Django processes these requests and communicates with Celery to schedule background tasks.
3. Celery asynchronously executes background tasks, such as fetching the latest YouTube videos and storing them in the database.
4. Redis facilitates communication between Django and Celery by storing task messages.
5. The Django admin dashboard allows superusers to manage application data conveniently.

This architecture ensures a scalable and efficient system for fetching and displaying the latest YouTube videos while maintaining responsiveness and user interactivity.

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
    celery -A fampay worker -l info -P solo
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
