import os


HTML_TEMPLATE = "template.html"
REPORT_SUBDIRECTORY = "generated_reports"



def write_report(selected_courses, possible_courses):

    with open(HTML_TEMPLATE, "r") as template_fp:
        template = template_fp.readlines()

    outfile = []
    for l in template:
        if '__COURSE_SELECTIONS__' in l:
            outfile.append("<h3>Courses selected: {}</h3>".format(', '.join(selected_courses).upper()))
        elif '__TABLE_ITEMS__' in l:
            for course in possible_courses.values():
                outfile.append("<tr>"
                               "<td><a href='{course.course_url}'>{course.code}</a></td>" \
                               "<td>{course.title}</td>" \
                               "<td>{course.category}</td>" \
                               "<td>{course.level}</td>" \
                               "<td>{course.credits}</td>" \
                               "<td>{course.clashes}</td>" \
                               "</tr>".format(course=course))
        else:
            outfile.append(l)


    try:
        os.mkdir(REPORT_SUBDIRECTORY)
    except FileExistsError:
        pass

    outfile_name = '{}.html'.format('_'.join(selected_courses).upper())
    outfile_name = os.path.join(os.path.dirname(__file__), REPORT_SUBDIRECTORY, outfile_name)
    outfile_fp = open(outfile_name, 'w')
    outfile_fp.writelines(outfile)
    print("Wrote results to {}".format(outfile_name))
