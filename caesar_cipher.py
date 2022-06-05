
from typing import Callable, Dict


encrypt_char: Dict[str, Callable[[str, int], str]] = {
    'uppercase': lambda char, shift:
        chr((ord(char) + shift - 65) % 26 + 65),
    'lowercase': lambda char, shift:
        chr((ord(char) + shift - 97) % 26 + 97)
}


def encrypt(plaintext: str, shift: int) -> str:
    result = ''
    for char in plaintext:
        key = 'uppercase' if char.isupper() else 'lowercase'
        result += encrypt_char[key](char, shift) if char.isalpha() else char
    return result
