# 元となるdockerイメージを指定
# M1 は `selenium/standalone-chrome` が使えないため
FROM seleniarm/standalone-chromium:4.0.0-20211213
# FROM django_tdd_web

# 管理者ユーザ docker の設定
RUN sudo useradd -m docker && echo "docker:docker" | sudo chpasswd && sudo adduser docker sudo
USER docker
# USER $HOME_USER

# この環境変数に値を入れることでバッファを無効化する('1'じゃなくてもいい)
ENV PYTHONUNBUFFERED 1
# codeディレクトリを作成
RUN sudo mkdir /code
# codeディレクトリに移動
WORKDIR /code
# txtファイルをcodeディレクトリに配置
COPY requirements.txt /code/

# パッケージインストーラ
# requirements.system に対象パッケージ記入
COPY requirements.system /tmp/requirements.system
RUN sudo apt-get update \
    && sudo xargs apt-get install -y --no-install-recommends \
        < /tmp/requirements.system \
    && sudo apt-get -y clean \
    && sudo rm -rf /var/lib/apt/lists/*
# pipコマンドを最新にし、txtファイル内のパッケージをpipインストール
RUN sudo pip install --upgrade pip \
    && sudo pip install -r requirements.txt

# sample-pj/配下のファイルをcodeディレクトリにコピー
COPY . /code/

CMD "/bin/bash"