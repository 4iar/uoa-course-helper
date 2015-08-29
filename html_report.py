

HTML_TEMPLATE = "template.html"


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

    outfile_name = '{}.html'.format('_'.join(selected_courses).upper())
    outfile_fp = open(outfile_name, 'w')
    outfile_fp.writelines(outfile)
    print("Wrote results to {}".format(outfile_name))

