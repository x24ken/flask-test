import logging
import os

from email_validator import EmailNotValidError, validate_email
from flask import render_template  # current_app,; g,
from flask import Flask, flash, redirect, request, url_for
from flask_debugtoolbar import DebugToolbarExtension
from flask_mail import Mail, Message

# Flaskクラスをインスタンス化する
app = Flask(__name__)
# SECRET_KEYを追加する
app.config["SECRET_KEY"] = "2AZSMss3p5QPbcY2hBsJ"
# ログレベルを設定する
app.logger.setLevel(logging.DEBUG)
# リダイレクトを中断しないようにする
app.config["DEBUG_TB_INTERCEPT_REDIRECTS"] = False
# DebugToolbarExtensionにアプリケーションをセットする
toolbar = DebugToolbarExtension(app)


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
            username = request.form["username"]
            email = request.form["email"]
            description = request.form["description"]
            print(description)
            # 入力チェック
            is_valid = True

            if not username:
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
            send_email(
                email,
                "問い合わせありがとうございました。",
                "contact_mail",
                username=username,
                description=description,
            )

            # 問い合わせ完了エンドポイントへリダイレクトする
            flash("問い合わせありがとうございました。")
            return redirect(url_for("contact_complete"))

    return render_template("contact_complete.html")


def send_email(to, subject, template, **kwargs):
    """メールを送信する関数"""
    msg = Message(subject, recipients=[to])
    msg.body = render_template(template + ".txt", **kwargs)
    msg.html = render_template(template + ".html", **kwargs)
    mail.send(msg)


app.config["MAIL_SERVER"] = os.environ.get("MAIL_SERVER")
app.config["MAIL_PORT"] = os.environ.get("MAIL_PORT")
app.config["MAIL_USE_TLS"] = os.environ.get("MAIL_USE_TLS")
app.config["MAIL_USERNAME"] = os.environ.get("MAIL_USERNAME")
app.config["MAIL_PASSWORD"] = os.environ.get("MAIL_PASSWORD")
app.config["MAIL_DEFAULT_SENDER"] = os.environ.get("MAIL_DEFAULT_SENDER")

mail = Mail(app)
