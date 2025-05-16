from datetime import datetime

from . import db
from .constants import MAX_LENGTH


class URLMap(db.Model):
    id = db.Column(
        db.Integer, primary_key=True
    )
    original = db.Column(
        db.Text, nullable=False
    )
    short = db.Column(
        db.String(MAX_LENGTH), index=True, unique=True, nullable=False
    )
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow
    )

    def to_dict(self):
        return dict(url=self.original, short_link=self.short)

    def from_dict(self, data):
        if 'url' in data:
            self.original = data['url']
        if 'short_link' in data:
            self.short = data['short_link']
        return self
