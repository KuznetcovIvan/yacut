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


SHORT_EXISTS = 'Предложенный вариант короткой ссылки уже существует.'
INVALID_SHORT = 'Указано недопустимое имя для короткой ссылки'
GENERATION_FAILED = 'Не удалось сгенерировать имя для короткой ссылки'
URL_TOO_LONG = 'Превышен максимальный размер URL'


class URLMapCreationError(Exception):
    """Исключение для ошибок, связанных с созданием
    или валидацией экземпляра URLMap"""


class URLMap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original = db.Column(db.String(MAX_URL_LENGTH), nullable=False)
    short = db.Column(
        db.String(MAX_SHORT_LENGTH), index=True, unique=True, nullable=False
    )
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def get_short_link(self):
        return url_for(REDIRECT_VIEW, short=self.short, _external=True)

    @staticmethod
    def get(short):
        return URLMap.query.filter_by(short=short).first()

    @staticmethod
    def create(original, short, validation=True):
        if short:
            if URLMap.get(short):
                raise URLMapCreationError(SHORT_EXISTS)
            if (
                validation
                and (len(short) > MAX_SHORT_LENGTH
                     or not fullmatch(PATTERN, short))
            ):
                raise URLMapCreationError(INVALID_SHORT)
        else:
            for _ in range(MAX_ATTEMPTS):
                short = ''.join(choices(ALLOWED_CHARS, k=SHORT_LENGTH))
                if not URLMap.get(short):
                    break
            else:
                raise URLMapCreationError(GENERATION_FAILED)
        if validation and (len(original) > MAX_URL_LENGTH):
            raise URLMapCreationError(URL_TOO_LONG)
        url_map = URLMap(original=original, short=short)
        db.session.add(url_map)
        db.session.commit()
        return url_map
