from flask import Flask, current_app, g, render_template, request, url_for

# Flaskクラスをインスタンス化する
app = Flask(__name__)


# URLと実行関数をマッピングする
@app.route("/")  # デコレーションが使われてる
def index():
    return "Hello, Flaskbook!"


# Postメソッドで変数を送れる
@app.route("/hello/<name>", methods=["GET", "POST"], endpoint="hello-endpoint")
def hello(name):
    return f"Hello, {name}"


# テンプレートの利用
@app.route("/name/<name>")
def show_name(name):
    return render_template("index.html", name=name)


with app.test_request_context():
    # /
    print(url_for("index"))
    # /hello/world
    print(url_for("hello-endpoint", name="world"))
    # /name/ichiro?page=1
    print(url_for("show_name", name="ichiro", page="1"))

with app.test_request_context("/users?updated=true"):
    # trueが出力される
    print(request.args.get("updated"))

ctx = app.app_context()
ctx.push()

print(current_app.name)

g.connection = "connection"
print(g.connection)
