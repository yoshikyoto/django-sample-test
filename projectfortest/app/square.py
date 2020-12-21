class Square():
    def square(self, x):
        """引数 x を受け取って、 x の2乗を返す"""
        return x * x


class User:
    def __init__(self, name, status):
        self.__name = name
        self.__status = status


class Status:
    ALIVE = 1
    WITHDRAW = 2
