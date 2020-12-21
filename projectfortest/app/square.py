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


class Service:

    def exec(self, parameter):
        log = open('logfile.txt', 'w')
        try:
            # エラーの調査がしやすいように parameter を
            # ログに出しておく
            log.info("リクエスト内容")
            log.info(parameter)

            # API リクエストをする
            result = api.getHogehoge(parameter)
            return result
        except Error as e:
            # Error の内容をログファイルに出す
            # e の中には、APIからどのようなエラーが返ってきたのかが
            # 入っているとする
            log.error("リクエスト中にエラーが発生")
            log.error(e)

            # エラー画面を表示する処理
            return "エラーが発生しました"
