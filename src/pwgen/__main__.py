#!/usr/bin/env python3

import argparse
import sys

import pwgen


def display_alphabets():
    print("Available alphabets")
    for alphabet in pwgen.alphabets.BUILD_INS:
        print(f'{alphabet["name"]:<15}: \'{alphabet["alphabet"]}\'')


def main():
    DEFAULT_PASSWORD_LENGTH = 12

    num_of_brackets = 0
    num_of_custom = 0
    num_of_digits = 0
    num_of_hexdigits = 0
    num_of_lower = 0
    num_of_upper = 0
    num_of_special = 0
    num_of_printable = 0
    num_of_passwords = 1
    custom_alphabet = ""
    exclude = ""

    parser = argparse.ArgumentParser(
        prog="pwgen",
        description="Utility for creating passwords with certain complexity. \
        Defaults will create a password of length 12 picked from the \
        'printable' alphabet",
    )

    parser.add_argument(
        "-a", "--alphabets", action="store_true", help="display build-in alphabets"
    )
    parser.add_argument(
        "-n",
        "--number",
        type=int,
        metavar="N",
        help="number of passwords to produce. Default is one,",
    )
    parser.add_argument(
        "-c",
        "--custom",
        nargs=2,
        metavar=("N", "ALPHABET"),
        help="pick N number of characters from this specified ALPHABET",
    )
    parser.add_argument(
        "-b",
        "--brackets",
        type=int,
        metavar="N",
        help="pick N number of characters from the 'brackets' alphabet",
    )
    parser.add_argument(
        "-d",
        "--digits",
        type=int,
        metavar="N",
        help="pick N number of characters from the 'digits' alphabet",
    )
    parser.add_argument(
        "-e",
        "--exclude",
        type=str,
        help="specify characters to exclude from passwords",
    )
    parser.add_argument(
        "-l",
        "--lower",
        type=int,
        metavar="N",
        help="pick N number of characters from the 'lower case' alphabet",
    )
    parser.add_argument(
        "-u",
        "--upper",
        type=int,
        metavar="N",
        help="pick N number of characters from the 'upper case' alphabet",
    )
    parser.add_argument(
        "-s",
        "--special",
        type=int,
        metavar="N",
        help="pick N number of characters from the 'special' alphabet",
    )
    parser.add_argument(
        "-x",
        "--hexdigits",
        type=int,
        metavar="N",
        help="pick N number of characters from the 'hexadecimal digits'\
        alphabet",
    )
    parser.add_argument(
        "-p",
        "--printable",
        type=int,
        metavar="N",
        help="pick N number of characters from any of the alphabets",
    )
    args = parser.parse_args()

    if args.alphabets:
        display_alphabets()
        sys.exit(0)

    password_length = 0

    if args.brackets is not None:
        num_of_brackets = args.brackets
        password_length += num_of_brackets

    if args.digits is not None:
        num_of_digits = args.digits
        password_length += num_of_digits

    if args.hexdigits is not None:
        num_of_hexdigits = args.hexdigits
        password_length += num_of_hexdigits

    if args.lower is not None:
        num_of_lower = args.lower
        password_length += num_of_lower

    if args.upper is not None:
        num_of_upper = args.upper
        password_length += num_of_upper

    if args.special is not None:
        num_of_special = args.special
        password_length += num_of_special

    if args.printable is not None:
        num_of_printable = args.printable
        password_length += num_of_printable

    if args.number is not None:
        num_of_passwords = args.number

    if args.custom is not None:
        num_of_custom, custom_alphabet = args.custom
        num_of_custom = int(num_of_custom)
        password_length += num_of_custom

    if args.exclude is not None:
        exclude = args.exclude

    if password_length == 0:
        num_of_printable = DEFAULT_PASSWORD_LENGTH

    for _ in range(0, num_of_passwords):
        passwd = pwgen.generate(
            brackets=num_of_brackets,
            digits=num_of_digits,
            hexdigits=num_of_hexdigits,
            lower_case=num_of_lower,
            upper_case=num_of_upper,
            printable=num_of_printable,
            specials=num_of_special,
            custom=num_of_custom,
            custom_alphabet=custom_alphabet,
            exclude=exclude,
        )
        print(passwd)


if __name__ == "__main__":
    main()
