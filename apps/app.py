from pathlib import Path

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

# SQLAlchemyをインスタンス化する
db = SQLAlchemy()


# create_app関数を作成する
def create_app():
    # Flaskクラスをインスタンス化する
    app = Flask(__name__)
    # アプリのコンフィグを設定する
    app.config.from_mapping(
        SECRET_KEY="2AZSMss3p5QPbcY2hBsJ",
        SQLALCHEMY_DATABASE_URI=(
            f"sqlite:///{Path(__file__).parent.parent / 'local.sqlite'}"
        ),
        SQLALCHEMY_TRACK_MODIFICATIONS=False,
        # SQLをコンソールログに出力する設定
        SQLALCHEMY_ECHO=True,
    )

    # SQLAlchemyとアプリを連携する
    db.init_app(app)
    # Migrateとアプリを連携する
    Migrate(app, db)

    # crudパッケージからviewをimportする
    from apps.crud import views as crud_views

    # register_blueprintを使いviewのcrudをアプリへ登録する
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    return app
