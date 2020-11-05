# modec-api

## Introduction

The purpose of this API is to manage different equipments of an FPSO.

## Functionalities

### Register a new vessel

Creates a new vessel. If it already exists, the API will return a `409 - Conflicted` error.

```http
POST /register-vessel
body: {
    vessel-id: <vessel-id>
}
```

### Register a new equipment in a vessel

Given a vessel, creates a new equipment for that vessel. The user can create as many equipment as it wants. If the vessel doesn't exist, an error `404 - Not Found` should be returned.

```http
POST /register-equipment
body: {
    vessel-id: <vessel-id>
    equipment-id: <equipment-id>
    name: <equipment-name>
    location: <equipment-location>
}
```

### Set equipment status

Set the equipment status between `0 (ACTIVE)` and `1 (INACTIVE)`. There is some error cases here:

- Invalid status code: if the user passes an invalid status code an error `406 - Not Allowed` should be returned
- Equipment not found: if the user tries to set the status of an invalid equipment an error `404 - Not Found` should be returned.

```http
PATCH /update-equipment
body: {
    "equipment-id": <equipment-id>
    "status": <1 | 2>
}
```

### Return all equipments of a vessel

Returns a json with all equipments of a vessel. If the vessel doesn't exist, an error `404 Not Found` should be returned.

```http
POST /get_equipments?<vessel_id>
```

## Setup

To run the application:

- The user needs `Python` installed in it's machine (I used `Python 3.8.5`). I highly recommend using any virtual environment logic here:
  - virtualenv
  - virtualenvwrapper
  - conda env
- With `Python` installed, run

    ```bash
    pip install -r requirements.txt
    ```

    to install all the dependencies used in this project.
- To start the application, run

    ```bash
    flask run
    # or `python -m flask run`
    ```

- Now you can access the application via browser making requests in the address `localhost:5000`. If you want to make `HTTP requests` more easily, I highly recommend installing `Postman`. In Ubuntu 20.04 you can install it easily with `snap`:

    ```bash
    sudo snap install postman
    ```

## Explaining the code

### Base API

The API was developed using Flask (Python) with some basic setups like blueprint, that is a way to define routes outside the `app/__init__.py`. With this approach, we can separate each route in a different folder and files, keeping each route isolated.

### Database

The API doesn't have a persistent database. I implemented an abstraction `CustomDatabase.py`, where I can simulate any database operations in a `dict`.

### Tests

To test the application I used `pytest`, that is a module to run tests more efficiently. To configure it, the developer needs to create the `conftest.py` test file that has the `pytest` logic (for this project, I only used the `fixture` decorator, that is a way to share functions from the `conftest.py` across all test files) and any other feature you want - I created some helper methods to improve the code files; like a database handler and a app helper to do the http requests. After setting the `conftest.py`, the developer needs to create test files with the same structure:

- test file name: `test_<test name>.py`.
- inside the test file, the methods should start with `test_<what are you testing>`. The developer can pass any `fixture` created before inside the method' signature.

To test the application, you just need to run `pytest`.

Each test is in a `__tests__` directory, so I can separate them by logic (for example, the routes test should be in the `routes/__tests__` path)
