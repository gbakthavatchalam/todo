import json
import pymysql.cursors
from chalice import Chalice

CONNECTION_STRING = {
        "host": "todo.cylxcbpu6bdo.ap-south-1.rds.amazonaws.com",
        "user": "todo",
        "password": "todo1234",
        "db": "todo"
}

INSERT = "INSERT INTO TASK (`NAME`, `DESC`, `STATUS`, `DUE_DATE`) VALUES ('{name}', '{desc}', '{status}', {date})"
SELECT_ALL = "SELECT `ID`, `NAME`, `DESC`, `STATUS`, `DUE_DATE` FROM task"
SELECT_ONE = "SELECT `ID`, `NAME`, `DESC`, `STATUS`, `DUE_DATE` FROM task WHERE id = {id}"


app = Chalice(app_name='todo')
db = pymysql.connect(**CONNECTION_STRING)


@app.route('/')
def index():
    return {'hello': 'world'}


@app.route('/tasks', methods=["GET"], cors=True)
def get_tasks():
    """Get the list of all tasks"""
    with db.cursor() as cursor:
        cursor.execute(SELECT_ALL)
        tasks = []
        keys = ('id', 'name', 'desc', 'status', 'due_date')
        for row in cursor.fetchall(): # Fetch as dictionary
            dct = dict(zip(keys, row))
            dct['due_date'] = str(dct['due_date'])
            tasks.append(dct)
        print(tasks)
        return tasks


@app.route('/tasks/{id}', methods=["GET"])
def get(task_id):
    """Get a task by Id"""
    pass

@app.route('/tasks/add', methods=['POST'])
def add_task():
    """Can use a forms and orm layer like wtforms and sqlalchemy to perform validation and provide querying mechanism. Due to lack of time, going 
    ahead with raw queries"""
    request = app.current_request
    details = request.json_body
     
# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
