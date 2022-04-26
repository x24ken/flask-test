from flask import Flask, current_app, g, redirect, render_template, request, url_for

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


# 問い合わせフォーム
@app.route("/contact")
def contact():
    return render_template("contact.html")


# 問い合わせ完了フォーム
@app.route("/contact/complete", methods=["GET", "POST"])
def contact_complete():
    if request.method == "POST":
        if request.method == "POST":
            # form属性を使ってフォームの値を取得する
            user_name = request.form["username"]
            email = request.form["email"]
            description = request.form["description"]
            # メールを送る

            return redirect(url_for("contact_complete"))

    return render_template("contact_complete.html")
