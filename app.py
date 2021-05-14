from flask import Flask
from gsheets import Sheets
from collections import defaultdict

app = Flask(__name__)
course_directory = defaultdict(lambda: [])
def build_dict_from_sheet():
    sheets = Sheets.from_files('~/credential.json', '~/storage.json')
    url = 'https://docs.google.com/spreadsheets/d/1hg9505a4hmp93pssg3hnZkPBSEhoR0X2w3i_MApocZ8/edit#gid=1621532970'
    data = sheets.get(url)
    print(data)



@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    # app.run()
    build_dict_from_sheet()
