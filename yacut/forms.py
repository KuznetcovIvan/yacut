from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import URL, DataRequired, Length, Optional, Regexp

from .constants import MAX_LENGTH, PATTERN


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Длинная ссылка',
        validators=(
            DataRequired(message='Это обязательное поле!'),
            URL(message='Введите корректный URL!')
        )
    )
    custom_id = StringField(
        'Ваш вариант короткой ссылки',
        validators=(
            Length(1, MAX_LENGTH),
            Optional(),
            Regexp(PATTERN, message='Только латинские буквы и цифры!')
        )
    )
    submit = SubmitField('Создать')
