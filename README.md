# Rollee API Challenge

## Overview
This project is designed to authenticate users and retrieve their account information from Rollee's API. The solution follows best practices such as environment variable management, logging, and structured exception handling.

## Setup Instructions

### Prerequisites
- Python 3.10+
- Docker (optional but recommended)

### Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/your-repo/rollee-challenge.git
   cd rollee-challenge
   ```
2. Create and activate a virtual environment:
   ```sh
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```
3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up environment variables:
   - Create a `.env` file in the project root.
   - Add the following environment variables:
     ```ini
     AUTH_URL=https://keycloak.getrollee.com/realms/rollee/protocol/openid-connect/token
     ACCOUNTS_URL_TEMPLATE=https://api.sand.getrollee.com/api/dashboard/v0.1/views/user/{user_id}?start_date=1268385035&end_date=1741770635
     CLIENT_ID=dashboard
     USERNAME=engr.abidbaig@gmail.com
     PASSWORD=Abid@rollee
     USER_ID=f1e13e83-fcd6-4990-b18b-022c6fc1ab80
     ```
   **Note:** Normally, we do not push `.env` files to GitHub for security reasons, but for the sake of running the project, it is included.

### Running the Application
```sh
python main.py
```

## Dockerized Deployment

### Building and Running the Docker Container
1. Build the Docker image:
   ```sh
   docker build -t rollee-app .
   ```
2. Run the container:
   ```sh
   docker run --env-file .env rollee-app
   ```

### Using Docker Compose (Recommended)
1. Create a `docker-compose.yml` file in the project root with the following content:
   ```yaml
   version: "3.8"

   services:
     rollee:
       build: .
       env_file: .env
       container_name: rollee-container
       command: ["python", "main.py"]
   ```
2. Run the application with:
   ```sh
   docker-compose up --build
   ```

## Running Unit Tests
1. Run unit tests with:
   ```sh
   python -m unittest 
   ```
