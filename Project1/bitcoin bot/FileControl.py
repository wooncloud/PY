import os
import json

def open_json_file(filename): 
    filename = os.getcwd() + "/Project1/bitcoin bot/" + filename
    with open(filename, encoding='UTF8') as file: 
        try:
            return json.load(file)
        except ValueError as e:
            print('파싱 실패! 에러 코드: {}'.format(e))
            return None
