import caesar_cipher
from unittest import TestCase


class CaesarCipherTest(TestCase):
    def test_output_only_alphabetic_characters(self):
        self.assertEqual(caesar_cipher.encrypt('A', 27), 'B')

    def test_preserve_uppercase(self):
        self.assertEqual(caesar_cipher.encrypt('A', 1), 'B')

    def test_preserve_lowercase(self):
        self.assertEqual(caesar_cipher.encrypt('a', 1), 'b')
