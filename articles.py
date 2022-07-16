import flask
from flask import request
from core import config
from crud.articles import article_crud
from datetime import datetime


article_api = flask.Blueprint('artice api',__name__)


@article_api.get(config.API_ROUTE_PREFIX + '/articles')
def get_arcticles():
    return flask.jsonify({
        'code':1,
        'message':'OK',
        'data':flask.jsonify(article_crud.get_all())
    })

@article_api.get(config.API_ROUTE_PREFIX + '/articles/<id>')
def get_arcticle(id):
    return flask.jsonify({
        'code':1,
        'message':'OK',
        'data':flask.jsonify(article_crud.get_one(id))
    })
@article_api.post((config.API_ROUTE_PREFIX + '/articles'))
def create_article():
    if 'title' not in request.json or 'content' not in request.json or 'author' not in request.json:
        return flask.jsonify({
            'code':9,
            'message':"Дата та автор є обов'язковими",
            'data':None
        })
    request.json['created_at'] = datetime.now().strftime('Y%-m%-d% H%:&:S%')
    return flask.jsonify({
        'code': 0,
        'message': 'OK',
        'data': article_crud.create(request.json)
    })

@article_api.put(config.API_ROUTE_PREFIX + '/articles/<id>')
def update_article(id):
    if 'title' not in request.json or 'content' not in request.json or 'author' not in request.json:
        return flask.jsonify({
            'code':9,
            'message':"Дата та автор є обов'язковими",
            'data':None
        })
    return flask.jsonify({
        'code':0,
        'message':'OK',
        'data':flask.jsonify(article_crud.update(id))
    })

@article_api.delete(config.API_ROUTE_PREFIX + '/articles/<id>')
def delete_article(id):
    return flask.jsonify({
        'code':0,
        'message':'Ok',
        'data':flask.jsonify(article_crud.delete(id))
    })

if __name__ == '__main__':
    article_api.run(debug=True)