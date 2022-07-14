import flask
from flask import Flask,request
import json

app = Flask(__name__)

tasks = []

@app.route('/tasks',methods=['GET'])
def get_tasks():
    return flask.jsonify(tasks)


@app.route('/tasks', methods=['POST'])
def create_task():
    data = request.json
    if 'id' in data and 'name' in data and 'dscrptn' in data and 'ddline' in data and 'crtion_date' in data:
        name = data['name']
        if len(list(filter(lambda x : x["name"] == name,tasks))) != 0:
            return flask.jsonify({
                'code':2,
                'message':'Задача вже є у системі'
            })
        tasks.append(data)
        return flask.jsonify({
            'code':0,
            'message':'Задачу було створено'
        })
    return flask.jsonify({
        'code':1,
        'message':"Задача має обовєязкові поля такі як:ід,назва,опис,дедлайн та дата створення"
    })

@app.route('/tasks/<int:task_id>',methods=['DELETE'])
def delete_task(task_id:int):
    global tasks
    if len(tasks) >= task_id:
        tasks.pop(task_id - 1)
        return flask.jsonify({
            'code':0,
            'message':'Задачу було видалено'
        })
    return flask.jsonify({
        'code':3,
        'message':"Дану задачу не було знайдено"
    })

@app.route('/tasks/<int:task_id>',methods=['PUT'])
def update_task(task_id:int):
    global tasks
    data = request.json
    if len(tasks)>= task_id:
        if 'id' in data and 'name' in data and 'dscrptn' in data and 'ddline' in data and 'crtion_date' in data:
            tasks[task_id-1]=data
            return flask.jsonify({
                'code':0,
                'message':'Задачу було оновлено'
            })
        return flask.jsonify({
            'code': 1,
            'message': "Задача має обовєязкові поля такі як:ід,назва,опис,дедлайн та дата створення"
        })
    return flask.jsonify({
        'code': 3,
        'message': "Дану задачу не було знайдено"
    })




if __name__ == '__main__':
    app.run(debug=True)
