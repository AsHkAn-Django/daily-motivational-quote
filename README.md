Daily Motivational Quote App

Just a quick little project I made while practicing Django and backend development.
This is part of my journey as I learn and improve my skill

## About the Project

This project is built using Django and includes a simple frontend with HTML, CSS, Bootstrap, and some JavaScript.
The app delivers a “Quote of the Day” to users and adds extra functionality like scheduling, notifications, and social media sharing.

## Features

- Task scheduling with Celery
- Sending emails/SMS
- Integrating with social media APIs
- Daily Quote Scheduling – A “Quote of the Day” is automatically scheduled.
- Notifications – Users can subscribe to receive daily quotes via email or SMS.
- Social Media Sharing – Automatic posting to connected social media accounts.
- User Accounts – Simple authentication so users can manage their subscriptions.
- Basic UI – Clean and minimal frontend using Bootstrap.

## Technologies Used

- Python
- Django
- HTML
- HTML, CSS, Bootstrap, JavaScript
- Celery (for task scheduling & background jobs)
- Redis (as Celery broker)
- SMTP / Twilio (for email & SMS)
- Social Media APIs (Twitter/X, Facebook, etc.)

## About Me

Hi, I'm Ashkan — a junior Django developer who recently transitioned from teaching English as a second language to learning backend development.
I’m currently focused on improving my skills, building projects, and looking for opportunities to work as a backend developer.
You can find more of my work here: [My GitHub](https://github.com/AsHkAn-Django)
[Linkdin](in/ashkan-ahrari-146080150)

## How to Use

1. Clone the repository
   `git clone https://github.com/AsHkAn-Django/daily-motivations-quote.git`
2. Navigate into the folder
   `cd daily-motivations-quote`
3. Create a virtual environment and activate it
   `python -m venv .venv`
   `source .venv/bin/activate  # Or .venv\Scripts\activate  on Windows`
4. Install the dependencies
   `pip install -r requirements.txt`
5. Run the server
   `python manage.py migrate`
   `python manage.py createsuperuser`
   `python manage.py runserver`
6. Start the Celery worker (in a separate terminal)
   `celery -A daily_motivations worker -l info`
   `celery -A daily_motivations beat -l info`
## Tutorial

COMMING SOON

---
