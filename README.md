# uoa-course-helper

## Summary
uoa-course-helper generates a HTML report of all courses and the number of timetable clashes that occur with the given courses.

The report provides an overview of all courses that can be taken within a semester and is much
more convenient than entering each potential course into the official clash checker.

## Usage
Syntax:
```
python3 run.py [selected courses]
```
Example:
```
python3 run.py EG2004 EG2011 EG2012
```

Example output in browser:


![alt tag](https://i.imgur.com/letDkv9.png)

## Course data

This repo already contains a courses.json file which contains course data such as course half, credits, title, urls, timetable, etc. However, if you need to update the data then run the [course scraper](https://github.com/4iar/uoa-course-scraper)
