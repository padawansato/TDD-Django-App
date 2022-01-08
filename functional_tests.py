from selenium import webdriver
#Optionsクラスのインポート（ヘッドレスの設定をするため）
from selenium.webdriver.chrome.options import Options

#Optionsのインスタンスを生成（変数optionsに格納）
options = Options()

#headlessの設定をTrueにする
options.headless = True

#webdriverの起動
browser = webdriver.Chrome(options=options)

# エディスさんはクールな To-Do アプリの話を聞き、
# 彼女はホームページをチェックしに行った。
browser.get('http://localhost:8000')

# 彼女はページタイトルとヘッダーが To-Do に言及している事に気づいた。
assert 'To-Do' in browser.title

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

browser.quit()