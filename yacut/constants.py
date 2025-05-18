from re import escape
from string import ascii_letters, digits

REDIRECT_VIEW = 'redirect_view'
ALLOWED_CHARS = ascii_letters + digits
PATTERN = f'^[{escape(ALLOWED_CHARS)}]+$'
MAX_SHORT_LENGTH = 16
MAX_URL_LENGTH = 2048
SHORT_LENGTH = 6
MAX_ATTEMPTS = 8
