# LittleLemon (Meta's Back-End Developer Capstone Project)

Welcome to the **LittleLemon** Project,
a culmination of the skills and knowledge gained throughout the Coursera Back-End Developement Specialization.

## Project Overview

The Back-End Developer Capstone Project serves as the final project for the Coursera Back-End Developer Specialization.
This project is designed to showcase our proficiency in building full-stack applications using Django.
Through this project, we gained the opportunity to apply our understanding of database design, RESTful APIs,
authentication, and deployment to create a real-world web application.

## Features

- User Authentication
- CRUD Operations
- API Endpoints
- Database Models

## Getting Started

### Installation

1. Clone this repository to your local machine
2. Create and activate a virtual environment based on your OS:

```shell
python3 -m venv venv
source venv/bin/activate
```

3. Install project dependencies:

```shell
pip install -r requirements.txt
```

### Configuration

Before running the application, you might need to configure the database, and any other necessary settings.
Refer to the project documentation for specific configuration instructions.
e.g. you should have set your database configurations such as `USER` and `PASSWORD` in project `settings.py`.

- Apply database migration commands:

```shell
python manage.py makemigrations
python manage.py migrate
```

## Usage

To start the development server, run:

```shell
python manage.py runserver
```

Visit <http://127.0.0.1:8000/> in your web browser to access the application.

## API Endpoints

Below API Endpoints are for the Peer-graded review:

- `restaurant/menu/`
- `restaurant/booking/`
- `auth`
