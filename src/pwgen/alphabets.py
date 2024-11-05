import string

BRACKETS = r"(){}[]<>"
DIGITS = string.digits
HEXDIGITS = string.hexdigits
LOWER_CASE = string.ascii_lowercase
UPPER_CASE = string.ascii_uppercase
SPACE = " "
SPECIALS = r"!\"#$%&'*+,-./:;=?@^_`|~"
PRINTABLE = (  # All of the other alphabets except SPACE
    BRACKETS + DIGITS + LOWER_CASE + UPPER_CASE + SPECIALS
)
BUILD_INS = (
    {"name": "Brackets", "alphabet": BRACKETS},
    {"name": "Digits", "alphabet": DIGITS},
    {"name": "Hex digits", "alphabet": HEXDIGITS},
    {"name": "Lower Case", "alphabet": LOWER_CASE},
    {"name": "Upper Case", "alphabet": UPPER_CASE},
    {"name": "Space", "alphabet": SPACE},
    {"name": "Specials", "alphabet": SPECIALS},
    {"name": "Printable", "alphabet": PRINTABLE},
)
