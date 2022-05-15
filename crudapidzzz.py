import flask
import json
from flask import request


app = flask.Flask(__name__)

users = [
    {
        'id': 1,
        'name':'Robert',
        'surname':'Plant'
    },
    {
        'id': 2,
        'name':'Jimmy',
        'surname':'Page'
    },
    {
        'id': 3,
        'name':'John',
        'surname':'Paul Johnes'
    },
    {
        'id': 4,
        'name':'John',
        'surname':'Bonham'
    },
]

@app.route('/')
def hello_page():
    return 'Hello'

@app.route('/users')
def get_users():
    return json.dumps(users),500

@app.route('/user/<int:user_id>',methods = ['GET','DELETE'])
def get_user(user_id):
    global users
    filtered_users = list(filter(lambda x:x['id']== user_id,users))
    if len(filtered_users) == 0:
        return "Не найдено",404
    if request.method == 'GET':
        return flask.jsonify(filtered_users[0])
    if request.method == 'DELETE':
        users = list(filter(lambda x:x['id'] == user_id,users))
        return 'Успешно удалено'


@app.route('/register',methods=['POST'])
def register():
    data = request.json
    email = data.get('email')
    if email is None and email.find('@') == -1 and email.finda != ('.') ==






if __name__ == ('__main__'):
    app.run(debug=True)

