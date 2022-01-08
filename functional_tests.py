from unittest.main import main
from selenium import webdriver
#Optionsクラスのインポート（ヘッドレスの設定をするため）
from selenium.webdriver.chrome.options import Options
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        #Optionsのインスタンスを生成（変数optionsに格納）
        self.options = Options()
        #headlessの設定をTrueにする
        self.options.headless = True
        #webdriverの起動
        self.browser = webdriver.Chrome(options=self.options)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        """
        ユーザはリストを作成し、後に取得することができる。
        """
        # エディスさんはクールな To-Do アプリの話を聞き、
        # 彼女はホームページをチェックしに行った。
        self.browser.get('http://localhost:8000')

        # 彼女はページタイトルとヘッダーが To-Do に言及している事に気づいた。
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # 早速、To-Do アプリへ項目を入力したくなる。

        # テキストボックスに「孔雀の羽毛を買う」と入力する
        # (エディスの趣味は、羽で釣りのルアーを作ること。)

        # エンターキーを押すと、ページが更新され、次のようなことが表示される。
        # To-Do リストの項目「1: 孔雀の羽毛を買う」

        # まだテキストボックスは残っていて、項目を追加できる。
        # 彼女は「孔雀の羽を使ってルアーを作る」と入力した。(彼女は几帳面だ)

        # 再びページが更新され、リストの2つの項目が表示された。

        # エディスは、サイトが自分のリストを記憶しているか疑問に思った。
        # そしてサイトが自分用のユニークなURLを生成している事を確認しました。
        # (その説明文が表示されている。)

        # 満足した彼女は眠りにつく。

if __name__ == '__main__':
    unittest.main(warnings='ignore')