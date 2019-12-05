from unittest import TestCase

from main.day4.day4_part1 import check_password, check_length, check_increasing, check_double_digits


class TestDay4Part1(TestCase):

    def test_check_length__correct_results(self):
        # Given
        passwords = [12345, 123456, 11, 111111]

        # When
        results = [check_length(password) for password in passwords]

        # Then
        expected_results = [False, True, False, True]
        self.assertEqual(results, expected_results)

    def test_check_double_digits__correct_results(self):
        # Given
        passwords = [123456, 112233, 112345, 453423]

        # When
        results = [check_double_digits(password) for password in passwords]

        # Then
        expected_results = [False, True, True, False]
        self.assertEqual(results, expected_results)

    def test_check_increasing__correct_results(self):
        # Given
        passwords = [123456, 122222, 123123, 124590]

        # When
        results = [check_increasing(password) for password in passwords]

        # Then
        expected_results = [True, True, False, False]
        self.assertEqual(results, expected_results)

    def test_check_password__correct_results(self):
        # Given
        passwords = [122345, 111111, 223450, 123789, 11234]

        # When
        results = [check_password(password) for password in passwords]

        # Then
        expected_results = [True, True, False, False, False]
        self.assertEqual(results, expected_results)
