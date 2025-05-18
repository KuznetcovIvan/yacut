from http import HTTPStatus

from flask import abort, redirect, render_template

from . import app
from .error_handlers import ShortError
from .forms import URLMapForm
from .models import URLMap


@app.route('/', methods=('GET', 'POST'))
def index_view():
    form = URLMapForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    try:
        url_map = URLMap.create(
            form.original_link.data, form.custom_id.data or None
        )
    except ShortError as error:
        form.custom_id.errors.append(str(error))
        return render_template('index.html', form=form)
    return render_template(
        'index.html',
        form=form,
        short_link=URLMap.get_short_link(url_map.short)
    )


@app.route('/<short>', methods=('GET', ))
def redirect_view(short):
    url_map = URLMap.get(short) or abort(HTTPStatus.NOT_FOUND)
    return redirect(url_map.original)
