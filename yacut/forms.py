from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, URLField
from wtforms.validators import DataRequired, Length, Optional


class URLMapForm(FlaskForm):
    original_link = URLField(
        'Введите длинную ссылку',
        validators=(DataRequired(message='Обязательное поле'))
    )
    custom_id = StringField(
        'Введите Ваш вариант идентификатора короткой сслыки',
        validators=(Length(1, 16), Optional())
    )
    submit = SubmitField(
        'Создать'
    )