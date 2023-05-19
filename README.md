# Request handler
____
## Description
Simple program that accepts requests and saves them in json format. 

## Technology stack
· Flask
____

## Installation

clone the repository and go to it on the command line:
```sh
https://github.com/BerdyshevEugene/request_handler.git
```

create and activate virtual enviroment:
```sh
python3 -m venv venv
source venv/bin/activate
python3 -m pip install --upgrade pip
```
install dependencies from a file requirements.txt:
```
pip install -r requirements.txt
```

run main.py:
```sh
python3 main.py
```
try to pass the request like in the example below:
```
http://127.0.0.1:5000/test/?user=User1&id=1&phone=1
```
the results will be saved to the data.json file
____
