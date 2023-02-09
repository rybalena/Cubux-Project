# **New Cubux Python Project**

## Project Setup

- Install scoop from www.scoop.sh
- Install allure commandline by running the following command:
```
scoop install allure
```

- git clone
- cd to project directory
- Create a virtual environment:
```
py -m venv venv
```
- Activate your virtual environment:
```
.\venv\Scripts\activate
```

## Running Tests
```
pytest --alluredir=allure-results
```
- Run according to tags:
```
pytest -m <tag_name> 
```

## Viewing Test Results
- View allure results locally:
```
allure serve allure-results
```

## View Help And Custom CLI Options
```
pytest --help
```

