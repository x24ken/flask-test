# flaskbook
![image](https://user-images.githubusercontent.com/25762625/166855040-39f0cd6b-5644-4d4a-9a22-1b8caeab4f94.png)


## Git Clone

githubからプロジェクトをclone

```
$ git clone https://github.com/x24ken/flaskbook
```

flaskbookフォルダーに移動

```
> cd flaskbook
```

## 仮想環境の設定(Windows)

まずWindowsPowerShellで次のコマンドを実行する。

```
> PowerShell Set-ExecutionPolicy RemoteSigned CurrentUser
```

仮想環境の実行

```
> py -m venv venv
> venv\Scripts\Activate.ps1
```

仮想環境の終了

```
> desctivate
```

## 環境変数ファイルの設置

`flaskbook/.env`ファイルを作成し、次の内容を`.env`ファイルに書き込む

```
FLASK_APP=apps.app:create_app('local')
FLASK_ENV=development
```

## パッケージのインストール

`requirements.txt`に書いてあるライブラリをインストール

```
(venv) $ pip install -r requirements.txt
```

## DBマイグレート

Python上のモデルから、実際のデータベースへの「変換」

```
(venv) $ flask db init
(venv) $ flask db migrate
(venv) $ flask db upgrade
```

## 学習済みモデルを取得

```
(venv) $ python
>>> import torch
>>> import torchvision
>>> model = torchvision.models.detection.maskrcnn_resnet50_fpn(pretrained=True)
>>> torch.save(model, "model.pt")
```

`model.pt`を`apps/detector`配下へ移動する

## アプリケーション起動

```
(venv) $ flask run
```

## テスト実行

```
$ pytest tests/detector
```

