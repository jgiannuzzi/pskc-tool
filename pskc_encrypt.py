#!/usr/bin/env -S pipenv run python

import argparse
import getpass

import pskc


def main():
    parser = argparse.ArgumentParser(
        description='Encrypt PSKC file with a PBKDF2 passphrase')
    parser.add_argument('input', type=pskc.PSKC,
                        help='Path to the input PSKC file')
    parser.add_argument('output', help='Path to the output PSKC file')
    parser.add_argument('-p', '--passphrase', type=argparse.FileType('r'),
                        help='Path to a file containing the passphrase')
    args = parser.parse_args()

    if args.passphrase is not None:
        passphrase = args.passphrase.read().strip()
    else:
        passphrase = getpass.getpass('Passphrase: ')

    args.input.encryption.setup_pbkdf2(password=passphrase)
    args.input.write(args.output)


if __name__ == '__main__':
    main()
