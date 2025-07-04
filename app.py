# Flask（フラスク）という軽量なWebフレームワークをインポートします
# Flaskは、Pythonで簡単にWebアプリケーションを作るためのツールです
from flask import Flask

# Flaskアプリケーションのインスタンス（実体）を作成します
# __name__は現在のファイル名を表す特殊な変数です
app = Flask(__name__)

# ルート（経路）を定義します
# @app.route()はデコレーターと呼ばれる特殊な記法です
# '/'はWebサイトのトップページ（ホームページ）を意味します
@app.route('/')
def hello_world():
    """
    この関数は、ユーザーがトップページにアクセスしたときに実行されます
    return文で返した文字列がブラウザに表示されます
    """
    # HTMLを使って、リンク付きのページを作成します
    html = """
    <h1>こんにちはセカイ</h1>
    <p>このサイトには以下のページがあります：</p>
    <ul>
        <li><a href="/hello">こんにちはページ</a> - シンプルな挨拶を表示します</li>
        <li><a href="/goodnight">おやすみページ</a> - おやすみの挨拶を表示します</li>
    </ul>
    """
    return html

# '/hello'というURLにアクセスしたときに実行される関数を定義します
@app.route('/hello')
def hello():
    """
    この関数は、ユーザーが/helloページにアクセスしたときに実行されます
    シンプルに「こんにちは」と表示します
    """
    return 'こんにちは'

# '/goodnight'というURLにアクセスしたときに実行される関数を定義します
@app.route('/goodnight')
def goodnight():
    """
    この関数は、ユーザーが/goodnightページにアクセスしたときに実行されます
    「おやすみ」と表示します
    """
    return 'おやすみ'

# このファイルが直接実行された場合のみ、以下のコードが実行されます
# 他のファイルからインポートされた場合は実行されません
if __name__ == '__main__':
    # Flaskアプリケーションを起動します
    # debug=Trueにすると、コードを変更したときに自動的にサーバーが再起動します
    # 本番環境では必ずdebug=Falseにしてください
    app.run(debug=True, host='0.0.0.0', port=5000)
    # host='0.0.0.0'は、どのIPアドレスからでもアクセスできるようにする設定です
    # port=5000は、5000番ポートでサーバーを起動する設定です