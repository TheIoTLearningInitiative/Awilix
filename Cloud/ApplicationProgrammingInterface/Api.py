#!flask/bin/python
from flask import Flask, jsonify

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Task One',
        'description': u'This is task one', 
        'done': False
    },
    {
        'id': 2,
        'title': u'Task Two',
        'description': u'This is task two', 
        'done': False
    }
]

@app.route('/api/v1.0/tasks', methods=['GET'])
def tasksget():
    return jsonify({'tasks': tasks})

if __name__ == '__main__':
    app.run(debug=True)
