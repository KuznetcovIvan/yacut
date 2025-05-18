from string import ascii_letters, digits

REDIRECT_VIEW = 'redirect_view'
ALLOWED_CHARS = ascii_letters + digits
PATTERN = f'^[{ALLOWED_CHARS}]+$'
MAX_LENGTH = 16
SHORT_LENGTH = 6
