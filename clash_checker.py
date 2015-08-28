from datetime import datetime


class Course(object):

    def __init__(self, course_data):

        self.half = course_data['half']
        self.lecture_timetable = self.convert_json_timetable_to_datetime(course_data['timetable_json_lectures_only'])
        self.code = course_data['code']

    def convert_json_timetable_to_datetime(self, json_timetable):
        """Convert a json formatted timetable to a datetime formatted timetable

        The output is a list of tuples of datetimes e.g. [(start1, end1), (start2, end2)]
        where every tuple represents a lecture and the two datetimes in the tuple represent
        the start and end of the lecture respectively.
        """
        converted_timetable = []

        for lecture in json_timetable:
            converted_timetable.append((datetime.fromtimestamp(int(lecture['start'])),
                                        datetime.fromtimestamp(int(lecture['end']))))

        return converted_timetable

class CourseDatabase(dict):

    def __init__(self, courses_dict):
        for k, v in courses_dict.items():
            self[k] = Course(v)

class ClashChecker(object):

    def __init__(self, courses_dict):
        self.courses = CourseDatabase(courses_dict)

    def get_possible_courses(self, courses):
        """Return a dict of of all courses in the library and the number of clashes with the pre selected list of courses"""

        courses_selected = []
        possible_courses = {}

        for c in courses:
            try:
                courses_selected.append(self.courses[c])
            except KeyError:
                raise

        for c in self.courses.values():
            possible_courses[c.code] = self.count_clashes(c, courses_selected)

        return possible_courses

    def count_clashes(self, main_course, other_courses):
        clashes = 0

        for main_course_dt in main_course.lecture_timetable:
            for other_course in other_courses:
                for other_course_dt in other_course.lecture_timetable:
                    if self.date_intersect(main_course_dt, other_course_dt):
                        clashes += 1
        return clashes

    def date_intersect(self, course_one, course_two):
        """Returns true if dates intersect and false if they do not intersect"""
        course_one_start, course_one_end = course_one
        course_two_start, course_two_end = course_two

        return (course_one_start < course_two_end) and (course_one_end > course_two_start)

    def load_courses(self, courses_dict):
        courses = {}

        for k, v in courses_dict.items():
            courses[k] = Course(v)

        return courses
