from unittest import TestCase

from main.day1.day1_part1 import calculate_fuel


class TestDay1Part1(TestCase):

    def test_calculate_fuel__correct_result(self):
        # Given
        masses = [12, 14, 1969, 100756]

        # When
        fuels = [calculate_fuel(mass) for mass in masses]

        # Then
        expected_fuels = [2, 2, 654, 33583]
        self.assertEqual(fuels, expected_fuels)
