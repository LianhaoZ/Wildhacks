# prereqParser.py
# Responsible for parsing the dictionary of human readable prereq information into a node format

from courseNode import CourseNode

def GenerateConnections(courseInfo : dict) -> dict:
    courses = {}
    for course in courseInfo.keys():
        courses[courses] = GenerateNodes(courseInfo[course])
    return courses

def GenerateNodes(prereqs):
    return "adlfa;ldfj"
