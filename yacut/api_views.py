from http import HTTPStatus

from flask import jsonify, request

from . import app
from .error_handlers import InvalidAPIUsage, ShortError
from .models import URLMap

NO_REQUEST_BODY = 'Отсутствует тело запроса'
URL_REQUIRED = '"url" является обязательным полем!'
ID_NOT_FOUND = 'Указанный id не найден'


@app.route('/api/id/', methods=('POST', ))
def create_short_link():
    data = request.get_json(silent=True)
    if data is None:
        raise InvalidAPIUsage(NO_REQUEST_BODY)
    original = data.get('url')
    if original is None:
        raise InvalidAPIUsage(URL_REQUIRED)
    try:
        url_map = URLMap.create(original, data.get('custom_id'))
    except ShortError as error:
        raise InvalidAPIUsage(str(error))
    return jsonify({
        'url': url_map.original,
        'short_link': URLMap.get_short_link(url_map.short)
    }), HTTPStatus.CREATED


@app.route('/api/id/<short>/', methods=('GET', ))
def get_original_link(short):
    url_map = URLMap.get(short)
    if url_map is None:
        raise InvalidAPIUsage(ID_NOT_FOUND, HTTPStatus.NOT_FOUND)
    return jsonify({'url': url_map.original})
