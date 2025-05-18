from http import HTTPStatus

from flask import abort, flash, redirect, render_template

from . import app
from .forms import URLMapForm
from .models import URLMap, URLMapCreationError


@app.route('/', methods=('GET', 'POST'))
def index_view():
    form = URLMapForm()
    if not form.validate_on_submit():
        return render_template('index.html', form=form)
    try:
        return render_template(
            'index.html',
            form=form,
            short_link=URLMap.create(
                form.original_link.data,
                form.custom_id.data or None,
                validation=False
            ).get_short_link()
        )
    except URLMapCreationError as error:
        flash(str(error))
        return render_template('index.html', form=form)


@app.route('/<short>', methods=('GET', ))
def redirect_view(short):
    url_map = URLMap.get(short) or abort(HTTPStatus.NOT_FOUND)
    return redirect(url_map.original)
