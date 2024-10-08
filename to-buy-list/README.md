# To-Buy List Application

## Overview

The To-Buy List application is a simple web application built using Flask and Docker. It allows users to manage a shopping list by adding and removing items. The application also sends an email update of the shopping list to specified email addresses at regular intervals.

## Features

- Add items to the shopping list.
- Remove items from the shopping list.
- Email updates of the shopping list every 40 seconds after the last item is added or removed.
- Simple and user-friendly web interface.

## Technologies Used

- **Flask**: A lightweight WSGI web application framework in Python.
- **SQLite**: A lightweight database for storing the shopping list items.
- **Docker**: Containerization platform to run the application in an isolated environment.
- **HTML/CSS**: For the front-end user interface.

## Directory Structure

to-buy-list/
├── app/
│   ├── requirements.txt
│   ├── app.py
│   └── templates/
│       └── index.html
├── Dockerfile
└── docker-compose.yml

Code

Copy Code

## Setup Instructions

### Prerequisites

- Docker installed on your machine.
- Docker Compose installed.

### Running the Application

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd to-buy-list
   ```
   
2. Create a `.env` file in the root directory with the following content:

```txt
EMAIL_USER=your_email@gmail.com
EMAIL_PASS=your_email_password
RECIPENT="recipent_of_email_delivery"
```
Replace variables for `EMAIL_USER` and `EMAIL_PASS' with your real data.
Remember that for gmail.com email, you have to Generate an App Password, do not provide the current account password. 
Follow this guide, scroll down to this section -> [Generate an App Password](https://www.linode.com/docs/guides/configure-postfix-to-send-mail-using-gmail-and-google-workspace-on-debian-or-ubuntu/#secure-your-postfix-hash-database-and-email-password-files).
Replace RECIPENT with delivery email address.


3. Build and run the application using Docker Compose:

```bash
docker-compose up --build -d
```

4. Access the application in your web browser at `http://localhost:8080`.

###Application Logic

* Database Initialization: The application initializes a SQLite database to store shopping list items.
* Adding Items: Users can add items through a form, which are then stored in the database.
* Removing Items: Users can remove items from the list, which updates the database accordingly.
* Email Notifications: The application sends an email with the current shopping list every 40 seconds after the last modification.

### Code Explanation
Dockerfile
The `Dockerfile` defines the environment for the application:


```bash
Copy Code
version: '3.8'

services:
  web:
    build: .
    container_name: to-buy-app
    image: bumipl/to-buy-app:1.2
    ports:
      - "8080:8080"
    env_file:
      - .env
```
     
### Flask Application
The main application logic is contained in app.py:

* Database Functions: Functions to initialize the database, add, remove, and retrieve items.
* Email Functionality: Uses SMTP to send emails with the shopping list.
* Flask Routes: Defines routes for the main page, adding items, and removing items.

### HTML Template
The `index.html` file provides the front-end interface for users to interact with the application.

### Contributing
Feel free to submit issues or pull requests if you have suggestions or improvements for the application.

### License
This project is licensed under the MIT License - see the LICENSE file for details.

