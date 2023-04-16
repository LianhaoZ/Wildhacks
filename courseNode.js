const ConnectionType = require("./connectionType")

class CourseNode {
    constructor(connections = null, connectionType = ConnectionType.NoConnection) {
        this.connections = [];
        // We love dynamic languages :c
        if (connections !== null) {
            if (typeof connections === "string") {
                this.connections = connections;
            } else {
                if (connectionType !== ConnectionType.NoConnection) { // This is a composite node, therefore will only have nodes as children
                    for (const connection of connections) {
                        if (connection instanceof CourseNode) {
                            this.connections.push(connection);
                        } else if (typeof connection === "string") {
                            const node = new CourseNode();
                            node.connections = connection;
                            this.connections.push(node);
                        } else {
                            throw new Error("Connections can only be CourseNodes or course names!");
                        }
                    }
                } else {
                    this.connections = connections; // This is not a composite node, and therefore will be stored as a string
                }
            }
        }
        this.connectionType = connectionType;
    }

    GetType() {
        return this.connectionType;
    }

    GetConnections() {
        return this.connections;
    }

    // A node is composite when it is comprised of at least one non-composite node
    // If the node simply holds a courseName as its connection, then it is not composite
    IsComposite() {
        return this.connectionType !== ConnectionType.NoConnection;
    }

    BuildHTMLTree(courses, level = 0, startname = "") {
        const buildElement = (elementName, level) => {
            return "\t".repeat(level) + `<li><a href=\"#\"><span>${elementName}</span></a></li>\n`;
        };

        let output = "";
        if (level === 0) {
            output += "<body>\n";
            output += "\t<div class=\"tree\">\n";
            output += "\t".repeat(2) + `<li><a href="#"><span>${startname}</span></a>\n`;
            output += "\t".repeat(3) + "<ul>\n";
        }

        if (this.IsComposite() === false) { // We have reached a possible stopping point
            const node = courses[this.connections];
            if (node === null) {
                // We have reached a stopping point
                return buildElement(this.connections, level + 4);
            } else { // Extending the tree
                output += "\t".repeat(level + 4) + `<li><a href="#"><span>${this.connections}</span></a>\n`;
                output += "\t".repeat(level + 5) + "<ul>\n";
                output += node.BuildHTMLTree(courses, level + 2);
                output += "\t".repeat(level + 5) + "</ul>\n";
                output += "\t".repeat(level + 4) + "</li>\n";
                if (level === 0) {
                    output += "\t</div>\n";
                    output += "</body>";
                }
                return output;
            }
        } else {
            output += "\t".repeat(level + 4) + `<li><a href="#"><span>${this.connectionType.toString()}</span></a>\n`;
            output += "\t".repeat(level + 5) + "<ul>\n";
            for (const connection of this.connections) {
                output += connection.BuildHTMLTree(courses, level + 2);
            }
            output += "\t".repeat(level + 5) + "</ul>\n";
            output += "\t".repeat(level + 4) + "<li>\n";
        }

        if (level == 0)
        {
            output += "\t".repeat(3) + "</ul>\n";
            output += "\t".repeat(2) + "</li>\n";
            output += "\t</div>\n";
            output += "</body>";
        }

        return output;
    }
}

module.exports.CourseNode = CourseNode