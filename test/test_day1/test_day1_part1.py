from unittest import TestCase

from main.day1.day1part1 import calculate_fuel


class TestDay1Part1(TestCase):

    def test_calculate_fuel__correct_result(self):
        # Given
        masses = [12, 14, 1969, 100756]

        # When
        fuels = [calculate_fuel(mass) for mass in masses]

        # Then
        expected_fuels = [2, 2, 654, 33583]
        self.assertEqual(fuels, expected_fuels)







# def test_get_elasticache_reservation_rows(self):
#     # Given
#     data = [
#         {
#             "ReservedCacheNodeId": "1",
#             "StartTime": dt.datetime(2019, 1, 11),
#             "Duration": 31536000,
#             "State": "active",
#             "CacheNodeType": "t2"
#         },
#         {
#             "ReservedCacheNodeId": "2",
#             "StartTime": dt.datetime(2018, 1, 11),
#             "Duration": 31536000,
#             "State": "retired",
#             "CacheNodeType": "t2"
#         }
#     ]
#     # When
#     elasticache_rows = bdh.get_elasticache_reservation_rows(data)
#     # Then
#     self.assertListEqual([self.elasticache_row_1, self.elasticache_row_2], elasticache_rows)