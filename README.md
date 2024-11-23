# pwgen - Yet another password generator.

## Description

Utility for creating passwords with certain complexity.
The generator randomly picks N number of characters from each of the chosen alphabets.
A custom alphabet can be specified.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install pwgen.

```bash
pip install pwgen
```

## Usage

usage: pwgen [-h] [-a] [-n N] [-c N ALPHABET] [-b N] [-d N] [-e EXCLUDE] [-l N] [-u N] [-s N] [-x N] [-p N] [--version]

Utility for creating passwords with certain complexity. Defaults will create a password of length 12 picked from the 'printable' alphabet

options:
-h, --help show this help message and exit
-a, --alphabets display build-in alphabets
-n N, --number N number of passwords to produce. Default is one,
-c N ALPHABET, --custom N ALPHABET
pick N number of characters from this specified ALPHABET
-b N, --brackets N pick N number of characters from the 'brackets' alphabet
-d N, --digits N pick N number of characters from the 'digits' alphabet
-e EXCLUDE, --exclude EXCLUDE
specify characters to exclude from passwords
-l N, --lower N pick N number of characters from the 'lower case' alphabet
-u N, --upper N pick N number of characters from the 'upper case' alphabet
-s N, --special N pick N number of characters from the 'special' alphabet
-x N, --hexdigits N pick N number of characters from the 'hexadecimal digits' alphabet
-p N, --printable N pick N number of characters from any of the alphabets
--version show program's version number and exit

## License

[MIT](https://choosealicense.com/licenses/mit/)
