from django.test import TestCase
from app.square import Square

# Create your tests here.

class SquareTest(TestCase):
    def test_square(self):
        square = Square()

        # 2の2乗は4
        result = square.square(2)
        self.assertEqual(result, 4)

        # 3の2乗は9
        result = square.square(3)
        self.assertEqual(result, 9)

from app.number import Number

class NumberTest(TestCase):
    """Number クラスのテスト"""

    def test_get_square(self):
        # 2に対して get_square すると 4 になる
        number = Number(2)
        self.assertEqual(number.get_square(), 4)

        # 3に対して get_square すると 9 になる
        number = Number(3)
        self.assertEqual(number.get_square(), 9)
