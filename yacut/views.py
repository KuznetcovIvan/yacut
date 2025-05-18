from flask import redirect, render_template, url_for

from . import app, db
from .constants import ALLOWED_CHARS, SHORT_LENGTH, REDIRECT_VIEW
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
        'index.html',
        form=form,
        short_url=url_for(REDIRECT_VIEW, short=url_map.short, _external=True)
    )


@app.route('/<short>', methods=('GET', ))
def redirect_view(short):
    return redirect(
        URLMap.query.filter_by(short=short).first_or_404().original
    )