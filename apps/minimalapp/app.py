from email_validator import EmailNotValidError, validate_email
from flask import render_template  # current_app,; g,
from flask import Flask, flash, redirect, request, url_for

# Flaskクラスをインスタンス化する
app = Flask(__name__)
# SECRET_KEYを追加する
app.config["SECRET_KEY"] = "2AZSMss3p5QPbcY2hBsJ"


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
            print(description)
            # 入力チェック
            is_valid = True

            if not user_name:
                flash("ユーザー名は必須です")
                is_valid = False

            if not email:
                flash("メールアドレスは必須です")
                is_valid = False

            try:
                validate_email(email)
            except EmailNotValidError:
                flash("メールアドレスの形式で入力してください")
                is_valid = False

            if not is_valid:
                return redirect(url_for("contact"))

            # メールを送る

            # 問い合わせ完了エンドポイントへリダイレクトする
            flash("問い合わせありがとうございました。")
            return redirect(url_for("contact_complete"))

    return render_template("contact_complete.html")
