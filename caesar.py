#!/usr/bin/env python
import sys

import caesar_cipher


class Caesar:
    def __init__(self) -> None:
        self.get_sys_arguments()
        self.get_input_plaintext()

    def get_sys_arguments(self) -> None:
        if len(sys.argv) == 1:
            self.print_errors(
                'No command line argument was provided 4 "shift".'
            )
            exit(1)
        if len(sys.argv) > 2:
            self.print_errors(
                'Too many command line arguments.'
            )
            exit(1)
        self.shift = int(sys.argv[1])

    def get_input_plaintext(self) -> None:
        self.plaintext = input('Enter message to encrypt:\n')

    def print_plaintext(self) -> None:
        print(f'plaintext: {self.plaintext}')

    def print_ciphertext(self) -> None:
        print(f'ciphertext: {self.result}')

    def print_errors(self, errorMessage: str):
        print(f'Error: {errorMessage}')

    def encrypt_phrase(self):
        self.result = caesar_cipher.encrypt(self.plaintext, self.shift)

    def run(self) -> None:
        self.encrypt_phrase()
        self.print_plaintext()
        self.print_ciphertext()


if __name__ == '__main__':
    Caesar().run()
