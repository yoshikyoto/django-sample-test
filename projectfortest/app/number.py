from app.square import Square

class Number():
    """数字を扱うクラス"""

    def __init__(self, x):
        self.x = x

    def get_square(self):
        """2乗の値を返す"""
        square = Square()
        return square.square(self.x)
