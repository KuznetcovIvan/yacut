from flask import redirect, render_template

from . import app, db
from .constants import ALLOWED_CHARS, SHORT_LENGTH
from .forms import URLMapForm
from .models import URLMap
from .utils import get_unique_short_id


@app.route('/', methods=('GET', 'POST'))
def index_view():
    form = URLMapForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    short = form.custom_id.data or None
    if short and URLMap.query.filter_by(short=short).first():
        form.custom_id.errors.append(
            'Предложенный вариант короткой ссылки уже существует.'
        )
        return render_template('index.html', form=form)
    url_map = URLMap(
        original=form.original_link.data,
        short=short or get_unique_short_id(ALLOWED_CHARS, SHORT_LENGTH)
    )
    db.session.add(url_map)
    db.session.commit()
    return render_template(
        'index.html', form=form, url_map=url_map
    )


@app.route('/<short_id>', methods=('GET', ))
def redirect_view(short_id):
    return redirect(
        URLMap.query.filter_by(short=short_id).first_or_404().original
    )