from datetime import datetime
from random import choices
from re import fullmatch

from flask import url_for

from . import db
from .constants import (
    ALLOWED_CHARS,
    MAX_ATTEMPTS,
    MAX_SHORT_LENGTH,
    MAX_URL_LENGTH,
    PATTERN,
    REDIRECT_VIEW,
    SHORT_LENGTH
)
from .error_handlers import ShortError


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(MAX_URL_LENGTH), nullable=False)
    short = db.Column(
        db.String(MAX_SHORT_LENGTH), index=True, unique=True, nullable=False
    )
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    @staticmethod
    def get(short):
        return URLMap.query.filter_by(short=short).first()

    @staticmethod
    def get_short_link(short):
        return url_for(REDIRECT_VIEW, short=short, _external=True)

    @staticmethod
    def create(original, short):
        if short:
            if URLMap.query.filter_by(short=short).first():
                raise ShortError(
                    'Предложенный вариант короткой ссылки уже существует.'
                )
            if not fullmatch(PATTERN, short) or len(short) > MAX_SHORT_LENGTH:
                raise ShortError(
                    'Указано недопустимое имя для короткой ссылки'
                )
        else:
            for _ in range(MAX_ATTEMPTS):
                short = ''.join(choices(ALLOWED_CHARS, k=SHORT_LENGTH))
                if not URLMap.get(short):
                    break
            else:
                raise ShortError(
                    'Не удалось сгенерировать имя для короткой ссылки'
                )
        url_map = URLMap(original=original, short=short)
        db.session.add(url_map)
        db.session.commit()
        return url_map
