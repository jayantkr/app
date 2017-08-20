import json
# Define a "getJson" function that takes 1 arguments
# returns json_string

def get_json(input_string):
    json_string = json.dumps(input_string)
    try:
        parsed_json = json.loads(json_string)
    except:
        print repr(resonse_json)
        return
    return parsed_json

