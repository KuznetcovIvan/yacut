from random import choices

from .models import URLMap


def get_unique_short_id(chars, short_len):
    while True:
        short_id = ''.join(choices(chars, k=short_len))
        if not URLMap.query.filter_by(short=short_id).exists():
            return short_id