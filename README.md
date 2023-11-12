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

Please use the following command to check the tasks are complete sucessfully

```bash
pytest
```


**Task 1**

Ensure that the ```/health``` endpoint returns ```{'status': 'ok'}```

**Task 2**

Ensure that when the Test client queries the endpoint ```/users```, it returns the list of ```User``` models.

**Task 3**

Ensure that when the Test client queries the endpoint ```/items```, it returns the list of ```Item``` models.



# Conclusion

Please submit your you ChatGPT/Github Copilot message history & your browser history (During the Experiment) to ```matthewtyler.aylward@uzh.ch```