from http import HTTPStatus
from re import fullmatch

from flask import jsonify, request

from . import app, db
from .constants import ALLOWED_CHARS, MAX_LENGTH, PATTERN, SHORT_LENGTH
from .error_handlers import InvalidAPIUsage
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/api/id/', methods=('POST', ))
def create_short_link():
    data = request.get_json(silent=True)
    if data is None:
        raise InvalidAPIUsage('Отсутствует тело запроса')
    url = data.get('url')
    if url is None:
        raise InvalidAPIUsage('"url" является обязательным полем!')
    custom_id = data.get('custom_id')
    if custom_id:
        if not fullmatch(PATTERN, custom_id) or len(custom_id) > MAX_LENGTH:
            raise InvalidAPIUsage(
                'Указано недопустимое имя для короткой ссылки'
            )
        if URLMap.query.filter_by(short=custom_id).first():
            raise InvalidAPIUsage(
                'Предложенный вариант короткой ссылки уже существует.'
            )
    url_map = URLMap(
        original=url,
        short=custom_id or get_unique_short_id(ALLOWED_CHARS, SHORT_LENGTH)
    )
    db.session.add(url_map)
    db.session.commit()
    return jsonify({
        'url': url_map.original,
        'short_link': request.host_url + url_map.short
    }), HTTPStatus.CREATED


@app.route('/api/id/<short_id>/', methods=('GET', ))
def get_original_link(short_id):
    url_map = URLMap.query.filter_by(short=short_id).first()
    if url_map is None:
        raise InvalidAPIUsage('Указанный id не найден', HTTPStatus.NOT_FOUND)
    return jsonify({'url': url_map.original})