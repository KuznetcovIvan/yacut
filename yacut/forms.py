from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp

from .constants import MAX_SHORT_LENGTH, MAX_URL_LENGTH, PATTERN

ORIGINAL_LABEL = 'Длинная ссылка'
SHORT_LABEL = 'Ваш вариант короткой ссылки'
SUBMIT_LABEL = 'Создать'

REQUIRED_MESSAGE = 'Это обязательное поле!'
URL_MESSAGE = 'Введите корректный URL!'
REGEXP_MESSAGE = 'Только латинские буквы и цифры!'


class URLMapForm(FlaskForm):
    original_link = URLField(
        ORIGINAL_LABEL,
        validators=(
            Length(max=MAX_URL_LENGTH),
            DataRequired(message=REQUIRED_MESSAGE),
            URL(message=URL_MESSAGE)
        )
    )
    custom_id = StringField(
        SHORT_LABEL,
        validators=(
            Length(max=MAX_SHORT_LENGTH),
            Optional(),
            Regexp(PATTERN, message=REGEXP_MESSAGE)
        )
    )
    submit = SubmitField(SUBMIT_LABEL)
