from flask import Flask

# Flaskクラスをインスタンス化する
app = Flask(__name__)

# URLと実行関数をマッピングする
@app.route("/")  # デコレーションが使われてる
def index():
    return "Hello, Flaskbook!"
