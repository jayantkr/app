#!flask/bin/python
from flask import Flask
import requests
# import module for processing json
import parse

URL_TO_GET_NAME_SURNAME = 'http://uinames.com/api/'
URL_TO_GET_JOKE = 'http://api.icndb.com/jokes/random?firstName='
DEFAULT_STRING = 'Please Try Again'

app = Flask(__name__)

@app.route('/')
# Gather all the main functionality here
def main():
    #define Accept header 
    head= {"Accept":"applicaiton/json"}
    try:
        response = requests.get(URL_TO_GET_NAME_SURNAME, headers=head)
    except requests.exceptions.RequestException as e:
        return DEFAULT_STRING

    if response.status_code == 200:
        parsed_json = parse.get_json(response.json())
    else:
        return DEFAULT_STRING

#    print parsed_json['name'] + '&&' + parsed_json['surname']
    url_to_get_joke = URL_TO_GET_JOKE + parsed_json['name'] + '&lastName=' +\
                                                     parsed_json['surname']

    try:
        response = requests.get(url_to_get_joke, headers=head)
    except requests.exceptions.RequestException as e:
        return DEFAULT_STRING
    if response.status_code == 200:
        parsed_json =  parse.get_json(response.json())
        json_string = parse.get_json(parsed_json['value'])
	return json_string['joke'] 
    else:
        return  DEFAULT_STRING
     

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=8000)
