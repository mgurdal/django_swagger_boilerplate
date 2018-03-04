## Simple swagger boilerplate for django rest applications

## Setup
1. Create a isolated environment and get inside it
    - with  **virtualenv**
      ```bash
      virtualenv env -p python2.7
      . ./env/bin/activate
      ```
    - or **pipenv**
      ```bash
      pipenv --two
      pipenv shell
      ```
2. Install the dependencies
    - virtualenv
      ```bash
      pip install -r requirements.txt
      ```
    - pipenv
      ```bash
       pipenv install
     ```
3. Initialize and start the project
    ```bash
    ./manage.py migrate
    ./manage.py runserver
    ```
