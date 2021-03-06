from django.test import Client
from app.number import Number
from app.models import SampleModel
from unittest.mock import MagicMock
from django.test import TestCase
from app.square import Square
from testfixtures import compare


# Create your tests here.


class SquareTest(TestCase):

    def setUp(self):
        # print("setUp")
        pass

    def tearDown(self):
        # print("tearDown")
        pass

    def test_compare(self):
        # print("test compare")
        a = {"a": 1, "b": 2}
        b = {"a": 1, "b": 3}
        # self.assertEqual(a, b)
        # compare(a, b)

    def test_square(self):
        # rint("test square")
        square = Square()

        # 2の2乗は4
        result = square.square(2)
        self.assertEqual(result, 4)

        # 3の2乗は9
        result = square.square(3)
        self.assertEqual(result, 9)


class NumberTest(TestCase):
    """Number クラスのテスト"""

    def test_get_square(self):
        # モック作成
        square_mock = MagicMock()

        # square メソッドが呼ばれたら 4 を返す
        square_mock.square.return_value = 4

        # モックを注入した number オブジェクトを作成
        number = Number(2, square=square_mock)

        # get_square メソッドは、 square_mock の結果をそのまま返す
        self.assertEqual(number.get_square(), 4)

        # square オブジェクトの square メソッドが
        # 1回、正しく呼ばれていることを確認
        self.assertEqual(square_mock.square.call_count, 1)

        # 1回目（call_args_list[0]）に関数が呼ばれる時の
        #  x 引数（0番目の引数 args[0]）の値は 2
        args, kwargs = square_mock.square.call_args_list[0]
        self.assertEqual(args[0], 2)


class SampleModelTest(TestCase):
    fixtures = ['sample_model_fixture.yaml']

    def test_get(self):
        result = SampleModel.objects.all()
        self.assertEqual(len(result), 1)
        self.assertEqual(result[0].name, "サンプルモデル")


class RequestTest(TestCase):
    def test_request(self):
        c = Client()
        response = c.get('/test/')
        self.assertEqual(200, response.status_code)
        # print(response.content)
