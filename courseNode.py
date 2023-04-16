from connectionType import ConnectionType
import json

class CourseNodeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, CourseNode):
            return {
                "connections": obj.connections,
                "connectionType": obj.connectionType
            }
        return super().default(obj)

# A CourseNode may have two values
# If the CourseNode is composite, then it's connections are always other courseNodes
# If the CourseNode is not composite, then it's connection is singular - it is a string
class CourseNode:
    def __init__(self, connections=None, connectionType=ConnectionType.NoConnection):
        self.connections = []
        # We love dynamic languages :c
        if connections != None:
            if isinstance(connections, str):
                    self.connections = connections
            else:
                if connectionType != connectionType.NoConnection: # This is a composite node, therefore will only have nodes as children
                    for connection in connections:
                        if isinstance(connection, CourseNode):
                            self.connections.append(connection)
                        elif isinstance(connection, str):
                            node = CourseNode()
                            node.connections = connection
                            self.connections.append(node)
                        else:
                            ValueError("Connections can only be CourseNodes or course names!")
                else:
                    self.connections = connections # This is not a composite node, and therefore will be stored as a string
            
        self.connectionType = connectionType 

    def GetType(self) -> ConnectionType:
        return self.connectionType

    def GetConnections(self):
        return self.connections
        
    # A node is composite when it is comprised of at least one non-compsite node
    # If the node simply holds a courseName as it's connection, then it is not composite
    def IsComposite(self):
        return self.connectionType != ConnectionType.NoConnection
        
    
    def BuildHTMLTree(self, courses, level = 0, startname = "") -> str:

        def BuildElement(elementName, level) -> str:
            return "\t" * (level) + f"<li><a heref = \"#\"><span>{elementName}</span></a></li>\n"
        
        output = ""
        if level == 0:
            output += "<body>\n"
            output += "\t<div class=\"tree\">\n"
            output += "\t" * 2 + f"<li><a heref = \"#\"><span>{startname}</span></a>\n"
            output += "\t" * 3 + "<ul>\n"
            #output += "\t" * 2 + "<ul>\n"
            #output += "\t" * (level + 3) + "<ul>\n"
        
        if self.IsComposite() == False: # We have reached a possible stopping point
            node = courses[self.connections]
            if node == None:
                # We have reached a stopping point
                return BuildElement(self.connections, level + 4)
            else: # Extending the tree
                output += "\t" * (level + 4) + f"<li><a heref = \"#\"><span>{self.connections}</span></a>\n"
                output += "\t" * (level + 5) + "<ul>\n"
                output += courses[self.connections].BuildHTMLTree(courses, level + 2)
                output += "\t" * (level + 5) + "</ul>\n"
                output += "\t" * (level + 4) + "</li>\n"
                if level == 0:
                    #output += "\t" * 2 + "</ul>\n"
                    output += "\t</div>\n"
                    output += "</body>"
                return output
        else:
            # output += "\t" * (level + 3) + "<ul>\n"
            output += "\t" * (level + 4) + f"<li><a heref = \"#\"><span>{str(self.connectionType)}</span></a>\n"
            output += "\t" * (level + 5) + "<ul>\n"
            for connection in self.connections:
                output += connection.BuildHTMLTree(courses, level + 2)

            output += "\t" * (level + 5) + "</ul>\n"
            output += "\t" * (level + 4) + "</li>\n"
            # output += "\t" * (level + 3) + "</ul>\n"
            # output += "\t" * (level + 2) + "</li>\n"

        if level == 0:
            output += "\t" * 3 + "</ul>\n"
            output += "\t" * 2 + "</li>\n"
            output += "\t</div>\n"
            output += "</body>"
        return output