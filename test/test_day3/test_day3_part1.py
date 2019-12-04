from unittest import TestCase

from main.day3.day3_part1 import find_closest_intersection

class TestDay3Part1(TestCase):

    def test_find_closest_intersection__correct_results(self):
        # Given
        wires1 = [
            ['R8','U5','L5','D3'],
            ['U7','R6','D4','L4']
        ]
        wires2 = [
            ['R75','D30','R83','U83','L12','D49','R71','U7','L72'],
            ['U62','R66','U55','R34','D71','R55','D58','R83']
        ]
        wires3 = [
            ['R98','U47','R26','D63','R33','U87','L62','D20','R33','U53','R51'],
            ['U98','R91','D20','R16','D67','R40','U7','R15','U6','R7']
        ]

        # When
        result1 = find_closest_intersection(wires1)
        result2 = find_closest_intersection(wires2)
        result3 = find_closest_intersection(wires3)

        # Then
        expected_result1 = 6
        expected_result2 = 159
        expected_result3 = 135

        self.assertEqual(result1, expected_result1)
        self.assertEqual(result2, expected_result2)
        self.assertEqual(result3, expected_result3)