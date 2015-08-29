import json
import sys
from clash_checker import ClashChecker
import html_report


FILENAME = 'courses.json'

fp = open(FILENAME, 'r')
course_dict = json.loads(fp.read())

c = ClashChecker(course_dict)
possible_courses = c.get_possible_courses(sys.argv[1:])

html_report.write_report(sys.argv[1:], possible_courses)


