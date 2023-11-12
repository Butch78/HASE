# Python Coding Tasks

# Introduction

For this Experiment you will be using FastAPI, a python framework for building APIs. You will be given a basic FastAPI application that has 3 endpoints, you will need to fix the endpoints so that they return the correct data.


## Set Up

To complete the Tasks you will need to open this repository in Github Codespaces, you can access this by pressing **<> Code** -> **Codespaces** ->  **Create Codespace on Master**

Once your Codespace has started you will just need to install the required packages using this command:

```
pip install -r requirements.txt
```

## Tasks

This a basic FastAPI application that has 3 endpoints will return the health of the application, a list of  ```user``` and ```item``` objects. You will have 3 tasks which are fixing the 3 endpoints in the ```src/main.py``` file.


**Task 1**

Ensure that the ```/health``` endpoint returns ```{'status': 'ok'}```

Check the success of this task by running the following command in the terminal:

```bash
pytest src/tests/test_main.py::test_health
```

**Task 2**

Ensure that when the Test client queries the endpoint ```/users```, it returns the list of ```User``` models.

Check the success of this task by running the following command in the terminal:

```bash
pytest src/tests/test_main.py::test_get_users
```

**Task 3**

Ensure that when the Test client queries the endpoint ```/items```, it returns the list of ```Item``` models.

Check the success of this task by running the following command in the terminal:

```bash
pytest src/tests/test_main.py::test_get_items
```



# Conclusion

Please run the following command in the terminal to output your results:
    
```bash
pytest > test_results.txt
```

Please submit your the newly created file ```test_results.txt```, your ChatGPT/Github Copilot message history & your browser history (During the Experiment) to ```matthewtyler.aylward@uzh.ch```