# Project Title
 FastAPI JWT Authentication Demo App

## Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Contributing](../CONTRIBUTING.md)

## About <a name = "about"></a>

The purpose of this project is to create a FastAPI endpoint that accepts a dictionary and responds with a JSON representation of the dictionary. Additionally, the API will be secured with JWT authentication, ensuring that only users with a valid JWT token can access the endpoint.

## Getting Started <a name = "getting_started"></a>

These instructions will help you set up the project on your local machine for development and testing purposes. To get started, follow the steps below:

### Prerequisites

Before running the project, make sure you have the following installed on your machine:

    Python 
    Docker (for containerization)

### Installing

Clone the repository to your local machine:

```
git clone https://github.com/meghana2002/FastAPI_demo_app

```

Navigate to the project directory:

```
cd FastAPI demo app

```
Create a virtual environment and activate it:

```
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

```

Install the required dependencies:

```
pip install -r requirements.txt

```

Running the FastAPI Application

To run the FastAPI application locally, use the following command:

```
python main.py

```
Running the Application in a Docker Container

To run the application in a Docker container, ensure that you have Docker installed and running on your machine. Then, follow these steps:

```
sudo docker build -t myfastapi

```

Run the docker container:
```
sudo docker run -p 8000:8000 myfastapi

```
The FastAPI application will now be accessible at http://localhost:8000.


## Usage <a name = "usage"></a>

To access the API endpoint, make a POST request to http://localhost:8000/api/dictionary with a valid JWT token passed in the Authorization header as a bearer token.

Example using curl:

```
curl -X 'POST' \
  'http://localhost:8000/api/dictionary' \
  -H 'Authorization: Bearer your-jwt-token' \
  -H 'Content-Type: application/json' \
  -d '{
  "key1": "value1",
  "key2": "value2",
  "key3": "value3"
}'


```
The API will respond with a JSON representation of the dictionary provided in the request.

Unit Tests

To run the unit tests for the API endpoints, use the following command:

```
pytest tests/

```
The unit tests include mocked authentication to simulate both authenticated and unauthenticated scenarios.

Contributing

If you'd like to contribute to this project, please follow the guidelines in CONTRIBUTING.md. We welcome contributions and appreciate any feedback or suggestions!