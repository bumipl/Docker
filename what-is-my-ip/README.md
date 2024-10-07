# What Is My IP

A simple Flask application that displays your public IP address. This application is containerized using Docker and can be run locally.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Getting Started](#getting-started)
- [Running the Application](#running-the-application)
- [Project Structure](#project-structure)
- [License](#license)

## Features

- Displays your public IP address.
- Built with Flask.
- Containerized using Docker.
- Simple and easy to use.

## Technologies Used

- Python 3.9
- Flask
- Docker
- Docker Compose

## Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

- [Docker](https://www.docker.com/get-started) installed on your machine.
- [Docker Compose](https://docs.docker.com/compose/install/) installed on your machine.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/what-is-my-ip.git
   cd what-is-my-ip
   ```

2. Build and run the application in detached mode.
    
   ```bash
   docker-compose up --build -d
   ```

3.  Access the application in your web browser at `http://localhost:5000/`  

## Running the Application
Access the application in your web browser at http://localhost:5000/

```bash
docker-compose up -d
```

## To stop and destroy the application, run:

```bash
docker-compose down
```

## Project strucutre

```
what-is-my-ip/
├── app.py                # Main application file
├── Dockerfile            # Dockerfile for building the image
├── docker-compose.yml    # Docker Compose configuration file
└── templates/            # Directory for HTML templates
    └── index.html        # HTML template for displaying the IP address
```


