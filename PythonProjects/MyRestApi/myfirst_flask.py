from flask import Flask, jsonify

app = Flask(__name__)


courses = [
            {"name" : "Python certificate",
             "price" : 3000,
             "course_id" : 0
            },
            {"name": "java certificate",
            "price": 4000,
            "course_id": 1
            },
            {"name": "data science certificate",
            "price": 10000,
            "course_id": 2
            },
            {"name": "c certificate",
            "price": 5000,
            "course_id": 3
             }
]


@app.route('/')
def index():
    return "welcome to the course api"

@app.route("/courses", methods = ['GET'])
def get():
    return jsonify({'courses':courses})

@app.route("/courses/<int:course_id>", methods = ['GET'])
def get_course_id(course_id):
    return jsonify({'courses':courses[course_id]})

@app.route("/courses", methods = ['POST'])
def create():
    course = {"name": "DOT certificate",
            "price": 5000,
            "course_id": 4
             }
    courses.append(course)
    return jsonify({'Created':courses})

if __name__ == "__main__":
    app.run(debug=True)
