from unittest import TestCase

from main.day7.day7_part1 import find_best_amplifier_combination


class TestDay7Part1(TestCase):

    def test_find_best_amplifier_combination__corrects_results(self):
        # Given
        programs = [
            [3,15,3,16,1002,16,10,16,1,16,15,15,4,15,99,0,0],
            [3,23,3,24,1002,24,10,24,1002,23,-1,23,101,5,23,23,1,24,23,23,4,23,99,0,0],
            [3,31,3,32,1002,32,10,32,1001,31,-2,31,1007,31,0,33,1002,33,7,33,1,33,31,31,1,32,31,31,4,31,99,0,0,0]
        ]

        # When
        results = [find_best_amplifier_combination(0, program) for program in programs]

        # Then
        expected_results = [43210, 54321, 65210]
        self.assertEqual(results, expected_results)
