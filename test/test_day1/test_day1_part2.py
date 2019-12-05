from unittest import TestCase

from main.day1.day1_part2 import calculate_fuel, calculate_total_fuel


class TestDay1Part2(TestCase):

    def test_calculate_fuel__correct_results(self):
        # Given
        masses = [12, 14, 1969, 100756]

        # When
        fuels = [calculate_fuel(mass) for mass in masses]

        # Then
        expected_fuels = [2, 2, 654, 33583]
        self.assertEqual(fuels, expected_fuels)

    def test_calculate_total_fuel__correct_results(self):
        # Given
        masses = [14, 1969, 100756]

        # When
        total_fuels = [calculate_total_fuel(mass) for mass in masses]

        # Then
        expected_total_fuels = [2, 966, 50346]
        self.assertEqual(total_fuels, expected_total_fuels)
