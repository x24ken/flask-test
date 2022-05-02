from flask import Flask, render_template
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect

from apps.config import config

# SQLAlchemyをインスタンス化する
db = SQLAlchemy()
# CSRF対策をインスタンス化する
csrf = CSRFProtect()

# LoginManagerをインスタンス化する
login_manager = LoginManager()
# login_view属性に未ログイン時にリダイレクトするエンドポイントを指定する
login_manager.login_view = "auth.signup"
# login_manage属性にログイン後に表示するメッセージを指定する
# ここでは何も表示しないように空を指定する
login_manager.login_message = ""


# コンフィグキーを渡す
def create_app(config_key):
    # Flaskクラスをインスタンス化する
    app = Flask(__name__)

    # config_keyにマッチする環境のコンフィグクラスを読み込む
    app.config.from_object(config[config_key])

    # SQLAlchemyとアプリを連携する
    db.init_app(app)
    # Migrateとアプリを連携する
    Migrate(app, db)
    # CSRFProtectとアプリを連携する
    csrf.init_app(app)
    # login_managerとアプリをれんけいする
    login_manager.init_app(app)

    # crudパッケージからviewsをimportする
    from apps.crud import views as crud_views

    # register_blueprintを使いviewのcrudをアプリへ登録する
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    # authパッケージからviewsをimportする
    from apps.auth import views as auth_views

    # register_blueprintを使いviewのauthをアプリへ登録する
    app.register_blueprint(auth_views.auth, url_prefix="/auth")

    # detectorパッケージからviewsをimportする
    from apps.detector import views as dt_views

    # register_blueprintを使いviewsのdtをアプリへ登録する
    app.register_blueprint(dt_views.dt)

    # カスタムエラー画面を登録する
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(500, internal_server_error)

    return app


# 登録したエンドポイント名の関数を作成し、404や500が発生した際に指定したHTMLを返す
def page_not_found(e):
    """404 Not Found"""
    return render_template("404.html"), 404


def internal_server_error(e):
    """500 Internal Server Error"""
    return render_template("500.html"), 500
