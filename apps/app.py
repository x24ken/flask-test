from flask import Flask


# create_app関数を作成する
def create_app():
    # Flaskクラスをインスタンス化する
    app = Flask(__name__)

    # crudパッケージからviewをimportする
    from apps.crud import views as crud_views

    # register_blueprintを使いviewのcrudをアプリへ登録する
    app.register_blueprint(crud_views.crud, url_prefix="/crud")

    return app
