from unittest import TestCase

from main.day6.day6_part1 import calculate_orbits


class TestDay5Part2(TestCase):

    def test_calculate_orbits__corrects_results(self):
        # Given
        orbits = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']

        # When
        result = calculate_orbits(orbits)

        # Then
        expected_result = 42
        self.assertEqual(result, expected_result)
