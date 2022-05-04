from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, length


# ユーザー新規作成とユーザー編集フォームクラス
class UserForm(FlaskForm):
    # ユーザーフォームのusername属性のラベルとバリデータを設定する
    username = StringField(
        "ユーザー名",
        validators=[
            DataRequired(message="ユーザー名は必須です。 "),
            length(max=30, message="30文字以内で入力してください。"),
        ],
    )
    # ユーザーフォームpassword属性のラベルとバリデータを設定する
    password = PasswordField("パスワード", validators=[DataRequired(message="パスワードは必須です。 ")])

    # ユーザーフォームsubmitの文言を設定する
    submit = SubmitField("新規登録")
