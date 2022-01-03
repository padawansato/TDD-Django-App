from selenium import webdriver
#Optionsクラスのインポート（ヘッドレスの設定をするため）
from selenium.webdriver.chrome.options import Options

#Optionsのインスタンスを生成（変数optionsに格納）
options = Options()

#headlessの設定をTrueにする
options.headless = True

#webdriverの起動
browser = webdriver.Chrome(options=options)
browser.get('http://localhost:8000')

assert 'Django' in browser.title