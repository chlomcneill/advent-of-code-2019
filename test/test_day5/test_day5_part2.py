# from unittest import TestCase
#
# from main.day5.day5_part2 import process_program
#
#
# class TestDay5Part2(TestCase):
#
#     def test_process_program__correct_results(self):
#         # Given
#         programs1 = [
#             [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8],
#             [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8],
#             [3, 3, 1108, -1, 8, 3, 4, 3, 99],
#             [3, 3, 1107, -1, 8, 3, 4, 3, 99]
#         ]
#
#         programs2 = [
#             [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9],
#             [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1]
#         ]
#
#         program3 = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31, 1106, 0, 36, 98, 0, 0, 1002, 21,
#                     125, 20, 4, 20, 1105, 1, 46, 104, 999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
#
#         # When
#         results1_1 = [process_program(8, program) for program in programs1]
#         results1_2 = [process_program(7, program) for program in programs1]
#         results1_3 = [process_program(9, program) for program in programs1]
#
#         results2_1 = [process_program(0, program) for program in programs2]
#         results2_2 = [process_program(1, program) for program in programs2]
#
#         results3_1 = process_program(8, program3)
#         results3_2 = process_program(7, program3)
#         results3_3 = process_program(9, program3)
#
#         # Then
#         expected_results1_1 = [1,1,1,1]
#         expected_results1_2 = [0,1,0,1]
#         expected_results1_3 = [0,0,0,0]
#
#         expected_results2_1 = [0, 0]
#         expected_results2_2 = [1, 1]
#
#         expected_results3_1 = 1000
#         expected_results3_2 = 999
#         expected_results3_3 = 1001
#
#         self.assertEqual(results1_1, expected_results1_1)
#         self.assertEqual(results1_2, expected_results1_2)
#         self.assertEqual(results1_3, expected_results1_3)
#         self.assertEqual(results2_1, expected_results2_1)
#         self.assertEqual(results2_2, expected_results2_2)
#         self.assertEqual(results3_1, expected_results3_1)
#         self.assertEqual(results3_2, expected_results3_2)
#         self.assertEqual(results3_3, expected_results3_3)
#
#
