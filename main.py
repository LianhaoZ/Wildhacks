from courseNode import CourseNode
from courseNode import CourseNodeEncoder
from connectionType import ConnectionType
import scraper
import prereqParser
import json
from pprint import pprint

header = """
<!DOCTYPE html>
<html>

<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale =1, maximum=scale=1, user scalable=no">
  <title>Courses</title>
  <link href="style.css" rel="stylesheet" type="text/css" />
</head>


"""
def GenerateTreeHTML(dest, courses, course):
    with open(dest, "w") as outfile:
        outfile.write(header)
        outfile.write(courses[course].BuildHTMLTree(courses, startname=course))

courses = {}
courses["COMP_SCI 213"] = CourseNode("COMP_SCI 211")
courses["COMP_SCI 211"] = CourseNode(["COMP_SCI 111", "COMP_SCI 150"], ConnectionType.Or)
courses["COMP_SCI 111"] = None
courses["COMP_SCI 150"] = CourseNode(["COMP_SCI 110", "COMP_SCI 111", "GEN_ENG 205-1", "GEN_ENG 206-1"],
                                     ConnectionType.Or)
courses["GEN_ENG 205-1"] = None
courses["GEN_ENG 206-1"] = None
courses["COMP_SCI 110"] = None
courses["COMP_SCI 300"] = CourseNode([CourseNode(["COMP_SCI 211", "GEN_ENG 205-1"], 
                                                 ConnectionType.Or),
                                     CourseNode("COMP_SCI 213")], 
                                     ConnectionType.And)


with open("courses.json", "w") as outfile:
    json.dump(courses, outfile, cls=CourseNodeEncoder, indent=4)


GenerateTreeHTML("tree.html", courses, "COMP_SCI 300")