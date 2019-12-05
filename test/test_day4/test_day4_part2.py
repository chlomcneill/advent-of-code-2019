from unittest import TestCase

from main.day4.day4_part2 import check_double_digits_exactly


class TestDay4Part2(TestCase):

    def test_check_double_digits_exactly__correct_results(self):
        # Given
        passwords = [112233, 123444, 111122, 111111]

        # When
        results = [check_double_digits_exactly(password) for password in passwords]

        # Then
        expected_results = [True, False, True, False]
        self.assertEqual(results, expected_results)
