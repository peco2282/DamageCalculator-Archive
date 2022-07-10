# TheLowダメージ計算Bot
created by peco2282

discord: https://discord.gg/5t6Ubgeq6Z

[![GitHub](https://img.shields.io/github/license/peco2282/DamageCalculator-Archive)](https://github.com/peco2282/DamageCalculator-Archive/blob/main/LICENSE)
[![Github](https://img.shields.io/badge/version-1.10.0-blue.svg)](https://github.com/peco2282/DamageCalc/blob/main/main.py)
[![Discord server invice](https://discord.com/api/guilds/885757485871398985/embed.png)](https://discord.gg/5t6Ubgeq6Z)

# Usage

[Discord Developper Portal](https://discord.com/developers/applications) からBot の TOKENを入手

[mongodb](https://www.mongodb.com/)からデータベースURLを入手

`.env` ファイルに
- TOKEN: botのトークン
- GUILD_ID: 使用するサーバーのID(複数可、その場合 `, `で区切ること)
- LOG_ID: Logを出力するチャンネルID
- EXECUTE_CHANNELS: ミニゲーム(hit and blow) とテクスチャpropetiesを作成するチャンネルを入力(複数可)
- MONGO_DB_URL: 上で入手したMongo-urlを入力


### ローカルPCで動かす場合
 
```shell
$git clone https://github.com/peco2282/DamageCalculator-Archive.git
$pip install -U git+https://github.com/Pycord-Development/pycord
$pip install -U pytz requests motor dnspython
```

すべてインストール完了したのち、

```shell
$python3 main.py
```

### herokuサーバーで動かすとき

[ここ](https://qiita.com/peco_2282/items/8fe9d65a673f278111e2) を参照。
