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
