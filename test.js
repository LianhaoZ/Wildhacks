const {CourseNode} = require('./courseNode');
const ConnectionType = require('./connectionType');
const fs = require('fs');

const header = `
<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1, minimum-scale =1, maximum=scale=1, user scalable=no">
  <title>replit</title>
  <link href="style.css" rel="stylesheet" type="text/css" />
</head>
`;

function GenerateTreeHTML(dest, courses, course) {
    fs.writeFileSync(dest, header);
    fs.appendFileSync(dest, courses[course].BuildHTMLTree(courses, startname = course));
}

let courses = {};
courses["COMP_SCI 213"] = new CourseNode("COMP_SCI 211");
courses["COMP_SCI 211"] = new CourseNode(["COMP_SCI 111", "COMP_SCI 150"], ConnectionType.Or);
courses["COMP_SCI 111"] = null;
courses["COMP_SCI 150"] = new CourseNode(["COMP_SCI 110", "COMP_SCI 111", "GEN_ENG 205-1", "GEN_ENG 206-1"], ConnectionType.Or);
courses["GEN_ENG 205-1"] = null;
courses["GEN_ENG 206-1"] = null;
courses["COMP_SCI 110"] = null;
courses["COMP_SCI 300"] = new CourseNode([new CourseNode(["COMP_SCI 211", "GEN_ENG 205-1"], ConnectionType.Or),
new CourseNode("COMP_SCI 213")], ConnectionType.And);

fs.writeFileSync("courses.json", JSON.stringify(courses, null, 4), { encoding: 'utf8', flag: 'w' });

GenerateTreeHTML("treejs.html", courses, "COMP_SCI 300");