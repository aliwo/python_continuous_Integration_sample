from unittest import TestCase


class TestObvious(TestCase):
    def test_1_더하기_1은_2(self) -> None:
        # Given
        num_1 = 1
        num_2 = 1

        # When
        귀요미 = num_1 + num_2

        # Then
        self.assertEqual(귀요미, 2)
