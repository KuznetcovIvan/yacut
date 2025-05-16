from http import HTTPStatus
from flask import jsonify, request

from . import app, db
from .models import URLMap
from .utils import get_unique_short_id
from .error_handlers import InvalidAPIUsage
