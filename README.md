# このプログラムはなに？

**四柱推命の命式を HTML で出力するプログラム**です。

プログラムを実行すると、次のような GUI が表示されます。

![命式生成ウィンドウ](https://user-images.githubusercontent.com/7956282/223109871-e9943e1e-f8db-4b76-8d16-36fd10388a40.png)

生年月日、生まれた時間、性別を入力して「命式生成」をクリックすると、ブラウザが自動的に起動して次のような命式が表示されます。

![生成された命式](https://user-images.githubusercontent.com/7956282/223111152-37f4f841-4d0f-46e3-a11e-e627e1bd8578.png)


# 動作を確認した環境

- macOS Sonoma 14.4
- Python 3.12.2

# 使い方
```
$ source ./local_python/bin/activate
(local_python)$ make install
(local_python)$ make
(local_python)$ deactivate
```

# Windows で exe 化する場合の手順

下記のコマンドで customtkinter のインストールパスを確認します。
```
$ pip show customtkinter
```
次に、以下のコマンドで exe 化します。
```
$ pyinstaller --onefile --noconsole --add-data "<確認したインストールパス>\customtkinter;customtkinter\" meishiki_gui.py
```
うまく命式が出力されない場合は、```--noconsole``` オプションを外してエラーメッセージを確認しましょう。
