
from typing import Callable, Dict


def encrypt(plaintext: str, shift: int) -> str:
    encrypt: Dict[str, Callable[[str, int], str]] = {
        'uppercase': lambda char, shift:
            chr((ord(char) + shift - 65) % 26 + 65),
        'lowercase': lambda char, shift:
            chr((ord(char) + shift - 97) % 26 + 97)
    }

    result = ''

    for char in plaintext:
        key = 'uppercase' if char.isupper() else 'lowercase'
        result += encrypt[key](char, shift)

    return result
