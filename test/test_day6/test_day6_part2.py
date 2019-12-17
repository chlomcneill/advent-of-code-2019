from unittest import TestCase

from main.day6.day6_part2 import calculate_minimum_orbital_transfers


class TestDay5Part2(TestCase):

    def test_calculate_orbits__corrects_results(self):
        # Given
        orbits = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L', 'K)YOU', 'I)SAN']

        # When
        result = calculate_minimum_orbital_transfers(orbits)

        # Then
        expected_result = 4
        self.assertEqual(result, expected_result)