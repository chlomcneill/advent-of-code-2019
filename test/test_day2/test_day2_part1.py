from unittest import TestCase

from main.day2.day2_part1 import run_program


class TestDay2Part1(TestCase):

    def test_run_program__correct_results(self):
        # Given
        programs = [
            [1,9,10,3,2,3,11,0,99,30,40,50],
            [1,0,0,0,99],
            [2,3,0,3,99],
            [2,4,4,5,99,0],
            [1,1,1,4,99,5,6,0,99]
        ]

        # When
        results = [run_program(program) for program in programs]

        # Then
        expected_results = [
            [3500,9,10,70,2,3,11,0,99,30,40,50],
            [2,0,0,0,99],
            [2, 3, 0, 6,99],
            [2,4,4,5,99,9801],
            [30,1,1,4,2,5,6,0,99]
        ]
        self.assertEqual(results, expected_results)