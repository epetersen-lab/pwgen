import secrets

from . import alphabets


def reorder(s: str) -> str:
    reordered = ""
    indices = [i for i in range(len(s))]
    while indices:
        chosen = secrets.choice(indices)
        indices.remove(chosen)
        reordered += s[chosen]
    return reordered


def pick_from_alphabet(alphabet: str, length: int) -> str:
    return "".join(secrets.choice(alphabet) for _ in range(length))


def generate(
    brackets=0,
    digits=0,
    hexdigits=0,
    lower_case=0,
    upper_case=0,
    printable=0,
    spaces=0,
    specials=0,
    custom=0,
    custom_alphabet="",
) -> str:
    password = ""
    if brackets:
        password += pick_from_alphabet(alphabets.BRACKETS, brackets)
    if digits:
        password += pick_from_alphabet(alphabets.DIGITS, digits)
    if hexdigits:
        password += pick_from_alphabet(alphabets.HEXDIGITS, hexdigits)
    if lower_case:
        password += pick_from_alphabet(alphabets.LOWER_CASE, lower_case)
    if upper_case:
        password += pick_from_alphabet(alphabets.UPPER_CASE, upper_case)
    if printable:
        password += pick_from_alphabet(alphabets.PRINTABLE, printable)
    if spaces:
        password += pick_from_alphabet(alphabets.SPACE, spaces)
    if specials:
        password += pick_from_alphabet(alphabets.SPECIALS, specials)
    if custom:
        password += pick_from_alphabet(custom_alphabet, custom)

    return reorder(password)
