from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional, Regexp

from .constants import MAX_LENGTH, PATTERN


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Введите длинную ссылку',
        validators=(
            DataRequired(message='Обязательное поле')
        )
    )
    custom_id = StringField(
        'Введите свой вариант идентификатора короткой сслыки',
        validators=(
            Length(1, MAX_LENGTH),
            Optional(),
            Regexp(PATTERN, message='Только латинские буквы и цифры')
        )
    )
    submit = SubmitField(
        'Создать'
    )