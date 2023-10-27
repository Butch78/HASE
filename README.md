# Python Coding Tasks

## Set Up

To complete the Tasks you will need to open this repository in Github Codespaces, you can access this by pressing **<> Code** -> **Codespaces** ->  **Create Codespace on Master**

Once your Codespace has started you will just need to install the required packages using this command:

```
pip install -r requirements.txt
```

## Tasks

This a basic FastAPI application that will return ```user``` & ```item``` objects. You will have 3 tasks which are fixing the 3 endpoints in the ```src/main.py``` file.

**Task 1**

Ensure that the ```/health``` endpoint returns ```{'status': 'ok'}```

**Task 2**

Ensure that when you perform the ```client.get("/users")``` function you are able to return a python list of ```User```

**Task 3**

Ensure that when you perform the ```client.get("/items")``` function you are able to return a python list of ```Item```

Please use the following command to check the tasks are complete sucessfully
```
pytest -v
```
