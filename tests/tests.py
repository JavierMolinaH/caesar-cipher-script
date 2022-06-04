import sys
from typing import Any, List
from caesar import Caesar

from unittest import TestCase
from unittest.mock import patch


class CaesarTest(TestCase):
    @staticmethod
    def cipher_process(
        testargs: List[Any],
        input_value: str,
        expected_result: str
    ) -> None:
        with patch.object(sys, 'argv', testargs):
            with patch('builtins.input', return_value=input_value):
                caesar = Caesar()
                caesar.encrypt_phrase()

                with patch('builtins.print') as mocked_print:
                    caesar.print_plaintext()
                    mocked_print.assert_called_with(
                        f'plaintext: {input_value}'
                    )

                with patch('builtins.print') as mocked_print:
                    caesar.print_ciphertext()
                    mocked_print.assert_called_with(
                        f'ciphertext: {expected_result}'
                    )

    def test_hello_phrase(self):
        testargs = [None, 1]
        input_value = 'HELLO'
        expected_result = 'IFMMP'
        self.cipher_process(testargs, input_value, expected_result)

    def test_a_list_of_words(self):
        testargs = [None, 13]
        input_value = 'hello, world'
        expected_result = 'uryyb, jbeyq'
        self.cipher_process(testargs, input_value, expected_result)

    def test_large_phrase(self):
        testargs = [None, 13]
        input_value = 'be sure to drink your Ovaltine'
        expected_result = 'or fher gb qevax lbhe Binygvar'
        self.cipher_process(testargs, input_value, expected_result)

    def test_without_command_line_argument_error(self):
        testargs = [None]
        with patch.object(sys, 'argv', testargs):
            with patch('builtins.input'):
                Caesar()

    def test_more_than_one_command_line_arguments_error(self):
        testargs = [None, 1, 2, 3, 4, 5]
        with patch.object(sys, 'argv', testargs):
            with patch('builtins.input'):
                Caesar()

    def test_negative_command_line_argument_error(self):
        testargs = [None, -1]
        with patch.object(sys, 'argv', testargs):
            with patch('builtins.input'):
                Caesar()
