from flask import Flask
from gsheets import Sheets
from collections import defaultdict
from pandas import DataFrame


course_directory = defaultdict(lambda: [])
added_set = set()
def build_dict_from_sheet():
    sheets = Sheets.from_files('credential.json', 'storage.json')
    url = 'https://docs.google.com/spreadsheets/d/1hg9505a4hmp93pssg3hnZkPBSEhoR0X2w3i_MApocZ8/edit#gid=1621532970'
    sheet = sheets.get(url)
    cols = ['B', 'D']
    data = DataFrame()
    data = sheet.sheets[0].to_frame()
    data = data.rename(columns={'Every class you have taken: Format-> Course_Name(Grade/TA)':'Courses'})
    data = data[['Name', 'Courses']]
    for index, row in data.iterrows():
        courses = cleanup_data(row['Courses'])
        for c in courses:
            # print(c.split('('))
            course_name, grade = c.split('(')
            if (course_name, row["Name"].lower()) not in added_set:
                added_set.add((course_name, row['Name']))
                is_ta = grade[:-1].lower() == 'ta'
                grade = grade[:-1] if not is_ta else 'A'
                course_directory[course_name].append({'Name' : row['Name'], 'grade' : grade, 'ta' : is_ta})
        print(course_directory)
def cleanup_data(str):
    return ''.join([c for c in str.replace("\n", ",") if (c.isalnum() or c in ",()")]).split(',')




if __name__ == '__main__':
    # app.run()
    build_dict_from_sheet()
