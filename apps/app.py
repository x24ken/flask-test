from flask import Flask
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

    return app
