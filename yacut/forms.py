from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp, URL

from .constants import MAX_LENGTH, PATTERN


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=(
            DataRequired(message='Обязательное поле'),
            URL(message='Введите корректный URL')
        )
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=(
            Length(1, MAX_LENGTH),
            Optional(),
            Regexp(PATTERN, message='Только латинские буквы и цифры')
        )
    )
    submit = SubmitField(
        'Создать'
    )