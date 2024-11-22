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


def pick_from_alphabet(alphabet: str, length: int, exclude: str) -> str:
    for c in exclude:
        alphabet = alphabet.replace(c, "")
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
    exclude="",
) -> str:
    password = ""
    if brackets:
        password += pick_from_alphabet(alphabets.BRACKETS, brackets, exclude)
    if digits:
        password += pick_from_alphabet(alphabets.DIGITS, digits, exclude)
    if hexdigits:
        password += pick_from_alphabet(alphabets.HEXDIGITS, hexdigits, exclude)
    if lower_case:
        password += pick_from_alphabet(alphabets.LOWER_CASE, lower_case, exclude)
    if upper_case:
        password += pick_from_alphabet(alphabets.UPPER_CASE, upper_case, exclude)
    if printable:
        password += pick_from_alphabet(alphabets.PRINTABLE, printable, exclude)
    if spaces:
        password += pick_from_alphabet(alphabets.SPACE, spaces, exclude)
    if specials:
        password += pick_from_alphabet(alphabets.SPECIALS, specials, exclude)
    if custom:
        password += pick_from_alphabet(custom_alphabet, custom, exclude)

    return reorder(password)
