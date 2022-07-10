import discord
from discord.ext import commands

url = "https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB"
job_list = [
    'ノービス'
]


# 魔根設定！！！！！！！！！！！！！！！！！！！
async def embed_list_skill(ctx: commands.Context, dmg, raw, os, osraw, r, alpha, makon=1.0):  # dmg: 魔法石込み
    embed_1 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(),
                            url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                            description=f"**職業：ノービス**")

    embed_1.set_author(name=ctx.author.name)

    embed_1.add_field(name='条件',
                      value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n魔法石倍率：{alpha}倍')

    embed_1.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                      value=f'メテオストライク (スペシャル)：**__{dmg * 9 * osraw:.3f}__**\n'
                            f'マジックボール (ノーマル)**：__{dmg * 4 * osraw:.3f}__**, '
                            f'**(詠唱時：__{dmg * 8 * osraw:.3f})__**\n'
                            f'ライトニングボルト (ノーマル)：**__{dmg * 3 * osraw:.3f}__**\n'
                            f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                      inline=False)

    embed_1.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                      value=f'ショックストーン (スペシャル)：**__{dmg * 7 * osraw:.3f}__**'
                            f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * osraw:.3f}__**', inline=False)

    embed_1.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                      value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{dmg * 1.1 * 7 * osraw:.3f}__**'
                            f'\n雪柱 (ノーマル)：**__{dmg * 4 * osraw:.3f}__**', inline=False)

    embed_1.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                      value=f'オーバーシュート (スペシャル)：**__{dmg * 12.5 * osraw:.3f}__, '
                            f'パッシブあり：__{dmg * 12.5 * 1.5 * osraw:.3f}__**'
                            f'\nシャドウパワー (ノーマル)：**__{dmg * 1.5 * osraw:.3f}__**'
                            f'\nエレメンタルパワー	(パッシブ)：**__{dmg * 1.5 * osraw:.3f}__**',
                      inline=False)

    embed_1.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                      value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * osraw:.3f}__**', inline=False)

    embed_1.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                      value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{dmg * 8 * osraw:.3f}**__')

    embed_1.add_field(name='**聖剣 (In 浮世の砂海)**',
                      value=f'下克上 (パッシブ)：**__ボスmob {dmg * 1.07 * osraw:.3f} / 通常mob {dmg * 0.7 * osraw:.3f}__**',
                      inline=False)

    # ソルジャー
    embed_2 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(),
                            url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                            description=f"**職業：ソルジャー**")

    embed_2.set_author(name=ctx.author.name)

    embed_2.add_field(name='条件',
                      value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n魔法石倍率：{alpha}倍')

    embed_2.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                      value=f'メテオストライク (スペシャル)：**__{dmg * 9 * 0.98 * (osraw - 0.02):.3f}__**\n'
                            f'マジックボール (ノーマル)**：__{dmg * 4 * (osraw - 0.02):.3f}__**, '
                            f'**(詠唱時：__{dmg * 8 * (osraw - 0.02):.3f}__**)'
                            f'\nライトニングボルト (ノーマル)：**__{dmg * 3 * 0.98 * (osraw - 0.02):.3f}__**\n'
                            f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                      inline=False)

    embed_2.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                      value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osraw + 0.05):.3f}__**'
                            f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osraw + 0.05):.3f}__**',
                      inline=False)

    embed_2.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                      value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{dmg * 1.1 * 7 * (osraw - 0.02):.3f}__**'
                            f'\n雪柱 (ノーマル)：**__{dmg * 4 * (osraw - 0.02):.3f}__**',
                      inline=False)

    embed_2.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                      value=f'オーバーシュート (スペシャル)：**__{dmg * 12.5 * (osraw - 0.02):.3f}__, '
                            f'パッシブあり：__{dmg * 12.5 * 1.5 * (osraw - 0.02):.3f}__**'
                            f'\nシャドウパワー (ノーマル)：**__{dmg * 1.5 * (osraw - 0.02):.3f}__**'
                            f'\nエレメンタルパワー	(パッシブ)：**__{dmg * 1.5 * (osraw - 0.02):.3f}__**',
                      inline=False)

    embed_2.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                      value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osraw + 0.05):.3f}__**',
                      inline=False)

    embed_2.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                      value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{dmg * 8 * (osraw - 0.02):.3f}**__')

    embed_2.add_field(name='**聖剣 (In 浮世の砂海)**',
                      value=f'下克上 (パッシブ)：**__ボスmob {dmg * 1.07 * (osraw + 0.05):.3f} / 通常mob {dmg * 0.7 * (osraw + 0.05):.3f}__**',
                      inline=False)

    # アーチャー
    embed_3 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(),
                            url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                            description=f"**職業：アーチャー**")

    embed_3.set_author(name=ctx.author.name)

    embed_3.add_field(name='条件',
                      value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n魔法石倍率：{alpha}倍')

    embed_3.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                      value=f'メテオストライク (スペシャル)：**__{dmg * 9 * (osraw - 0.02):.3f}__**\n'
                            f'マジックボール (ノーマル)**：__{dmg * 4 * (osraw - 0.02):.3f}__**, '
                            f'**(詠唱時：__{dmg * 8 * (osraw - 0.02):.3f}__**)'
                            f'\nライトニングボルト (ノーマル)：**__{dmg * 3 * (osraw - 0.02):.3f}__**\n'
                            f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                      inline=False)

    embed_3.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                      value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osraw - 0.02):.3f}__**'
                            f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osraw - 0.02):.3f}__**',
                      inline=False)

    embed_3.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                      value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{dmg * 1.1 * 7 * (osraw + 0.05):.3f}__**'
                            f'\n雪柱 (ノーマル)：**__{dmg * 4 * (osraw + 0.05):.3f}__**',
                      inline=False)

    embed_3.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                      value=f'オーバーシュート (スペシャル)：**__{dmg * 12.5 * (osraw + 0.05):.3f}__, '
                            f'パッシブあり：__{dmg * 12.5 * 1.5 * (osraw + 0.05):.3f}__**'
                            f'\nシャドウパワー (ノーマル)：**__{dmg * 1.5 * (osraw + 0.05):.3f}__**'
                            f'\nエレメンタルパワー	(パッシブ)：**__{dmg * 1.5 * (osraw + 0.05):.3f}__**',
                      inline=False)

    embed_3.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                      value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osraw - 0.02):.3f}__**',
                      inline=False)

    embed_3.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                      value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{dmg * 8 * (osraw + 0.05):.3f}**__')

    embed_3.add_field(name='**聖剣 (In 浮世の砂海)**',
                      value=f'下克上 (パッシブ)：**__ボスmob {dmg * 1.07 * (osraw - 0.02):.3f} / 通常mob {dmg * 0.7 * (osraw - 0.02):.3f}__**',
                      inline=False)

    # マジシャン
    embed_4 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(),
                            url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                            description=f"**職業：マジシャン**")

    embed_4.set_author(name=ctx.author.name)

    embed_4.add_field(name='条件',
                      value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n魔法石倍率：{alpha}倍')

    embed_4.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                      value=f'メテオストライク (スペシャル)：**__{dmg * 9 * (osraw + 0.05):.3f}__**\n'
                            f'マジックボール (ノーマル)**：__{dmg * 4 * (osraw + 0.05):.3f}__**, '
                            f'**(詠唱時：__{dmg * 8 * (osraw + 0.05):.3f}__**)'
                            f'\nライトニングボルト (ノーマル)：**__{dmg * 3 * (osraw + 0.05):.3f}__**\n'
                            f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                      inline=False)

    embed_4.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                      value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osraw - 0.02):.3f}__**'
                            f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osraw - 0.02):.3f}__**',
                      inline=False)

    embed_4.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                      value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{dmg * 7 * 1.1 * (osraw - 0.02):.3f}__**'
                            f'\n雪柱 (ノーマル)：**__{dmg * 4 * (osraw - 0.02):.3f}__**',
                      inline=False)

    embed_4.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                      value=f'オーバーシュート (スペシャル)：**__{dmg * 12.5 * (osraw - 0.02):.3f}__, '
                            f'パッシブあり：__{dmg * 12.5 * 1.5 * (osraw - 0.02):.3f}__**'
                            f'\nシャドウパワー (ノーマル)：**__{dmg * 1.5 * (osraw - 0.02):.3f}__**'
                            f'\nエレメンタルパワー	(パッシブ)：**__{dmg * 1.5 * (osraw - 0.02):.3f}__**',
                      inline=False)

    embed_4.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                      value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osraw - 0.02):.3f}__**',
                      inline=False)

    embed_4.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                      value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{dmg * 8 * (osraw - 0.02):.3f}**__')

    embed_4.add_field(name='**聖剣 (In 浮世の砂海)**',
                      value=f'下克上 (パッシブ)：**__ボスmob {dmg * 1.07 * (osraw - 0.02):.3f} / 通常mob {dmg * 0.7 * (osraw - 0.02):.3f}__**',
                      inline=False)

    # ウォーリア
    embed_5 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(),
                            url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                            description=f"**職業：ウォーリア**")

    embed_5.set_author(name=ctx.author.name)

    embed_5.add_field(name='条件',
                      value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n魔法石倍率：{alpha}倍')

    embed_5.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                      value=f'メテオストライク (スペシャル)：**__{dmg * 9 * (osraw - 0.05):.3f}__**\n'
                            f'マジックボール (ノーマル)**：__{dmg * 4 * (osraw - 0.05):.3f}__**, '
                            f'**(詠唱時：__{dmg * 8 * (osraw - 0.05):.3f}__**)'
                            f'\nライトニングボルト (ノーマル)：**__{dmg * 3 * (osraw - 0.05):.3f}__**\n'
                            f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                      inline=False)

    embed_5.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                      value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osraw + 0.10):.3f}__**'
                            f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osraw + 0.10):.3f}__**',
                      inline=False)

    embed_5.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                      value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{dmg * 1.1 * 7 * (osraw - 0.05):.3f}__**'
                            f'\n雪柱 (ノーマル)：**__{dmg * 4 * (osraw - 0.05):.3f}__**',
                      inline=False)

    embed_5.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                      value=f'オーバーシュート (スペシャル)：**__{dmg * 12.5 * (osraw - 0.05):.3f}__, '
                            f'パッシブあり：__{dmg * 12.5 * 1.5 * (osraw - 0.05):.3f}__**'
                            f'\nシャドウパワー (ノーマル)：**__{dmg * 1.5 * (osraw - 0.05):.3f}__**'
                            f'\nエレメンタルパワー	(パッシブ)：**__{dmg * 1.5 * (osraw - 0.05):.3f}__**',
                      inline=False)

    embed_5.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                      value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osraw + 0.10):.3f}__**',
                      inline=False)

    embed_5.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                      value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{dmg * 8 * (osraw - 0.05):.3f}**__')

    embed_5.add_field(name='**聖剣 (In 浮世の砂海)**',
                      value=f'下克上 (パッシブ)：**__ボスmob {dmg * 1.07 * (osraw + 0.10):.3f} / 通常mob {dmg * 0.7 * (osraw + 0.10):.3f}__**',
                      inline=False)

    # ボウマン
    embed_6 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(),
                            url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                            description=f"**職業：ボウマン**")

    embed_6.set_author(name=ctx.author.name)

    embed_6.add_field(name='条件',
                      value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n魔法石倍率：{alpha}倍')

    embed_6.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                      value=f'メテオストライク (スペシャル)：**__{dmg * 9 * (osraw - 0.05):.3f}__**\n'
                            f'マジックボール (ノーマル)**：__{dmg * 4 * (osraw - 0.05):.3f}__**, '
                            f'**(詠唱時：__{dmg * 8 * (osraw - 0.05):.3f}__**)'
                            f'\nライトニングボルト (ノーマル)：**__{dmg * 3 * (osraw - 0.05):.3f}__**\n'
                            f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                      inline=False)

    embed_6.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                      value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osraw - 0.05):.3f}__**'
                            f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osraw - 0.05):.3f}__**',
                      inline=False)

    embed_6.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                      value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{dmg * 1.1 * 7 * (osraw + 0.10):.3f}__**'
                            f'\n雪柱 (ノーマル)：**__{dmg * 4 * (osraw + 0.10):.3f}__**',
                      inline=False)

    embed_6.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                      value=f'オーバーシュート (スペシャル)：**__{dmg * 12.5 * (osraw + 0.10):.3f}__, パッシブあり：__{dmg * 12.5 * 1.5 * (osraw + 0.10):.3f}__**'
                            f'\nシャドウパワー (ノーマル)：**__{dmg * 1.5 * (osraw + 0.10):.3f}__**'
                            f'\nエレメンタルパワー	(パッシブ)：**__{dmg * 1.5 * (osraw + 0.10):.3f}__**',
                      inline=False)

    embed_6.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                      value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osraw - 0.05):.3f}__**',
                      inline=False)

    embed_6.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                      value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{dmg * 8 * (osraw + 0.10):.3f}**__')

    embed_6.add_field(name='**聖剣 (In 浮世の砂海)**',
                      value=f'下克上 (パッシブ)：**__ボスmob {dmg * 1.07 * (osraw - 0.05):.3f} / 通常mob {dmg * 0.7 * (osraw - 0.05):.3f}__**',
                      inline=False)

    # メイジ
    embed_7 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(),
                            url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                            description=f"**職業：メイジ**")

    embed_7.set_author(name=ctx.author.name)

    embed_7.add_field(name='条件',
                      value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n魔法石倍率：{alpha}倍')

    embed_7.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                      value=f'メテオストライク (スペシャル)：**__{dmg * 9 * (osraw + 0.10):.3f}__**\n'
                            f'マジックボール (ノーマル)**：__{dmg * 4 * (osraw + 0.10):.3f}__**, '
                            f'**(詠唱時：__{dmg * 8 * (osraw + 0.10):.3f}__**)'
                            f'\nライトニングボルト (ノーマル)：**__{dmg * 3 * (osraw + 0.10):.3f}__**\n'
                            f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                      inline=False)

    embed_7.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                      value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osraw - 0.05):.3f}__**'
                            f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osraw - 0.05):.3f}__**',
                      inline=False)

    embed_7.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                      value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{dmg * 1.1 * 7 * (osraw - 0.05):.3f}__**'
                            f'\n雪柱 (ノーマル)：**__{dmg * 4 * (osraw - 0.05):.3f}__**',
                      inline=False)

    embed_7.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                      value=f'オーバーシュート (スペシャル)：**__{dmg * 12.5 * (osraw - 0.05):.3f}__, '
                            f'パッシブあり：__{dmg * 12.5 * 1.5 * (osraw - 0.05):.3f}__**'
                            f'\nシャドウパワー (ノーマル)：**__{dmg * 1.5 * (osraw - 0.05):.3f}__**'
                            f'\nエレメンタルパワー	(パッシブ)：**__{dmg * 1.5 * (osraw - 0.05):.3f}__**',
                      inline=False)

    embed_7.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                      value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osraw - 0.05):.3f}__**',
                      inline=False)

    embed_7.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                      value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{dmg * 8 * (osraw - 0.05):.3f}**__')

    embed_7.add_field(name='**聖剣 (In 浮世の砂海)**',
                      value=f'下克上 (パッシブ)：**__ボスmob {dmg * 1.07 * (osraw - 0.05):.3f} / 通常mob {dmg * 0.7 * (osraw - 0.05):.3f}__**',
                      inline=False)

    embed_8 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(),
                            url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                            description=f"**職業：ロウニン**")

    embed_8.set_author(name=ctx.author.name)

    embed_8.add_field(name='条件',
                      value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n魔法石倍率：{alpha}倍')

    embed_8.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                      value=f'メテオストライク (スペシャル)：**__{dmg * 9 * (osraw - 0.04):.3f}__**\n'
                            f'マジックボール (ノーマル)**：__{dmg * 4 * (osraw - 0.04):.3f}__**, '
                            f'**(詠唱時：__{dmg * 8 * (osraw - 0.04):.3f}__**)'
                            f'\nライトニングボルト (ノーマル)：**__{dmg * 3 * osraw:.3f}__**\n'
                            f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                      inline=False)

    embed_8.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                      value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osraw - 0.04):.3f}__**'
                            f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osraw - 0.04):.3f}__**',
                      inline=False)

    embed_8.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                      value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{dmg * 1.1 * 7 * (osraw - 0.04):.3f}__**'
                            f'\n雪柱 (ノーマル)：**__{dmg * 4 * (osraw - 0.04):.3f}__**',
                      inline=False)

    embed_8.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                      value=f'オーバーシュート (スペシャル)：**__{dmg * 12.5 * (osraw - 0.04):.3f}__, '
                            f'パッシブあり：__{dmg * 12.5 * 1.5 * (osraw - 0.04):.3f}__**'
                            f'\nシャドウパワー (ノーマル)：**__{dmg * 1.5 * (osraw - 0.04):.3f}__**'
                            f'\nエレメンタルパワー	(パッシブ)：**__{dmg * 1.5 * (osraw - 0.04):.3f}__**',
                      inline=False)

    embed_8.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                      value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osraw - 0.04):.3f}__**',
                      inline=False)

    embed_8.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                      value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{dmg * 8 * (osraw - 0.04):.3f}**__')

    embed_8.add_field(name='**聖剣 (In 浮世の砂海)**',
                      value=f'下克上 (パッシブ)：**__ボスmob {dmg * 1.07 * (osraw - 0.04):.3f} / 通常mob {dmg * 0.7 * (osraw - 0.04):.3f}__**',
                      inline=False)

    # ドラゴンキラー
    embed_9 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(),
                            url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                            description=f"**職業：ドラゴンキラー**")

    embed_9.set_author(name=ctx.author.name)

    embed_9.add_field(name='条件',
                      value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n魔法石倍率：{alpha}倍')

    embed_9.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                      value=f'メテオストライク (スペシャル)：**__{dmg * 9 * (osraw - 0.02):.3f}__**\n'
                            f'マジックボール (ノーマル)**：__{dmg * 4 * (osraw - 0.02):.3f}__**, '
                            f'**(詠唱時：__{dmg * 8 * (osraw - 0.02):.3f}__**)'
                            f'\nライトニングボルト (ノーマル)：**__{dmg * 3 * (osraw - 0.02):.3f}__**\n'
                            f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                      inline=False)

    embed_9.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                      value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osraw - 0.02):.3f}__**'
                            f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osraw - 0.02):.3f}__**',
                      inline=False)

    embed_9.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                      value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{dmg * 1.1 * 7 * (osraw + 0.05):.3f}__**'
                            f'\n雪柱 (ノーマル)：**__{dmg * 4 * osraw:.3f}__**', inline=False)

    embed_9.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                      value=f'オーバーシュート (スペシャル)：**__{dmg * 12.5 * (osraw + 0.05):.3f}__, '
                            f'パッシブあり：__{dmg * 12.5 * 1.5 * (osraw + 0.05):.3f}__**'
                            f'\nシャドウパワー (ノーマル)：**__{dmg * 1.5 * (osraw + 0.05):.3f}__**'
                            f'\nエレメンタルパワー	(パッシブ)：**__{dmg * 1.5 * (osraw + 0.05):.3f}__**',
                      inline=False)

    embed_9.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                      value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osraw - 0.02):.3f}__**',
                      inline=False)

    embed_9.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                      value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{dmg * 8 * (osraw + 0.05):.3f}**__')

    embed_9.add_field(name='**聖剣 (In 浮世の砂海)**',
                      value=f'下克上 (パッシブ)：**__ボスmob {dmg * 1.07 * (osraw - 0.02):.3f} / 通常mob {dmg * 0.7 * (osraw - 0.02):.3f}__**',
                      inline=False)

    # プリースト
    embed_10 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(),
                             url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                             description=f"**職業：プリースト**")

    embed_10.set_author(name=ctx.author.name)

    embed_10.add_field(name='条件',
                       value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n魔法石倍率：{alpha}倍')

    embed_10.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                       value=f'メテオストライク (スペシャル)：**__{dmg * 9 * (osraw - 0.10):.3f}__**\n'
                             f'マジックボール (ノーマル)**：__{dmg * 4 * (osraw - 0.10):.3f}__**, '
                             f'**(詠唱時：__{dmg * 8 * (osraw - 0.10):.3f}__**)'
                             f'\nライトニングボルト (ノーマル)：**__{dmg * 3 * (osraw - 0.10):.3f}__**\n'
                             f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                       inline=False)

    embed_10.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                       value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osraw - 0.10):.3f}__**'
                             f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osraw - 0.10):.3f}__**',
                       inline=False)

    embed_10.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                       value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{dmg * 1.1 * 7 * (osraw - 0.10):.3f}__**'
                             f'\n雪柱 (ノーマル)：**__{dmg * 4 * (osraw - 0.10):.3f}__**',
                       inline=False)

    embed_10.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                       value=f'オーバーシュート (スペシャル)：**__{dmg * 12.5 * (osraw - 0.10):.3f}__, '
                             f'パッシブあり：__{dmg * 12.5 * 1.5 * osraw:.3f}__**'
                             f'\nシャドウパワー (ノーマル)：**__{dmg * 1.5 * (osraw - 0.10):.3f}__**'
                             f'\nエレメンタルパワー	(パッシブ)：**__{dmg * 1.5 * (osraw - 0.10):.3f}__**',
                       inline=False)

    embed_10.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                       value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osraw - 0.10):.3f}__**',
                       inline=False)

    embed_10.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                       value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{dmg * 8 * (osraw - 0.10):.3f}**__')

    embed_10.add_field(name='**聖剣 (In 浮世の砂海)**',
                       value=f'下克上 (パッシブ)：**__ボスmob {dmg * 1.07 * (osraw - 0.10):.3f} / 通常mob {dmg * 0.7 * (osraw - 0.10):.3f}__**',
                       inline=False)

    # スカ―ミッシャー
    embed_11 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(),
                             url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                             description=f"**職業：スカ―ミッシャー**")

    embed_11.set_author(name=ctx.author.name)

    embed_11.add_field(name='条件',
                       value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n魔法石倍率：{alpha}倍')

    embed_11.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                       value=f'メテオストライク (スペシャル)：**__{dmg * 9 * osraw:.3f}__**\n'
                             f'マジックボール (ノーマル)**：__{dmg * 4 * osraw:.3f}__**, '
                             f'**(詠唱時：__{dmg * 8 * osraw:.3f}__**)'
                             f'\nライトニングボルト (ノーマル)：**__{dmg * 3 * osraw:.3f}__**\n'
                             f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                       inline=False)

    embed_11.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                       value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osraw + 0.05):.3f}__**'
                             f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osraw + 0.05):.3f}__**',
                       inline=False)

    embed_11.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                       value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{dmg * 1.1 * 7 * osraw:.3f}__**'
                             f'\n雪柱 (ノーマル)：**__{dmg * 4 * osraw:.3f}__**', inline=False)

    embed_11.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                       value=f'オーバーシュート (スペシャル)：**__{dmg * 12.5 * osraw:.3f}__, '
                             f'パッシブあり：__{dmg * 12.5 * 1.5 * osraw:.3f}__**'
                             f'\nシャドウパワー (ノーマル)：**__{dmg * 1.5 * osraw:.3f}__**'
                             f'\nエレメンタルパワー	(パッシブ)：**__{dmg * 1.5 * osraw:.3f}__**',
                       inline=False)

    embed_11.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                       value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osraw + 0.05):.3f}__**',
                       inline=False)

    embed_11.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                       value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{dmg * 8 * osraw:.3f}**__')

    embed_11.add_field(name='**聖剣 (In 浮世の砂海)**',
                       value=f'下克上 (パッシブ)：**__ボスmob {dmg * 1.07 * (osraw + 0.05):.3f} / 通常mob {dmg * 0.7 * (osraw + 0.05):.3f}__**',
                       inline=False)

    # ハグレモノ
    embed_12 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(),
                             url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                             description=f"**職業：ハグレモノ**")

    embed_12.set_author(name=ctx.author.name)

    embed_12.add_field(name='条件',
                       value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n魔法石倍率：{alpha}倍')

    embed_12.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                       value=f'メテオストライク (スペシャル)：**__{dmg * 9 * (osraw - 0.07):.3f}__**\n'
                             f'マジックボール (ノーマル)**：__{dmg * 4 * (osraw - 0.07):.3f}__**, '
                             f'**(詠唱時：__{dmg * 8 * osraw:.3f}__**)'
                             f'\nライトニングボルト (ノーマル)：**__{dmg * 3 * (osraw - 0.07):.3f}__**\n'
                             f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                       inline=False)

    embed_12.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                       value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osraw - 0.07):.3f}__**'
                             f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osraw - 0.07):.3f}__**',
                       inline=False)

    embed_12.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                       value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{dmg * 1.1 * 7 * (osraw - 0.07):.3f}__**'
                             f'\n雪柱 (ノーマル)：**__{dmg * 4 * osraw - 0.07:.3f}__**',
                       inline=False)

    embed_12.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                       value=f'オーバーシュート (スペシャル)：**__{dmg * 12.5 * (osraw - 0.07):.3f}__, '
                             f'パッシブあり：__{dmg * 12.5 * 1.5 * (osraw - 0.07):.3f}__**'
                             f'\nシャドウパワー (ノーマル)：**__{dmg * 1.5 * (osraw - 0.07):.3f}__**'
                             f'\nエレメンタルパワー	(パッシブ)：**__{dmg * 1.5 * (osraw - 0.07):.3f}__**',
                       inline=False)

    embed_12.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                       value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osraw - 0.07):.3f}__**',
                       inline=False)

    embed_12.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                       value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{dmg * 8 * (osraw - 0.07):.3f}**__')

    embed_12.add_field(name='**聖剣 (In 浮世の砂海)**',
                       value=f'下克上 (パッシブ)：**__ボスmob {dmg * 1.07 * (osraw - 0.07):.3f} / 通常mob {dmg * 0.7 * (osraw - 0.07):.3f}__**',
                       inline=False)

    # ルーンキャスター
    embed_13 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(),
                             url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                             description=f"**職業：ルーンキャスター**")

    embed_13.set_author(name=ctx.author.name)

    embed_13.add_field(name='条件',
                       value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n魔法石倍率：{alpha}倍')

    embed_13.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                       value=f'メテオストライク (スペシャル)：**__{dmg * 9 * (osraw + 0.07):.3f}__**\n'
                             f'マジックボール (ノーマル)**：__{dmg * 4 * (osraw + 0.07):.3f}__**, '
                             f'**(詠唱時：__{dmg * 8 * (osraw + 0.07):.3f}__**)'
                             f'\nライトニングボルト (ノーマル)：**__{dmg * 3 * (osraw + 0.07):.3f}__**\n'
                             f'ファイヤ・ボルケーノ (ノーマル)**：__{dmg * 22 * (osraw + 0.07):.3f}__**',
                       inline=False)

    embed_13.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                       value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osraw - 0.07):.3f}__**'
                             f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osraw - 0.07):.3f}__**',
                       inline=False)

    embed_13.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                       value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{dmg * 7 * 1.1 * (osraw - 0.07):.3f}__**'
                             f'\n雪柱 (ノーマル)：**__{dmg * 4 * (osraw - 0.07):.3f}__**',
                       inline=False)

    embed_13.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                       value=f'オーバーシュート (スペシャル)：**__{dmg * 12.5 * (osraw - 0.07):.3f}__, '
                             f'パッシブあり：__{dmg * 12.5 * 1.5 * osraw:.3f}__**'
                             f'\nシャドウパワー (ノーマル)：**__{dmg * 1.5 * (osraw - 0.07):.3f}__**'
                             f'\nエレメンタルパワー	(パッシブ)：**__{dmg * 1.5 * (osraw - 0.07):.3f}__**',
                       inline=False)

    embed_13.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                       value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osraw - 0.07):.3f}__**',
                       inline=False)

    embed_13.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                       value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{dmg * 8 * (osraw - 0.07):.3f}**__')

    embed_13.add_field(name='**聖剣 (In 浮世の砂海)**',
                       value=f'下克上 (パッシブ)：**__ボスmob {dmg * 1.07 * (osraw - 0.07):.3f} / 通常mob {dmg * 0.7 * (osraw - 0.07):.3f}__**',
                       inline=False)

    # スペランカー
    embed_14 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(),
                             url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                             description=f"**職業：スペランカー**")

    embed_14.set_author(name=ctx.author.name)

    embed_14.add_field(name='条件',
                       value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n魔法石倍率：{alpha}倍')

    embed_14.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                       value=f'メテオストライク (スペシャル)：**__{dmg * 9 * (osraw + 0.10) :.3f}__**\n'
                             f'マジックボール (ノーマル)**：__{dmg * 4 * (osraw + 0.10):.3f}__**, '
                             f'**(詠唱時：__{dmg * 8 * (osraw + 0.10):.3f}__**)'
                             f'\nライトニングボルト (ノーマル)：**__{dmg * 3 * (osraw + 0.10):.3f}__**\n'
                             f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                       inline=False)

    embed_14.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                       value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osraw + 0.10):.3f}__**'
                             f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osraw + 0.10):.3f}__**',
                       inline=False)

    embed_14.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                       value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{dmg * 1.1 * 7 * (osraw + 0.10):.3f}__**'
                             f'\n雪柱 (ノーマル)：**__{dmg * 4 * (osraw + 0.10):.3f}__**',
                       inline=False)

    embed_14.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                       value=f'オーバーシュート (スペシャル)：**__{dmg * 12.5 * (osraw + 0.10):.3f}__, '
                             f'パッシブあり：__{dmg * 12.5 * 1.5 * (osraw + 0.10):.3f}__**'
                             f'\nシャドウパワー (ノーマル)：**__{dmg * 1.5 * (osraw + 0.10):.3f}__**'
                             f'\nエレメンタルパワー	(パッシブ)：**__{dmg * 1.5 * (osraw + 0.10):.3f}__**',
                       inline=False)

    embed_14.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                       value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osraw + 0.10):.3f}__**',
                       inline=False)

    embed_14.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                       value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{dmg * 8 * (osraw + 0.10):.3f}**__')

    embed_14.add_field(name='**聖剣 (In 浮世の砂海)**',
                       value=f'下克上 (パッシブ)：**__ボスmob {dmg * 1.07 * (osraw + 0.10):.3f} / 通常mob {dmg * 0.7 * (osraw + 0.10):.3f}__**',
                       inline=False)

    # アーサー
    embed_15 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(),
                             url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                             description=f"**職業：アーサー**")

    embed_15.set_author(name=ctx.author.name)

    embed_15.add_field(name='条件',
                       value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n魔法石倍率：{alpha}倍')

    embed_15.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                       value=f'メテオストライク (スペシャル)：**__{dmg * 9 * osraw :.3f}__**\n'
                             f'マジックボール (ノーマル)**：__{dmg * 4 * osraw :.3f}__**, '
                             f'**(詠唱時：__{dmg * 8 * osraw :.3f}__**)'
                             f'\nライトニングボルト (ノーマル)：**__{dmg * 3 * osraw :.3f}__**\n'
                             f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                       inline=False)

    embed_15.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                       value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osraw + 0.05):.3f}__**'
                             f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osraw + 0.05):.3f}__**',
                       inline=False)

    embed_15.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                       value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{dmg * 1.1 * 7 * osraw :.3f}__**'
                             f'\n雪柱 (ノーマル)：**__{dmg * 4 * osraw :.3f}__**',
                       inline=False)

    embed_15.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                       value=f'オーバーシュート (スペシャル)：**__{dmg * 12.5 * osraw :.3f}__, '
                             f'パッシブあり：__{dmg * 12.5 * 1.5 * osraw :.3f}__**'
                             f'\nシャドウパワー (ノーマル)：**__{dmg * 1.5 * osraw :.3f}__**'
                             f'\nエレメンタルパワー	(パッシブ)：**__{dmg * 1.5 * osraw :.3f}__**',
                       inline=False)

    embed_15.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                       value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osraw + 0.05):.3f}__**',
                       inline=False)

    embed_15.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                       value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{dmg * 8 * osraw :.3f}**__')

    embed_15.add_field(name='**聖剣 (In 浮世の砂海)**',
                       value=f'下克上 (パッシブ)：**__ボスmob {dmg * 1.07 * (osraw + 0.05):.3f} / 通常mob {dmg * 0.7 * (osraw + 0.05):.3f}__**',
                       inline=False)

    # シーカー
    embed_16 = discord.Embed(title=f"skill一覧", color=discord.Color.dark_green(),
                             url="https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB",
                             description=f"**職業：シーカー**")

    embed_16.set_author(name=ctx.author.name)

    embed_16.add_field(name='条件',
                       value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n魔法石倍率：{alpha}倍')

    embed_16.add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                       value=f'メテオストライク (スペシャル)：**__{dmg * 9 * (osraw - 0.07):.3f}__**\n'
                             f'マジックボール (ノーマル)**：__{dmg * 4 * (osraw - 0.07):.3f}__**, '
                             f'**(詠唱時：__{dmg * 8 * (osraw - 0.07):.3f}__**)'
                             f'\nライトニングボルト (ノーマル)：**__{dmg * 3 * (osraw - 0.07):.3f}__**\n'
                             f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                       inline=False)

    embed_16.add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                       value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osraw - 0.07):.3f}__**'
                             f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osraw - 0.07):.3f}__**',
                       inline=False)

    embed_16.add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                       value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{dmg * 1.1 * 7 * (osraw + 0.07):.3f}__**'
                             f'\n雪柱 (ノーマル)：**__{dmg * 4 * (osraw + 0.07):.3f}__**',
                       inline=False)

    embed_16.add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                       value=f'オーバーシュート (スペシャル)：**__{dmg * 12.5 * (osraw + 0.07):.3f}__, '
                             f'パッシブあり：__{dmg * 12.5 * 1.5 * osraw:.3f}__**'
                             f'\nシャドウパワー (ノーマル)：**__{dmg * 1.5 * (osraw + 0.07):.3f}__**'
                             f'\nエレメンタルパワー	(パッシブ)：**__{dmg * 1.5 * (osraw + 0.07):.3f}__**',
                       inline=False)

    embed_16.add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                       value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osraw - 0.07):.3f}__**',
                       inline=False)

    embed_16.add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                       value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{dmg * 8 * (osraw - 0.07):.3f}**__')

    embed_16.add_field(name='**聖剣 (In 浮世の砂海)**',
                       value=f'下克上 (パッシブ)：**__ボスmob {dmg * 1.07 * (osraw - 0.07):.3f} / 通常mob {dmg * 0.7 * (osraw - 0.07):.3f}__**',
                       inline=False)
    embed_lists = [
        embed_1, embed_2, embed_3, embed_4, embed_5, embed_6, embed_7, embed_8,
        embed_9, embed_10, embed_11, embed_12, embed_13, embed_14, embed_15, embed_16
    ]
    return embed_lists


def embed_skill(
        ctx: commands.Context,
        raw: float,  # 素ダメ
        dmg: float,  # 追加ダメ+魔法石込みのダメージ
        sp_dmg: float,  # 魔法石込みのダメージ
        os: int,  # OS値
        osval: float,  # OS倍率
        stone_list: list,  # 魔法石リスト
        stone_val: float  # 魔法石倍率
) -> list[discord.Embed]:
    print(stone_list)
    """This function takes in the user's input and returns a list of the
        embeds that will be sent to the user.

    Parameters
    ----------
    ctx : commands.Context
        The context of the command.
    raw : float
        The raw value of the weapon
    dmg : float
        The base damage of the skill.
    sp_dmg : float
        The amount of special damage the skill does.
    os : int
        the number of OverStrength
    osval : float
        the value of the OS
    stone_list : list
        list of stones to be used
    stone_val : float
        the value of the stones

    Returns
    -------
    embed_list : list
        list of skilldata embeds
    """
    # 1 : ノービス, ソルジャー, アーチャー, マジシャン, ウォーリア, ボウマン, メイジ
    # 2 : ロウニン, ドラゴンキラー, プリースト, スカーミッシャー, ハグレモノ, ルーンキャスター, スペランカー, アーサー, シーカー
    # 3 : スカルピアサー, バタフライシーカー, アレイスター, ダークブラスター 1, ダークブラスター 2
    if stone_list != ['な', 'し']:
        stone_list = ', '.join(sorted(stone_list))
    if stone_list == ['な', 'し']:
        stone_list = 'なし'
    e_01 = discord.Embed(title='skill 一覧', url=url, description='**職業：ノービス**', colour=discord.Colour.gold())
    e_02 = discord.Embed(title='skill 一覧', url=url, description='**職業：ソルジャー**', colour=discord.Colour.gold())
    e_03 = discord.Embed(title='skill 一覧', url=url, description='**職業：アーチャー**', colour=discord.Colour.gold())
    e_04 = discord.Embed(title='skill 一覧', url=url, description='**職業：マジシャン**', colour=discord.Colour.gold())

    e_05 = discord.Embed(title='skill 一覧', url=url, description='**職業：ウォーリア**', colour=discord.Colour.gold())
    e_06 = discord.Embed(title='skill 一覧', url=url, description='**職業：ボウマン**', colour=discord.Colour.gold())
    e_07 = discord.Embed(title='skill 一覧', url=url, description='**職業：メイジ**', colour=discord.Colour.gold())

    e_08 = discord.Embed(title='skill 一覧', url=url, description='**職業：ロウニン**', colour=discord.Colour.gold())
    e_09 = discord.Embed(title='skill 一覧', url=url, description='**職業：ドラゴンキラー**', colour=discord.Colour.gold())
    e_10 = discord.Embed(title='skill 一覧', url=url, description='**職業：プリースト**', colour=discord.Colour.gold())
    e_11 = discord.Embed(title='skill 一覧', url=url, description='**職業：スカーミッシャー**', colour=discord.Colour.gold())

    e_12 = discord.Embed(title='skill 一覧', url=url, description='**職業：ハグレモノ**', colour=discord.Colour.gold())
    e_13 = discord.Embed(title='skill 一覧', url=url, description='**職業：ルーンキャスター**', colour=discord.Colour.gold())
    e_14 = discord.Embed(title='skill 一覧', url=url, description='**職業：スペランカー**', colour=discord.Colour.gold())
    e_15 = discord.Embed(title='skill 一覧', url=url, description='**職業：アーサー**', colour=discord.Colour.gold())
    e_16 = discord.Embed(title='skill 一覧', url=url, description='**職業：シーカー**', colour=discord.Colour.gold())

    e_17 = discord.Embed(title='skill 一覧', url=url, description='**職業：スカルピアサー**', colour=discord.Colour.gold())
    e_18 = discord.Embed(title='skill 一覧', url=url, description='**職業：バタフライシーカー**', colour=discord.Colour.gold())
    e_19 = discord.Embed(title='skill 一覧', url=url, description='**職業：アレイスター**', colour=discord.Colour.gold())
    e_20 = discord.Embed(title='skill 一覧', url=url, description='**職業：ダークブラスター 1**', colour=discord.Colour.gold())
    e_21 = discord.Embed(title='skill 一覧', url=url, description='**職業：ダークブラスター 2**', colour=discord.Colour.gold())

    # ノービス
    e_01.add_field(name='条件',
                   value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osval}\n魔法石： {stone_list}\n魔法石倍率：{stone_val}倍') \
        .set_author(name=ctx.author.name) \
        .add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                   value=f'メテオストライク (スペシャル)：**__{sp_dmg * 9 * osval:.3f}__**\n'
                         f'マジックボール (ノーマル)**：__{sp_dmg * 4 * osval:.3f}__**, '
                         f'**(詠唱時：__{sp_dmg * 8 * osval:.3f})__**\n'
                         f'ライトニングボルト (ノーマル)：**__{sp_dmg * 3 * osval:.3f}__**\n'
                         f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                   inline=False) \
        .add_field(name='**†Twilight HeavenRay† (In 輝煌の残滓)**',
                   value=f'神の鉄槌 (スペシャル): __**{sp_dmg * 3 * osval:.3f}**__\n'
                         f'光ある場所に (パッシブ): __**{sp_dmg * 1.2 * osval:.3f}**__', inline=False) \
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * osval:.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * osval:.3f}__**', inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * osval:.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * osval:.3f}__**', inline=False) \
        .add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                   value=f'オーバーシュート (スペシャル)：**__{sp_dmg * 12.5 * osval:.3f}__, '
                         f'パッシブあり：__{sp_dmg * 12.5 * 1.5 * osval:.3f}__**'
                         f'\nシャドウパワー (ノーマル)：**__{sp_dmg * 1.7 * 1.5 * osval:.3f}__**'
                         f'\nエレメンタルパワー	(パッシブ)：**__{sp_dmg * 1.7 * 1.5 * osval:.3f}__**',
                   inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * osval:.3f}__**', inline=False) \
        .add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                   value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{sp_dmg * 8 * osval:.3f}**__') \
        .add_field(name='**シャルル (魔界：ヘルスラ)**',
                   value=f'サテライトキャノン (スペシャル): __**1発 {sp_dmg * 2.5 * osval:.3f} 10発 {sp_dmg * 2.5 * 10 * osval:.3f}**__\n'
                         f'ダークサイクロン (ノーマル): __**1発 {sp_dmg * 1.7 * 0.8:.3f} 5発 {sp_dmg * 1.7 * 0.8 * 5 * osval:.3f}**__\n'
                         f'インフェライズ (ノーマル): __**{sp_dmg * 2.0 * osval:.3f}**__', inline=False) \
        .add_field(name='**聖剣 (In 浮世の砂海)**',
                   value=f'天下無双 (スペシャル): __**{dmg * 1.07 * osval * 0.75:.3f} / {dmg * 0.70 * osval * 0.75:.3f}**__\n'
                         f'下克上 (パッシブ)：**__ボスmob {dmg * 1.07 * osval:.3f} / 通常mob {dmg * 0.7 * osval:.3f}__**',
                   inline=False)

    # ソルジャー
    e_02.add_field(name='条件',
                   value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osval}\n魔法石： {stone_list}\n魔法石倍率：{stone_val}倍') \
        .set_author(name=ctx.author.name) \
        .add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                   value=f'メテオストライク (スペシャル)：**__{sp_dmg * 9 * (osval - 0.02):.3f}__**\n'
                         f'マジックボール (ノーマル)**：__{sp_dmg * 4 * (osval - 0.02):.3f}__**, '
                         f'**(詠唱時：__{sp_dmg * 8 * (osval - 0.02):.3f})__**\n'
                         f'ライトニングボルト (ノーマル)：**__{sp_dmg * 3 * (osval - 0.02):.3f}__**\n'
                         f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                   inline=False) \
        .add_field(name='**†Twilight HeavenRay† (In 輝煌の残滓)**',
                   value=f'神の鉄槌 (スペシャル): __**{sp_dmg * 3 * (osval - 0.02):.3f}**__\n'
                         f'光ある場所に (パッシブ): __**{sp_dmg * 1.2 * (osval - 0.02):.3f}**__', inline=False) \
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osval + 0.05):.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osval + 0.05):.3f}__**', inline=False) \
        .add_field(name=f'***-神弓- ブリザードテンスト*** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * (osval - 0.02):.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * (osval - 0.02):.3f}__**', inline=False) \
        .add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                   value=f'オーバーシュート (スペシャル)：**__{sp_dmg * 12.5 * (osval - 0.02):.3f}__, '
                         f'パッシブあり：__{sp_dmg * 12.5 * 1.5 * (osval - 0.02):.3f}__**'
                         f'\nシャドウパワー (ノーマル)：**__{sp_dmg * 1.7 * 1.5 * (osval - 0.02):.3f}__**'
                         f'\nエレメンタルパワー	(パッシブ)：**__{sp_dmg * 1.7 * 1.5 * (osval - 0.02):.3f}__**',
                   inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osval + 0.05):.3f}__**', inline=False) \
        .add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                   value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{sp_dmg * 8 * (osval - 0.02):.3f}**__') \
        .add_field(name='**シャルル (魔界：ヘルスラ)**',
                   value=f'サテライトキャノン (スペシャル): __**1発 {sp_dmg * 2.5 * osval:.3f} 10発 {sp_dmg * 2.5 * 10 * (osval - 0.02):.3f}**__\n'
                         f'ダークサイクロン (ノーマル): __**1発 {sp_dmg * 1.7 * 0.8 * (osval - 0.02):.3f} '
                         f'5発 {sp_dmg * 1.7 * 0.8 * 5 * (osval - 0.02):.3f}**__\n'
                         f'インフェライズ (ノーマル): __**{sp_dmg * 2.0 * (osval - 0.02):.3f}**__', inline=False) \
        .add_field(name='**聖剣 (In 浮世の砂海)**',
                   value=f'天下無双 (スペシャル): __**{dmg * 1.07 * (osval + 0.05) * 0.75:.3f} / {dmg * 0.70 * (osval + 0.05) * 0.75:.3f}**__\n'
                         f'下克上 (パッシブ)：**__ボスmob {dmg * 1.07 * (osval + 0.05):.3f} / 通常mob {dmg * 0.7 * (osval + 0.05):.3f}__**',
                   inline=False)
    # アーチャー
    e_03.add_field(name='条件',
                   value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osval}\n魔法石： {stone_list}\n魔法石倍率：{stone_val}倍') \
        .set_author(name=ctx.author.name) \
        .add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                   value=f'メテオストライク (スペシャル)：**__{sp_dmg * 9 * (osval - 0.02):.3f}__**\n'
                         f'マジックボール (ノーマル)**：__{sp_dmg * 4 * (osval - 0.02):.3f}__**, '
                         f'**(詠唱時：__{sp_dmg * 8 * (osval - 0.02):.3f})__**\n'
                         f'ライトニングボルト (ノーマル)：**__{sp_dmg * 3 * (osval - 0.02):.3f}__**\n'
                         f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                   inline=False) \
        .add_field(name='**†Twilight HeavenRay† (In 輝煌の残滓)**',
                   value=f'神の鉄槌 (スペシャル): __**{sp_dmg * 3 * (osval - 0.02):.3f}**__\n'
                         f'光ある場所に (パッシブ): __**{sp_dmg * 1.2 * (osval - 0.02):.3f}**__', inline=False) \
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osval - 0.02):.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osval - 0.02):.3f}__**', inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * (osval + 0.05):.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * (osval + 0.05):.3f}__**', inline=False) \
        .add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                   value=f'オーバーシュート (スペシャル)：**__{sp_dmg * 12.5 * (osval + 0.05):.3f}__, '
                         f'パッシブあり：__{sp_dmg * 12.5 * 1.5 * (osval + 0.05):.3f}__**'
                         f'\nシャドウパワー (ノーマル)：**__{sp_dmg * 1.7 * 1.5 * (osval + 0.05):.3f}__**'
                         f'\nエレメンタルパワー	(パッシブ)：**__{sp_dmg * 1.7 * 1.5 * (osval + 0.05):.3f}__**',
                   inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osval - 0.02):.3f}__**', inline=False) \
        .add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                   value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{sp_dmg * 8 * (osval + 0.05):.3f}**__') \
        .add_field(name='**シャルル (魔界：ヘルスラ)**',
                   value=f'サテライトキャノン (スペシャル): __**1発 {sp_dmg * 2.5 * (osval + 0.05):.3f} 10発 {sp_dmg * 2.5 * 10 * (osval + 0.05):.3f}**__\n'
                         f'ダークサイクロン (ノーマル): __**1発 {sp_dmg * 1.7 * 0.8 * (osval + 0.05):.3f} 5発 {sp_dmg * 1.7 * 0.8 * 5 * (osval + 0.05):.3f}**__\n'
                         f'インフェライズ (ノーマル): __**{sp_dmg * 2.0 * (osval + 0.05):.3f}**__', inline=False) \
        .add_field(name='**聖剣 (In 浮世の砂海)**',
                   value=f'天下無双 (スペシャル): __**{dmg * 1.07 * (osval - 0.02) * 0.75:.3f} / {dmg * 0.70 * (osval - 0.02) * 0.75:.3f}**__\n'
                         f'下克上 (パッシブ)：**__ボスmob {dmg * 1.07 * (osval - 0.02):.3f} / 通常mob {dmg * 0.7 * (osval - 0.02):.3f}__**',
                   inline=False)

    # マジシャン
    e_04.add_field(name='条件',
                   value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osval}\n魔法石： {stone_list}\n魔法石倍率：{stone_val}倍') \
        .set_author(name=ctx.author.name) \
        .add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                   value=f'メテオストライク (スペシャル)：**__{sp_dmg * 9 * (osval + 0.05):.3f}__**\n'
                         f'マジックボール (ノーマル)**：__{sp_dmg * 4 * (osval + 0.05):.3f}__**, '
                         f'**(詠唱時：__{sp_dmg * 8 * (osval + 0.05):.3f})__**\n'
                         f'ライトニングボルト (ノーマル)：**__{sp_dmg * 3 * (osval + 0.05):.3f}__**\n'
                         f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                   inline=False) \
        .add_field(name='**†Twilight HeavenRay† (In 輝煌の残滓)**',
                   value=f'神の鉄槌 (スペシャル): __**{sp_dmg * 3 * (osval + 0.05):.3f}**__\n'
                         f'光ある場所に (パッシブ): __**{sp_dmg * 1.2 * (osval + 0.05):.3f}**__', inline=False) \
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osval - 0.02):.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osval - 0.02):.3f}__**', inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * (osval - 0.02):.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * (osval - 0.02):.3f}__**', inline=False) \
        .add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                   value=f'オーバーシュート (スペシャル)：**__{sp_dmg * 12.5 * (osval - 0.02):.3f}__, '
                         f'パッシブあり：__{sp_dmg * 12.5 * 1.5 * (osval - 0.02):.3f}__**'
                         f'\nシャドウパワー (ノーマル)：**__{sp_dmg * 1.7 * 1.5 * (osval - 0.02):.3f}__**'
                         f'\nエレメンタルパワー	(パッシブ)：**__{sp_dmg * 1.7 * 1.5 * (osval - 0.02):.3f}__**',
                   inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osval - 0.02):.3f}__**', inline=False) \
        .add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                   value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{sp_dmg * 8 * (osval - 0.02):.3f}**__') \
        .add_field(name='**シャルル (魔界：ヘルスラ)**',
                   value=f'サテライトキャノン (スペシャル): __**1発 {sp_dmg * 2.5 * (osval - 0.02):.3f} 10発 {sp_dmg * 2.5 * 10 * (osval - 0.02):.3f}**__\n'
                         f'ダークサイクロン (ノーマル): __**1発 {sp_dmg * 1.7 * 0.8 * (osval - 0.02):.3f} 5発 {sp_dmg * 1.7 * 0.8 * 5 * (osval - 0.02):.3f}**__\n'
                         f'インフェライズ (ノーマル): __**{sp_dmg * 2.0 * (osval - 0.02):.3f}**__', inline=False) \
        .add_field(name='**聖剣 (In 浮世の砂海)**',
                   value=f'天下無双 (スペシャル): __**{dmg * 1.07 * (osval - 0.02) * 0.75:.3f} / {dmg * 0.70 * (osval - 0.02) * 0.75:.3f}**__\n'
                         f'下克上 (パッシブ)：**__ボスmob {dmg * 1.07 * (osval - 0.02):.3f} / 通常mob {dmg * 0.7 * (osval - 0.02):.3f}__**',
                   inline=False)
    # ウォーリア
    e_05.add_field(name='条件',
                   value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osval}\n魔法石： {stone_list}\n魔法石倍率：{stone_val}倍') \
        .set_author(name=ctx.author.name) \
        .add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                   value=f'メテオストライク (スペシャル)：**__{sp_dmg * 9 * (osval - 0.05):.3f}__**\n'
                         f'マジックボール (ノーマル)**：__{sp_dmg * 4 * (osval - 0.05):.3f}__**, '
                         f'**(詠唱時：__{sp_dmg * 8 * (osval - 0.05):.3f})__**\n'
                         f'ライトニングボルト (ノーマル)：**__{sp_dmg * 3 * (osval - 0.05):.3f}__**\n'
                         f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                   inline=False) \
        .add_field(name='**†Twilight HeavenRay† (In 輝煌の残滓)**',
                   value=f'神の鉄槌 (スペシャル): __**{sp_dmg * 3 * (osval - 0.05):.3f}**__\n'
                         f'光ある場所に (パッシブ): __**{sp_dmg * 1.2 * (osval - 0.05):.3f}**__', inline=False) \
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osval + 0.10):.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osval + 0.10):.3f}__**', inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * (osval - 0.05):.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * (osval - 0.05):.3f}__**', inline=False) \
        .add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                   value=f'オーバーシュート (スペシャル)：**__{sp_dmg * 12.5 * (osval - 0.05):.3f}__, '
                         f'パッシブあり：__{sp_dmg * 12.5 * 1.5 * (osval - 0.05):.3f}__**'
                         f'\nシャドウパワー (ノーマル)：**__{sp_dmg * 1.7 * 1.5 * (osval - 0.05):.3f}__**'
                         f'\nエレメンタルパワー	(パッシブ)：**__{sp_dmg * 1.7 * 1.5 * (osval - 0.05):.3f}__**',
                   inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osval + 0.10):.3f}__**', inline=False) \
        .add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                   value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{sp_dmg * 8 * (osval + 0.10):.3f}**__') \
        .add_field(name='**シャルル (魔界：ヘルスラ)**',
                   value=f'サテライトキャノン (スペシャル): __**1発 {sp_dmg * 2.5 * (osval - 0.05):.3f} 10発 {sp_dmg * 2.5 * 10 * (osval - 0.05):.3f}**__\n'
                         f'ダークサイクロン (ノーマル): __**1発 {sp_dmg * 1.7 * 0.8 * (osval - 0.05):.3f} 5発 {sp_dmg * 1.7 * 0.8 * 5 * (osval - 0.05):.3f}**__\n'
                         f'インフェライズ (ノーマル): __**{sp_dmg * 2.0 * (osval - 0.05):.3f}**__', inline=False) \
        .add_field(name='**聖剣 (In 浮世の砂海)**',
                   value=f'天下無双 (スペシャル): __**{dmg * 1.07 * (osval + 0.10) * 0.75:.3f} / {dmg * 0.70 * (osval + 0.10) * 0.75:.3f}**__\n'
                         f'下克上 (パッシブ)：**__ボスmob {dmg * 1.07 * (osval + 0.10):.3f} / 通常mob {dmg * 0.7 * (osval + 0.10):.3f}__**',
                   inline=False)
    # ボウマン
    e_06.add_field(name='条件',
                   value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osval}\n魔法石： {stone_list}\n魔法石倍率：{stone_val}倍') \
        .set_author(name=ctx.author.name) \
        .add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                   value=f'メテオストライク (スペシャル)：**__{sp_dmg * 9 * (osval - 0.05):.3f}__**\n'
                         f'マジックボール (ノーマル)**：__{sp_dmg * 4 * (osval - 0.05):.3f}__**, '
                         f'**(詠唱時：__{sp_dmg * 8 * (osval - 0.05):.3f})__**\n'
                         f'ライトニングボルト (ノーマル)：**__{sp_dmg * 3 * (osval - 0.05):.3f}__**\n'
                         f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                   inline=False) \
        .add_field(name='**†Twilight HeavenRay† (In 輝煌の残滓)**',
                   value=f'神の鉄槌 (スペシャル): __**{sp_dmg * 3 * (osval - 0.05):.3f}**__\n'
                         f'光ある場所に (パッシブ): __**{sp_dmg * 1.2 * (osval - 0.05):.3f}**__', inline=False) \
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osval - 0.05):.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osval - 0.05):.3f}__**', inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * (osval + 0.10):.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * (osval + 0.10):.3f}__**', inline=False) \
        .add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                   value=f'オーバーシュート (スペシャル)：**__{sp_dmg * 12.5 * (osval + 0.10):.3f}__, '
                         f'パッシブあり：__{sp_dmg * 12.5 * 1.5 * (osval + 0.10):.3f}__**'
                         f'\nシャドウパワー (ノーマル)：**__{sp_dmg * 1.7 * 1.5 * (osval + 0.10):.3f}__**'
                         f'\nエレメンタルパワー	(パッシブ)：**__{sp_dmg * 1.7 * 1.5 * (osval + 0.10):.3f}__**',
                   inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osval - 0.05):.3f}__**', inline=False) \
        .add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                   value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{sp_dmg * 8 * (osval - 0.05):.3f}**__') \
        .add_field(name='**シャルル (魔界：ヘルスラ)**',
                   value=f'サテライトキャノン (スペシャル): __**1発 {sp_dmg * 2.5 * (osval + 0.10):.3f} 10発 {sp_dmg * 2.5 * 10 * (osval + 0.10):.3f}**__\n'
                         f'ダークサイクロン (ノーマル): __**1発 {sp_dmg * 1.7 * 0.8 * (osval + 0.10):.3f} 5発 {sp_dmg * 1.7 * 0.8 * 5 * (osval + 0.10):.3f}**__\n'
                         f'インフェライズ (ノーマル): __**{sp_dmg * 2.0 * (osval + 0.10):.3f}**__', inline=False) \
        .add_field(name='**聖剣 (In 浮世の砂海)**',
                   value=f'天下無双 (スペシャル): __**{dmg * 1.07 * (osval - 0.05) * 0.75:.3f} / {dmg * 0.70 * (osval - 0.05) * 0.75:.3f}**__\n'
                         f'下克上 (パッシブ)：**__ボスmob {dmg * 1.07 * (osval - 0.05):.3f} / 通常mob {dmg * 0.7 * (osval - 0.05):.3f}__**',
                   inline=False)

    # メイジ
    e_07.add_field(name='条件',
                   value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osval}\n魔法石： {stone_list}\n魔法石倍率：{stone_val}倍') \
        .set_author(name=ctx.author.name) \
        .add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                   value=f'メテオストライク (スペシャル)：**__{sp_dmg * 9 * (osval + 0.10):.3f}__**\n'
                         f'マジックボール (ノーマル)**：__{sp_dmg * 4 * (osval + 0.10):.3f}__**, '
                         f'**(詠唱時：__{sp_dmg * 8 * (osval + 0.10):.3f})__**\n'
                         f'ライトニングボルト (ノーマル)：**__{sp_dmg * 3 * (osval + 0.10):.3f}__**\n'
                         f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                   inline=False) \
        .add_field(name='**†Twilight HeavenRay† (In 輝煌の残滓)**',
                   value=f'神の鉄槌 (スペシャル): __**{sp_dmg * 3 * (osval + 0.10):.3f}**__\n'
                         f'光ある場所に (パッシブ): __**{sp_dmg * 1.2 * (osval + 0.10):.3f}**__', inline=False) \
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osval - 0.05):.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osval - 0.05):.3f}__**', inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * (osval - 0.05):.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * (osval - 0.05):.3f}__**', inline=False) \
        .add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                   value=f'オーバーシュート (スペシャル)：**__{sp_dmg * 12.5 * (osval - 0.05):.3f}__, '
                         f'パッシブあり：__{sp_dmg * 12.5 * 1.5 * (osval - 0.05):.3f}__**'
                         f'\nシャドウパワー (ノーマル)：**__{sp_dmg * 1.7 * 1.5 * (osval - 0.05):.3f}__**'
                         f'\nエレメンタルパワー	(パッシブ)：**__{sp_dmg * 1.7 * 1.5 * (osval - 0.05):.3f}__**',
                   inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osval - 0.05):.3f}__**', inline=False) \
        .add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                   value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{sp_dmg * 8 * (osval - 0.05):.3f}**__') \
        .add_field(name='**シャルル (魔界：ヘルスラ)**',
                   value=f'サテライトキャノン (スペシャル): __**1発 {sp_dmg * 2.5 * (osval - 0.05):.3f} 10発 {sp_dmg * 2.5 * 10 * (osval - 0.05):.3f}**__\n'
                         f'ダークサイクロン (ノーマル): __**1発 {sp_dmg * 1.7 * 0.8 * (osval - 0.05):.3f} 5発 {sp_dmg * 1.7 * 0.8 * 5 * (osval - 0.05):.3f}**__\n'
                         f'インフェライズ (ノーマル): __**{sp_dmg * 2.0 * (osval - 0.05):.3f}**__', inline=False) \
        .add_field(name='**聖剣 (In 浮世の砂海)**',
                   value=f'天下無双 (スペシャル): __**{dmg * 1.07 * (osval - 0.05) * 0.75:.3f} / {dmg * 0.70 * (osval - 0.05) * 0.75:.3f}**__\n'
                         f'下克上 (パッシブ)：**__ボスmob {dmg * 1.07 * (osval - 0.05):.3f} / 通常mob {dmg * 0.7 * (osval - 0.05):.3f}__**',
                   inline=False)

    # ロウニン
    e_08.add_field(name='条件',
                   value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osval}\n魔法石： {stone_list}\n魔法石倍率：{stone_val}倍') \
        .set_author(name=ctx.author.name) \
        .add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                   value=f'メテオストライク (スペシャル)：**__{sp_dmg * 9 * (osval - 0.04):.3f}__**\n'
                         f'マジックボール (ノーマル)**：__{sp_dmg * 4 * (osval - 0.04):.3f}__**, '
                         f'**(詠唱時：__{sp_dmg * 8 * (osval - 0.04):.3f})__**\n'
                         f'ライトニングボルト (ノーマル)：**__{sp_dmg * 3 * (osval - 0.04):.3f}__**\n'
                         f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                   inline=False) \
        .add_field(name='**†Twilight HeavenRay† (In 輝煌の残滓)**',
                   value=f'神の鉄槌 (スペシャル): __**{sp_dmg * 3 * (osval - 0.04):.3f}**__\n'
                         f'光ある場所に (パッシブ): __**{sp_dmg * 1.2 * (osval - 0.04):.3f}**__', inline=False) \
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osval - 0.04):.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osval - 0.04):.3f}__**', inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * (osval - 0.04):.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * (osval - 0.04):.3f}__**', inline=False) \
        .add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                   value=f'オーバーシュート (スペシャル)：**__{sp_dmg * 12.5 * (osval - 0.04):.3f}__, '
                         f'パッシブあり：__{sp_dmg * 12.5 * 1.5 * (osval - 0.04):.3f}__**'
                         f'\nシャドウパワー (ノーマル)：**__{sp_dmg * 1.7 * 1.5 * (osval - 0.04):.3f}__**'
                         f'\nエレメンタルパワー	(パッシブ)：**__{sp_dmg * 1.7 * 1.5 * (osval - 0.04):.3f}__**',
                   inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osval - 0.04):.3f}__**', inline=False) \
        .add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                   value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{sp_dmg * 8 * (osval - 0.04):.3f}**__') \
        .add_field(name='**シャルル (魔界：ヘルスラ)**',
                   value=f'サテライトキャノン (スペシャル): __**1発 {sp_dmg * 2.5 * (osval - 0.04):.3f} 10発 {sp_dmg * 2.5 * 10 * (osval - 0.04):.3f}**__\n'
                         f'ダークサイクロン (ノーマル): __**1発 {sp_dmg * 1.7 * 0.8 * (osval - 0.04):.3f} 5発 {sp_dmg * 1.7 * 0.8 * 5 * (osval - 0.04):.3f}**__\n'
                         f'インフェライズ (ノーマル): __**{sp_dmg * 2.0 * (osval - 0.04):.3f}**__', inline=False) \
        .add_field(name='**聖剣 (In 浮世の砂海)**',
                   value=f'天下無双 (スペシャル): __**{dmg * 1.07 * (osval - 0.04) * 0.75:.3f} / {dmg * 0.70 * (osval - 0.04) * 0.75:.3f}**__\n'
                         f'下克上 (パッシブ)：**__ボスmob {dmg * 1.07 * (osval - 0.04):.3f} / 通常mob {dmg * 0.7 * osval:.3f}__**',
                   inline=False)

    # ドラゴンキラー
    e_09.add_field(name='条件',
                   value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osval}\n魔法石： {stone_list}\n魔法石倍率：{stone_val}倍') \
        .set_author(name=ctx.author.name) \
        .add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                   value=f'メテオストライク (スペシャル)：**__{sp_dmg * 9 * (osval - 0.02):.3f}__**\n'
                         f'マジックボール (ノーマル)**：__{sp_dmg * 4 * (osval - 0.02):.3f}__**, '
                         f'**(詠唱時：__{sp_dmg * 8 * (osval - 0.02):.3f})__**\n'
                         f'ライトニングボルト (ノーマル)：**__{sp_dmg * 3 * osval:.3f}__**\n'
                         f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                   inline=False) \
        .add_field(name='**†Twilight HeavenRay† (In 輝煌の残滓)**',
                   value=f'神の鉄槌 (スペシャル): __**{sp_dmg * 3 * (osval - 0.02):.3f}**__\n'
                         f'光ある場所に (パッシブ): __**{sp_dmg * 1.2 * (osval - 0.02):.3f}**__', inline=False) \
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osval - 0.02):.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osval - 0.02):.3f}__**', inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * (osval + 0.05):.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * (osval + 0.05):.3f}__**', inline=False) \
        .add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                   value=f'オーバーシュート (スペシャル)：**__{sp_dmg * 12.5 * (osval + 0.05):.3f}__, '
                         f'パッシブあり：__{sp_dmg * 12.5 * 1.5 * (osval + 0.05):.3f}__**'
                         f'\nシャドウパワー (ノーマル)：**__{sp_dmg * 1.7 * 1.5 * (osval + 0.05):.3f}__**'
                         f'\nエレメンタルパワー	(パッシブ)：**__{sp_dmg * 1.7 * 1.5 * (osval + 0.05):.3f}__**',
                   inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osval - 0.02):.3f}__**', inline=False) \
        .add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                   value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{sp_dmg * 8 * (osval - 0.02):.3f}**__') \
        .add_field(name='**シャルル (魔界：ヘルスラ)**',
                   value=f'サテライトキャノン (スペシャル): __**1発 {sp_dmg * 2.5 * (osval + 0.05):.3f} 10発 {sp_dmg * 2.5 * 10 * (osval + 0.05):.3f}**__\n'
                         f'ダークサイクロン (ノーマル): __**1発 {sp_dmg * 1.7 * 0.8 * (osval + 0.05):.3f} 5発 {sp_dmg * 1.7 * 0.8 * 5 * (osval + 0.05):.3f}**__\n'
                         f'インフェライズ (ノーマル): __**{sp_dmg * 2.0 * (osval + 0.05):.3f}**__', inline=False) \
        .add_field(name='**聖剣 (In 浮世の砂海)**',
                   value=f'天下無双 (スペシャル): __**{dmg * 1.07 * (osval - 0.02) * 0.75:.3f} / {dmg * 0.70 * (osval - 0.02) * 0.75:.3f}**__\n'
                         f'下克上 (パッシブ)：**__ボスmob {dmg * 1.07 * (osval - 0.02):.3f} / 通常mob {dmg * 0.7 * (osval - 0.02):.3f}__**',
                   inline=False)

    # プリースト
    e_10.add_field(name='条件',
                   value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osval}\n魔法石： {stone_list}\n魔法石倍率：{stone_val}倍') \
        .set_author(name=ctx.author.name) \
        .add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                   value=f'メテオストライク (スペシャル)：**__{sp_dmg * 9 * (osval - 0.10):.3f}__**\n'
                         f'マジックボール (ノーマル)**：__{sp_dmg * 4 * (osval - 0.10):.3f}__**, '
                         f'**(詠唱時：__{sp_dmg * 8 * (osval - 0.10):.3f})__**\n'
                         f'ライトニングボルト (ノーマル)：**__{sp_dmg * 3 * (osval - 0.10):.3f}__**\n'
                         f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                   inline=False) \
        .add_field(name='**†Twilight HeavenRay† (In 輝煌の残滓)**',
                   value=f'神の鉄槌 (スペシャル): __**{sp_dmg * 3 * (osval - 0.10):.3f}**__\n'
                         f'光ある場所に (パッシブ): __**{sp_dmg * 1.2 * (osval - 0.10):.3f}**__', inline=False) \
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osval - 0.10):.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osval - 0.10):.3f}__**', inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * (osval - 0.10):.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * (osval - 0.10):.3f}__**', inline=False) \
        .add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                   value=f'オーバーシュート (スペシャル)：**__{sp_dmg * 12.5 * (osval - 0.10):.3f}__, '
                         f'パッシブあり：__{sp_dmg * 12.5 * 1.5 * (osval - 0.10):.3f}__**'
                         f'\nシャドウパワー (ノーマル)：**__{sp_dmg * 1.7 * 1.5 * (osval - 0.10):.3f}__**'
                         f'\nエレメンタルパワー	(パッシブ)：**__{sp_dmg * 1.7 * 1.5 * (osval - 0.10):.3f}__**',
                   inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osval - 0.10):.3f}__**', inline=False) \
        .add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                   value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{sp_dmg * 8 * (osval - 0.10):.3f}**__') \
        .add_field(name='**シャルル (魔界：ヘルスラ)**',
                   value=f'サテライトキャノン (スペシャル): __**1発 {sp_dmg * 2.5 * (osval - 0.10):.3f} 10発 {sp_dmg * 2.5 * 10 * (osval - 0.10):.3f}**__\n'
                         f'ダークサイクロン (ノーマル): __**1発 {sp_dmg * 1.7 * 0.8 * (osval - 0.10):.3f} 5発 {sp_dmg * 1.7 * 0.8 * 5 * (osval - 0.10):.3f}**__\n'
                         f'インフェライズ (ノーマル): __**{sp_dmg * 2.0 * (osval - 0.10):.3f}**__', inline=False) \
        .add_field(name='**聖剣 (In 浮世の砂海)**',
                   value=f'天下無双 (スペシャル): __**{dmg * 1.07 * (osval - 0.10) * 0.75:.3f} / {dmg * 0.70 * (osval - 0.10) * 0.75:.3f}**__\n'
                         f'下克上 (パッシブ)：**__ボスmob {dmg * 1.07 * (osval - 0.10):.3f} / 通常mob {dmg * 0.7 * (osval - 0.10):.3f}__**',
                   inline=False)

    # スカーミッッシャー
    e_11.add_field(name='条件',
                   value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osval}\n魔法石： {stone_list}\n魔法石倍率：{stone_val}倍') \
        .set_author(name=ctx.author.name) \
        .add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                   value=f'メテオストライク (スペシャル)：**__{sp_dmg * 9 * osval:.3f}__**\n'
                         f'マジックボール (ノーマル)**：__{sp_dmg * 4 * osval:.3f}__**, '
                         f'**(詠唱時：__{sp_dmg * 8 * osval:.3f})__**\n'
                         f'ライトニングボルト (ノーマル)：**__{sp_dmg * 3 * osval:.3f}__**\n'
                         f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                   inline=False) \
        .add_field(name='**†Twilight HeavenRay† (In 輝煌の残滓)**',
                   value=f'神の鉄槌 (スペシャル): __**{sp_dmg * 3 * osval:.3f}**__\n'
                         f'光ある場所に (パッシブ): __**{sp_dmg * 1.2 * osval:.3f}**__', inline=False) \
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osval + 0.05):.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osval + 0.05):.3f}__**', inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * osval:.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * osval:.3f}__**', inline=False) \
        .add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                   value=f'オーバーシュート (スペシャル)：**__{sp_dmg * 12.5 * osval:.3f}__, '
                         f'パッシブあり：__{sp_dmg * 12.5 * 1.5 * osval:.3f}__**'
                         f'\nシャドウパワー (ノーマル)：**__{sp_dmg * 1.7 * 1.5 * osval:.3f}__**'
                         f'\nエレメンタルパワー	(パッシブ)：**__{sp_dmg * 1.7 * 1.5 * osval:.3f}__**',
                   inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osval + 0.05):.3f}__**', inline=False) \
        .add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                   value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{sp_dmg * 8 * osval:.3f}**__') \
        .add_field(name='**シャルル (魔界：ヘルスラ)**',
                   value=f'サテライトキャノン (スペシャル): __**1発 {sp_dmg * 2.5 * osval:.3f} 10発 {sp_dmg * 2.5 * 10 * osval:.3f}**__\n'
                         f'ダークサイクロン (ノーマル): __**1発 {sp_dmg * 1.7 * 0.8} 5発 {sp_dmg * 1.7 * 0.8 * 5 * osval:.3f}**__\n'
                         f'インフェライズ (ノーマル): __**{sp_dmg * 2.0 * osval:.3f}**__', inline=False) \
        .add_field(name='**聖剣 (In 浮世の砂海)**',
                   value=f'天下無双 (スペシャル): __**{dmg * 1.07 * (osval + 0.05) * 0.75} / {dmg * 0.70 * (osval + 0.05) * 0.75}**__\n'
                         f'下克上 (パッシブ)：**__ボスmob {dmg * 1.07 * (osval + 0.05):.3f} / 通常mob {dmg * 0.7 * (osval + 0.05):.3f}__**',
                   inline=False)

    # ハグレモノ
    e_12.add_field(name='条件',
                   value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osval}\n魔法石： {stone_list}\n魔法石倍率：{stone_val}倍') \
        .set_author(name=ctx.author.name) \
        .add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                   value=f'メテオストライク (スペシャル)：**__{sp_dmg * 9 * (osval - 0.07):.3f}__**\n'
                         f'マジックボール (ノーマル)**：__{sp_dmg * 4 * (osval - 0.07):.3f}__**, '
                         f'**(詠唱時：__{sp_dmg * 8 * (osval - 0.07):.3f})__**\n'
                         f'ライトニングボルト (ノーマル)：**__{sp_dmg * 3 * (osval - 0.07):.3f}__**\n'
                         f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                   inline=False) \
        .add_field(name='**†Twilight HeavenRay† (In 輝煌の残滓)**',
                   value=f'神の鉄槌 (スペシャル): __**{sp_dmg * 3 * (osval - 0.07):.3f}**__\n'
                         f'光ある場所に (パッシブ): __**{sp_dmg * 1.2 * (osval - 0.07):.3f}**__', inline=False) \
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osval - 0.07):.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osval - 0.07):.3f}__**', inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * (osval - 0.07):.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * (osval - 0.07):.3f}__**', inline=False) \
        .add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                   value=f'オーバーシュート (スペシャル)：**__{sp_dmg * 12.5 * (osval - 0.07):.3f}__, '
                         f'パッシブあり：__{sp_dmg * 12.5 * 1.5 * (osval - 0.07):.3f}__**'
                         f'\nシャドウパワー (ノーマル)：**__{sp_dmg * 1.7 * 1.5 * (osval - 0.07):.3f}__**'
                         f'\nエレメンタルパワー	(パッシブ)：**__{sp_dmg * 1.7 * 1.5 * (osval - 0.07):.3f}__**',
                   inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osval - 0.07):.3f}__**', inline=False) \
        .add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                   value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{sp_dmg * 8 * (osval - 0.07):.3f}**__') \
        .add_field(name='**シャルル (魔界：ヘルスラ)**',
                   value=f'サテライトキャノン (スペシャル): __**1発 {sp_dmg * 2.5 * (osval - 0.07):.3f} 10発 {sp_dmg * 2.5 * 10 * (osval - 0.07):.3f}**__\n'
                         f'ダークサイクロン (ノーマル): __**1発 {sp_dmg * 1.7 * 0.8 * (osval - 0.07):.3f} 5発 {sp_dmg * 1.7 * 0.8 * 5 * (osval - 0.07):.3f}**__\n'
                         f'インフェライズ (ノーマル): __**{sp_dmg * 2.0 * (osval - 0.07):.3f}**__', inline=False) \
        .add_field(name='**聖剣 (In 浮世の砂海)**',
                   value=f'天下無双 (スペシャル): __**{dmg * 1.07 * (osval - 0.07) * 0.75} / {dmg * 0.70 * (osval - 0.07) * 0.75}**__\n'
                         f'下克上 (パッシブ)：**__ボスmob {dmg * 1.07 * (osval - 0.07):.3f} / 通常mob {dmg * 0.7 * (osval - 0.07):.3f}__**',
                   inline=False)

    # ルーンキャスター
    e_13.add_field(name='条件',
                   value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osval}\n魔法石： {stone_list}\n魔法石倍率：{stone_val}倍') \
        .set_author(name=ctx.author.name) \
        .add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                   value=f'メテオストライク (スペシャル)：**__{sp_dmg * 9 * (osval + 0.07):.3f}__**\n'
                         f'マジックボール (ノーマル)**：__{sp_dmg * 4 * (osval + 0.07):.3f}__**, '
                         f'**(詠唱時：__{sp_dmg * 8 * (osval + 0.07):.3f})__**\n'
                         f'ライトニングボルト (ノーマル)：**__{sp_dmg * 3 * (osval + 0.07):.3f}__**\n'
                         f'ファイヤ・ボルケーノ: __**{sp_dmg * 22 * (osval + 0.07):.3f}**__',
                   inline=False) \
        .add_field(name='**†Twilight HeavenRay† (In 輝煌の残滓)**',
                   value=f'神の鉄槌 (スペシャル): __**{sp_dmg * 3 * (osval + 0.07):.3f}**__\n'
                         f'光ある場所に (パッシブ): __**{sp_dmg * 1.2 * (osval + 0.07):.3f}**__', inline=False) \
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osval - 0.07):.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osval - 0.07):.3f}__**', inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * (osval - 0.07):.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * (osval - 0.07):.3f}__**', inline=False) \
        .add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                   value=f'オーバーシュート (スペシャル)：**__{sp_dmg * 12.5 * (osval - 0.07):.3f}__, '
                         f'パッシブあり：__{sp_dmg * 12.5 * 1.5 * (osval - 0.07):.3f}__**'
                         f'\nシャドウパワー (ノーマル)：**__{sp_dmg * 1.7 * 1.5 * (osval - 0.07):.3f}__**'
                         f'\nエレメンタルパワー	(パッシブ)：**__{sp_dmg * 1.7 * 1.5 * (osval - 0.07):.3f}__**',
                   inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osval - 0.07):.3f}__**', inline=False) \
        .add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                   value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{sp_dmg * 8 * (osval - 0.07):.3f}**__') \
        .add_field(name='**シャルル (魔界：ヘルスラ)**',
                   value=f'サテライトキャノン (スペシャル): __**1発 {sp_dmg * 2.5 * (osval - 0.07):.3f} 10発 {sp_dmg * 2.5 * 10 * (osval - 0.07):.3f}**__\n'
                         f'ダークサイクロン (ノーマル): __**1発 {sp_dmg * 1.7 * 0.8 * (osval - 0.07):.3f} 5発 {sp_dmg * 1.7 * 0.8 * 5 * (osval - 0.07):.3f}**__\n'
                         f'インフェライズ (ノーマル): __**{sp_dmg * 2.0 * (osval - 0.07):.3f}**__', inline=False) \
        .add_field(name='**聖剣 (In 浮世の砂海)**',
                   value=f'天下無双 (スペシャル): __**{dmg * 1.07 * (osval - 0.07) * 0.75} / {dmg * 0.70 * (osval - 0.07) * 0.75}**__\n'
                         f'下克上 (パッシブ)：**__ボスmob {dmg * 1.07 * (osval - 0.07):.3f} / 通常mob {dmg * 0.7 * (osval - 0.07):.3f}__**',
                   inline=False)

    # スペランカー
    e_14.add_field(name='条件',
                   value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osval}\n魔法石： {stone_list}\n魔法石倍率：{stone_val}倍') \
        .set_author(name=ctx.author.name) \
        .add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                   value=f'メテオストライク (スペシャル)：**__{sp_dmg * 9 * (osval + 0.10):.3f}__**\n'
                         f'マジックボール (ノーマル)**：__{sp_dmg * 4 * (osval + 0.10):.3f}__**, '
                         f'**(詠唱時：__{sp_dmg * 8 * (osval + 0.10):.3f})__**\n'
                         f'ライトニングボルト (ノーマル)：**__{sp_dmg * 3 * (osval + 0.10):.3f}__**\n'
                         f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                   inline=False) \
        .add_field(name='**†Twilight HeavenRay† (In 輝煌の残滓)**',
                   value=f'神の鉄槌 (スペシャル): __**{sp_dmg * 3 * (osval + 0.10):.3f}**__\n'
                         f'光ある場所に (パッシブ): __**{sp_dmg * 1.2 * (osval + 0.10):.3f}**__', inline=False) \
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osval + 0.10):.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osval + 0.10):.3f}__**', inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * (osval + 0.10):.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * (osval + 0.10):.3f}__**', inline=False) \
        .add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                   value=f'オーバーシュート (スペシャル)：**__{sp_dmg * 12.5 * (osval + 0.10):.3f}__, '
                         f'パッシブあり：__{sp_dmg * 12.5 * 1.5 * (osval + 0.10):.3f}__**'
                         f'\nシャドウパワー (ノーマル)：**__{sp_dmg * 1.7 * 1.5 * (osval + 0.10):.3f}__**'
                         f'\nエレメンタルパワー	(パッシブ)：**__{sp_dmg * 1.7 * 1.5 * (osval + 0.10):.3f}__**',
                   inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osval + 0.10):.3f}__**', inline=False) \
        .add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                   value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{sp_dmg * 8 * (osval + 0.10):.3f}**__') \
        .add_field(name='**シャルル (魔界：ヘルスラ)**',
                   value=f'サテライトキャノン (スペシャル): __**1発 {sp_dmg * 2.5 * (osval + 0.10):.3f} 10発 {sp_dmg * 2.5 * 10 * (osval + 0.10):.3f}**__\n'
                         f'ダークサイクロン (ノーマル): __**1発 {sp_dmg * 1.7 * 0.8 * (osval + 0.10):.3f} 5発 {sp_dmg * 1.7 * 0.8 * 5 * (osval + 0.10):.3f}**__\n'
                         f'インフェライズ (ノーマル): __**{sp_dmg * 2.0 * (osval + 0.10):.3f}**__', inline=False) \
        .add_field(name='**聖剣 (In 浮世の砂海)**',
                   value=f'天下無双 (スペシャル): __**{dmg * 1.07 * (osval + 0.10) * 0.75} / {dmg * 0.70 * (osval + 0.10) * 0.75}**__\n'
                         f'下克上 (パッシブ)：**__ボスmob {dmg * 1.07 * (osval + 0.10):.3f} / 通常mob {dmg * 0.7 * (osval + 0.10):.3f}__**',
                   inline=False)

    # アーサー
    e_15.add_field(name='条件',
                   value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osval}\n魔法石： {stone_list}\n魔法石倍率：{stone_val}倍') \
        .set_author(name=ctx.author.name) \
        .add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                   value=f'メテオストライク (スペシャル)：**__{sp_dmg * 9 * (osval + 0.05):.3f}__**\n'
                         f'マジックボール (ノーマル)**：__{sp_dmg * 4 * (osval + 0.05):.3f}__**, '
                         f'**(詠唱時：__{sp_dmg * 8 * (osval + 0.05):.3f})__**\n'
                         f'ライトニングボルト (ノーマル)：**__{sp_dmg * 3 * (osval + 0.05):.3f}__**\n'
                         f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                   inline=False) \
        .add_field(name='**†Twilight HeavenRay† (In 輝煌の残滓)**',
                   value=f'神の鉄槌 (スペシャル): __**{sp_dmg * 3 * (osval + 0.05):.3f}**__\n'
                         f'光ある場所に (パッシブ): __**{sp_dmg * 1.2 * (osval + 0.05):.3f}**__', inline=False) \
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osval + 0.05):.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osval + 0.05):.3f}__**', inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * (osval - 0.05):.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * (osval - 0.05):.3f}__**', inline=False) \
        .add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                   value=f'オーバーシュート (スペシャル)：**__{sp_dmg * 12.5 * (osval - 0.05):.3f}__, '
                         f'パッシブあり：__{sp_dmg * 12.5 * 1.5 * (osval - 0.05):.3f}__**'
                         f'\nシャドウパワー (ノーマル)：**__{sp_dmg * 1.7 * 1.5 * (osval - 0.05):.3f}__**'
                         f'\nエレメンタルパワー	(パッシブ)：**__{sp_dmg * 1.7 * 1.5 * (osval - 0.05):.3f}__**',
                   inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osval + 0.05):.3f}__**', inline=False) \
        .add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                   value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{sp_dmg * 8 * (osval - 0.05):.3f}**__') \
        .add_field(name='**シャルル (魔界：ヘルスラ)**',
                   value=f'サテライトキャノン (スペシャル): __**1発 {sp_dmg * 2.5 * (osval - 0.05):.3f} 10発 {sp_dmg * 2.5 * 10 * (osval - 0.05):.3f}**__\n'
                         f'ダークサイクロン (ノーマル): __**1発 {sp_dmg * 1.7 * 0.8 * (osval - 0.05):.3f} 5発 {sp_dmg * 1.7 * 0.8 * 5 * (osval - 0.05):.3f}**__\n'
                         f'インフェライズ (ノーマル): __**{sp_dmg * 2.0 * (osval - 0.05):.3f}**__', inline=False) \
        .add_field(name='**聖剣 (In 浮世の砂海)**',
                   value=f'天下無双 (スペシャル): __**{dmg * 1.07 * (osval + 0.05) * 0.75:.3f} / {dmg * 0.70 * (osval + 0.05) * 0.75:.3f}**__\n'
                         f'下克上 (パッシブ)：**__ボスmob {dmg * 1.07 * (osval + 0.05):.3f} / 通常mob {dmg * 0.7 * (osval + 0.05):.3f}__**',
                   inline=False)

    # シーカー
    e_16.add_field(name='条件',
                   value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osval}\n魔法石： {stone_list}\n魔法石倍率：{stone_val}倍') \
        .set_author(name=ctx.author.name) \
        .add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                   value=f'メテオストライク (スペシャル)：**__{sp_dmg * 9 * (osval - 0.04):.3f}__**\n'
                         f'マジックボール (ノーマル)**：__{sp_dmg * 4 * (osval - 0.04):.3f}__**, '
                         f'**(詠唱時：__{sp_dmg * 8 * (osval - 0.04):.3f})__**\n'
                         f'ライトニングボルト (ノーマル)：**__{sp_dmg * 3 * (osval - 0.04):.3f}__**\n'
                         f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                   inline=False) \
        .add_field(name='**†Twilight HeavenRay† (In 輝煌の残滓)**',
                   value=f'神の鉄槌 (スペシャル): __**{sp_dmg * 3 * (osval - 0.04):.3f}**__\n'
                         f'光ある場所に (パッシブ): __**{sp_dmg * 1.2 * (osval - 0.04):.3f}**__', inline=False) \
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osval - 0.04):.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osval - 0.04):.3f}__**', inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * (osval + 0.10):.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * (osval + 0.10):.3f}__**', inline=False) \
        .add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                   value=f'オーバーシュート (スペシャル)：**__{sp_dmg * 12.5 * (osval + 0.10):.3f}__, '
                         f'パッシブあり：__{sp_dmg * 12.5 * 1.5 * (osval + 0.10):.3f}__**'
                         f'\nシャドウパワー (ノーマル)：**__{sp_dmg * 1.7 * 1.5 * (osval + 0.10):.3f}__**'
                         f'\nエレメンタルパワー	(パッシブ)：**__{sp_dmg * 1.7 * 1.5 * (osval + 0.10):.3f}__**',
                   inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osval - 0.04):.3f}__**', inline=False) \
        .add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                   value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{sp_dmg * 8 * (osval + 0.10):.3f}**__') \
        .add_field(name='**シャルル (魔界：ヘルスラ)**',
                   value=f'サテライトキャノン (スペシャル): __**1発 {sp_dmg * 2.5 * (osval + 0.10):.3f} 10発 {sp_dmg * 2.5 * 10 * (osval + 0.10):.3f}**__\n'
                         f'ダークサイクロン (ノーマル): __**1発 {sp_dmg * 1.7 * 0.8 * (osval + 0.10):.3f} 5発 {sp_dmg * 1.7 * 0.8 * 5 * (osval + 0.10):.3f}**__\n'
                         f'インフェライズ (ノーマル): __**{sp_dmg * 2.0 * (osval + 0.10):.3f}**__', inline=False) \
        .add_field(name='**聖剣 (In 浮世の砂海)**',
                   value=f'天下無双 (スペシャル): __**{dmg * 1.07 * (osval - 0.04) * 0.75:.3f} / {dmg * 0.70 * (osval - 0.04) * 0.75:.3f}**__\n'
                         f'下克上 (パッシブ)：**__ボスmob {dmg * 1.07 * (osval - 0.04):.3f} / 通常mob {dmg * 0.7 * (osval - 0.04):.3f}__**',
                   inline=False)

    # スカルピアサー
    e_17.add_field(name='条件',
                   value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osval}\n魔法石： {stone_list}\n魔法石倍率：{stone_val}倍') \
        .set_author(name=ctx.author.name) \
        .add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                   value=f'メテオストライク (スペシャル)：**__{sp_dmg * 9 * osval:.3f},  ゾンビ: {sp_dmg * 9 * osval * 0.90:.3f}__**\n'
                         f'マジックボール (ノーマル)**：__{sp_dmg * 4 * osval:.3f},  ゾンビ: {sp_dmg * 4 * osval * 0.90:.3f}__**, '
                         f'__**(詠唱時：{sp_dmg * 8 * osval:.3f},  ゾンビ: {sp_dmg * 8 * osval * 0.90:.3f})__**\n'
                         f'ライトニングボルト (ノーマル)：**__{sp_dmg * 3 * osval:.3f},  ゾンビ: {sp_dmg * 3 * osval * 0.90:.3f}__**\n'
                         f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                   inline=False) \
        .add_field(name='**†Twilight HeavenRay† (In 輝煌の残滓)**',
                   value=f'神の鉄槌 (スペシャル): __**{sp_dmg * 3 * osval:.3f},  ゾンビ: {sp_dmg * 3 * osval * 0.90:.3f}**__\n'
                         f'光ある場所に (パッシブ): __**{sp_dmg * 1.2 * osval:.3f},  ゾンビ: {sp_dmg * 1.2 * osval * 0.90:.3f}**__',
                   inline=False) \
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * osval:.3f},  ゾンビ: {dmg * 7 * osval * 0.90:.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * osval:.3f},  ゾンビ: {dmg * 4 * osval * 0.90:.3f}__**',
                   inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * osval:.3f},  ゾンビ: {sp_dmg * 1.1 * 7 * osval * 0.90:.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * osval:.3f},  ゾンビ: {sp_dmg * 4 * osval * 0.90:.3f}__**',
                   inline=False) \
        .add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                   value=f'オーバーシュート (スペシャル)：**__{sp_dmg * 12.5 * osval:.3f},  ゾンビ: {sp_dmg * 12.5 * osval * 0.90:.3f}__, '
                         f'パッシブあり：__{sp_dmg * 12.5 * 1.5 * osval:.3f},  ゾンビ: {sp_dmg * 12.5 * osval * 0.90:.3f}__**'
                         f'\nシャドウパワー (ノーマル)：**__{sp_dmg * 1.7 * 1.5 * osval:.3f}__**'
                         f'\nエレメンタルパワー	(パッシブ)：**__{sp_dmg * 1.7 * 1.5 * osval:.3f}__**',
                   inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * osval:.3f},  ゾンビ: {dmg * 2.5 * osval * 0.90:.3f}__**',
                   inline=False) \
        .add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                   value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{sp_dmg * 8 * osval:.3f},  ゾンビ: {sp_dmg * 8 * osval * 0.90:.3f}**__') \
        .add_field(name='**シャルル (魔界：ヘルスラ)**',
                   value=f'サテライトキャノン (スペシャル): __**1発 {sp_dmg * 2.5 * osval:.3f},  ゾンビ: {sp_dmg * 2.5 * osval * 0.90:.3f}**__\n'
                         f'__**10発 {sp_dmg * 2.5 * 10 * osval:.3f},  ゾンビ: {sp_dmg * 2.5 * 10 * osval * 0.90:.3f}**__\n'
                         f'ダークサイクロン (ノーマル): __**1発 {sp_dmg * 1.7 * 0.8 * osval:.3f},  ゾンビ: {sp_dmg * 1.7 * osval * 0.90:.3f}**__\n'
                         f'5発 {dmg * 1.7 * 0.8 * 5 * osval:.3f},  ゾンビ: {sp_dmg * 1.7 * 0.8 * 5 * osval * 0.90:.3f}**__\n'
                         f'インフェライズ (ノーマル): __**{sp_dmg * 2.0 * osval:.3f},  ゾンビ: {sp_dmg * 2.0 * osval * 0.90:.3f}**__',
                   inline=False) \
        .add_field(name='**聖剣 (In 浮世の砂海)**',
                   value=f'天下無双 (スペシャル): __**{dmg * 1.30 * osval * 0.75:.3f},  ゾンビ: {dmg * 1.30 * 0.75 * osval * 0.90:.3f}**__\n'
                         f'__** / 通常mob {dmg * 0.70 * osval * 0.75:.3f},  ゾンビ: {dmg * 0.70 * 0.75 * osval * 0.90:.3f}**__\n'
                         f'下克上 (パッシブ)：**__ボスmob {dmg * 1.30 * osval:.3f},  ゾンビ: {dmg * 1.30 * osval * 0.90:.3f}**__\n'
                         f'__** / 通常mob {dmg * 0.7 * osval:.3f},  ゾンビ: {dmg * 0.70 * osval * 0.90:.3f}__**',
                   inline=False)

    # バタフライシーカー
    e_18.add_field(name='条件',
                   value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osval}\n魔法石： {stone_list}\n魔法石倍率：{stone_val}倍') \
        .set_author(name=ctx.author.name) \
        .add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                   value=f'メテオストライク (スペシャル)：**__{sp_dmg * 9 * (osval - 0.07):.3f}__**\n'
                         f'マジックボール (ノーマル)**：__{sp_dmg * 4 * (osval - 0.07):.3f}__**, '
                         f'**(詠唱時：__{sp_dmg * 8 * (osval - 0.07):.3f})__**\n'
                         f'ライトニングボルト (ノーマル)：**__{sp_dmg * 3 * (osval - 0.07):.3f}__**\n'
                         f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                   inline=False) \
        .add_field(name='**†Twilight HeavenRay† (In 輝煌の残滓)**',
                   value=f'神の鉄槌 (スペシャル): __**{sp_dmg * 3 * (osval - 0.07):.3f}**__\n'
                         f'光ある場所に (パッシブ): __**{sp_dmg * 1.2 * (osval - 0.07):.3f}**__', inline=False) \
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osval - 0.07):.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osval - 0.07):.3f}__**', inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * (osval + 0.10):.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * (osval + 0.10):.3f}__**', inline=False) \
        .add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                   value=f'オーバーシュート (スペシャル)：**__{sp_dmg * 12.5 * (osval + 0.10):.3f}__, '
                         f'パッシブあり：__{sp_dmg * 12.5 * 1.5 * (osval + 0.10):.3f}__**'
                         f'\nシャドウパワー (ノーマル)：**__{sp_dmg * 1.7 * 1.5 * (osval + 0.10):.3f}__**'
                         f'\nエレメンタルパワー	(パッシブ)：**__{dmg * 1.7 * 1.5 * (osval + 0.10):.3f}__**',
                   inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osval - 0.07):.3f}__**', inline=False) \
        .add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                   value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{sp_dmg * 8 * (osval - 0.07):.3f}**__') \
        .add_field(name='**シャルル (魔界：ヘルスラ)**',
                   value=f'サテライトキャノン (スペシャル): __**1発 {sp_dmg * 2.5 * (osval - 0.07):.3f} 10発 {sp_dmg * 2.5 * 10 * (osval - 0.07):.3f}**__\n'
                         f'ダークサイクロン (ノーマル): __**1発 {sp_dmg * 1.7 * 0.8 * (osval - 0.07):.3f} 5発 {sp_dmg * 1.7 * 0.8 * 5 * (osval - 0.07):.3f}**__\n'
                         f'インフェライズ (ノーマル): __**{sp_dmg * 2.0 * (osval - 0.07):.3f}**__', inline=False) \
        .add_field(name='**聖剣 (In 浮世の砂海)**',
                   value=f'天下無双 (スペシャル): __**{dmg * 1.07 * (osval - 0.07) * 0.75} / {dmg * 0.70 * (osval - 0.07) * 0.75}**__\n'
                         f'下克上 (パッシブ)：**__ボスmob {dmg * 1.07 * (osval - 0.07):.3f} / 通常mob {dmg * 0.7 * (osval - 0.07):.3f}__**',
                   inline=False)

    # アレイスター
    e_19.add_field(name='条件',
                   value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osval}\n魔法石： {stone_list}\n魔法石倍率：{stone_val}倍') \
        .set_author(name=ctx.author.name) \
        .add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                   value=f'メテオストライク (スペシャル)：**__{sp_dmg * 9 * osval:.3f}__**\n'
                         f'マジックボール (ノーマル)**：__{sp_dmg * 4 * osval:.3f}__**, '
                         f'**(詠唱時：__{sp_dmg * 8 * osval:.3f})__**\n'
                         f'ライトニングボルト (ノーマル)：**__{sp_dmg * 3 * osval:.3f}__**\n'
                         f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                   inline=False) \
        .add_field(name='**†Twilight HeavenRay† (In 輝煌の残滓)**',
                   value=f'神の鉄槌 (スペシャル): __**{sp_dmg * 3 * osval:.3f}**__\n'
                         f'光ある場所に (パッシブ): __**{sp_dmg * 1.2 * osval:.3f}**__', inline=False) \
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osval - 0.05):.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osval - 0.05):.3f}__**', inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * osval:.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * osval:.3f}__**', inline=False) \
        .add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                   value=f'オーバーシュート (スペシャル)：**__{sp_dmg * 12.5 * osval:.3f}__, '
                         f'パッシブあり：__{sp_dmg * 12.5 * 1.5 * osval:.3f}__**'
                         f'\nシャドウパワー (ノーマル)：**__{sp_dmg * 1.7 * 1.5 * osval:.3f}__**'
                         f'\nエレメンタルパワー	(パッシブ)：**__{sp_dmg * 1.7 * 1.5 * osval:.3f}__**',
                   inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osval - 0.05):.3f}__**', inline=False) \
        .add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                   value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{sp_dmg * 8 * osval:.3f}**__') \
        .add_field(name='**シャルル (魔界：ヘルスラ)**',
                   value=f'サテライトキャノン (スペシャル): __**1発 {sp_dmg * 2.5 * osval:.3f} 10発 {sp_dmg * 2.5 * 10 * osval:.3f}**__\n'
                         f'ダークサイクロン (ノーマル): __**1発 {sp_dmg * 1.7 * 0.8:.3f} 5発 {sp_dmg * 1.7 * 0.8 * 5 * osval:.3f}**__\n'
                         f'インフェライズ (ノーマル): __**{sp_dmg * 2.0 * osval:.3f}**__', inline=False) \
        .add_field(name='**聖剣 (In 浮世の砂海)**',
                   value=f'天下無双 (スペシャル): __**{dmg * 1.07 * (osval - 0.05) * 0.75:.3f} / {dmg * 0.70 * (osval - 0.05) * 0.75:.3f}**__\n'
                         f'下克上 (パッシブ)：**__ボスmob {dmg * 1.07 * (osval - 0.05):.3f} / 通常mob {dmg * 0.7 * (osval - 0.05):.3f}__**',
                   inline=False)

    # ダークブラスター
    e_20.add_field(name='条件',
                   value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osval}\n魔法石： {stone_list}\n魔法石倍率：{stone_val}倍') \
        .set_author(name=ctx.author.name) \
        .add_field(name='**ルーンオブアルカディア (In Lux et Tenebrae) ,~Rune of Arcadia~ (In 追憶と創成の間)**',
                   value=f'メテオストライク (スペシャル)：**__{sp_dmg * 9 * osval:.3f},  スケルトン: {sp_dmg * 9 * osval * 0.90:.3f}__**\n'
                         f'マジックボール (ノーマル)**：__{sp_dmg * 4 * osval:.3f},  スケルトン: {sp_dmg * 4 * osval * 0.90:.3f}__**, '
                         f'**(詠唱時：__{sp_dmg * 8 * osval:.3f},  スケルトン: {sp_dmg * 8 * osval * 0.90:.3f})__**\n'
                         f'ライトニングボルト (ノーマル)：**__{sp_dmg * 3 * osval:.3f},  スケルトン: {sp_dmg * 3 * osval * 0.90:.3f}__**\n'
                         f'**(ファイヤ・ボルケーノ はルーンキャスターのみ使用可能。)**',
                   inline=False) \
        .add_field(name='**†Twilight HeavenRay† (In 輝煌の残滓)**',
                   value=f'神の鉄槌 (スペシャル): __**{sp_dmg * 3 * osval:.3f},  スケルトン: {sp_dmg * 3 * osval * 0.90:.3f}**__\n'
                         f'光ある場所に (パッシブ): __**{sp_dmg * 1.2 * osval:.3f},  スケルトン: {sp_dmg * 1.2 * osval * 0.90:.3f}**__',
                   inline=False) \
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * osval:.3f},  スケルトン: {sp_dmg * 7 * osval * 0.90:.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * osval:.3f},  スケルトン: {sp_dmg * 4 * osval * 0.90:.3f}__**',
                   inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * osval:.3f},  スケルトン: {sp_dmg * 1.1 * 7 * osval * 0.90:.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * osval:.3f},  スケルトン: {sp_dmg * 4 * osval * 0.90:.3f}__**',
                   inline=False) \
        .add_field(name=f'**~繊翳~ (In Xen\'s Castle)**',
                   value=f'オーバーシュート (スペシャル)：**__{sp_dmg * 12.5 * osval:.3f},  スケルトン: {sp_dmg * 12.5 * osval * 0.90:.3f}__, '
                         f'パッシブあり：__{sp_dmg * 12.5 * 1.5 * osval:.3f},  スケルトン: {sp_dmg * 12.5 * 1.5 * osval * 0.90:.3f}__**'
                         f'\nシャドウパワー (ノーマル)：**__{sp_dmg * 1.7 * 1.5 * osval:.3f},  スケルトン: {sp_dmg * 1.7 * 1.5 * osval * 0.90:.3f}__**'
                         f'\nエレメンタルパワー	(パッシブ)：**__{sp_dmg * 1.7 * 1.5 * osval:.3f},  スケルトン: {sp_dmg * 1.7 * 1.5 * osval * 0.90:.3f}__**',
                   inline=False)

    e_21.set_author(name=ctx.author.name) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * osval:.3f},  スケルトン: {dmg * 2.5 * osval * 0.90:.3f}__**',
                   inline=False) \
        .add_field(name=f'**Dorachenbogen・HässlichesBogen (In ドラゴンの谷)**',
                   value=f'-黒竜- ヘイロン -滅-	(スペシャル)：__**{sp_dmg * 8 * osval:.3f},  スケルトン: {sp_dmg * 8 * osval * 0.90:.3f}**__') \
        .add_field(name='**シャルル (魔界：ヘルスラ)**',
                   value=f'サテライトキャノン (スペシャル): __**1発 {sp_dmg * 2.5 * osval:.3f},  スケルトン: {sp_dmg * 2.5 * osval * 0.90:.3f}**__\n'
                         f'__** 10発 {sp_dmg * 2.5 * 10 * osval:.3f},  スケルトン: {sp_dmg * 2.5 * 10 * osval * 0.90:.3f}**__\n'
                         f'ダークサイクロン (ノーマル): __**1発 {sp_dmg * 1.7 * 0.8 * osval:.3f},  スケルトン: {sp_dmg * 1.7 * 0.8 * osval * 0.90:.3f}**__\n'
                         f'__** 5発 {sp_dmg * 1.7 * 0.8 * 5 * osval:.3f},  スケルトン: {sp_dmg * 1.7 * 0.8 * osval * 0.90:.3f}**__\n'
                         f'インフェライズ (ノーマル): __**{sp_dmg * 2.0 * osval:.3f},  スケルトン: {sp_dmg * 2.0 * osval * 0.90:.3f}**__',
                   inline=False) \
        .add_field(name='**聖剣 (In 浮世の砂海)**',
                   value=f'天下無双 (スペシャル): __**{sp_dmg * 1.07 * osval * 0.75:.3f},  スケルトン: {dmg * 1.07 * 0.75 * osval * 0.90:.3f}**__\n'
                         f'__** / {sp_dmg * 0.70 * osval * 0.75:.3f},  スケルトン: {dmg * 0.70 * 0.75 * osval * 0.90:.3f}**__\n'
                         f'下克上 (パッシブ)：**__ボスmob {sp_dmg * 1.07 * osval:.3f},  スケルトン: {dmg * 1.07 * osval * 0.90:.3f}**__\n'
                         f'__** / 通常mob {sp_dmg * 0.7 * osval:.3f},  スケルトン: {dmg * 0.7 * osval * 0.90:.3f}__**',
                   inline=False) \
        .add_field(name='**冥剣, トワ剣**',
                   value=f'Boss: {dmg * 1.30 * osval:.3f},  スケルトン: {dmg * 1.30 * osval * 0.90:.3f}\n'
                         f'(冥剣 mob: {dmg * 0.70 * osval:.3f},  スケルトン: {dmg * 0.70 * osval * 0.90:.3f})', inline=False) \
        .add_field(name='**Amərətāt**',
                   value=f'__**Boss: {dmg * 1.10 * osval:.3f},  スケルトン: {dmg * 1.10 * osval * 0.90:.3f}**__',
                   inline=False)

    return [e_01, e_02, e_03, e_04, e_05, e_06, e_07, e_08, e_09, e_10, e_11, e_12, e_13, e_14, e_15, e_16, e_17, e_18,
            e_19, e_20, e_21]


# 魔根設定！！！！！！
async def embeds_list_job(ctx, dmg: float, raw: float, os: int, osraw: float, alpha: float, r: list, makon=1.0) -> list[discord.Embed]:
    """This function creates a list of embeds to be sent to the user

    Parameters
    ----------
    ctx
        the context of the command
    dmg : float
        The damage of the weapon.
    raw : float
        The raw damage of the weapon
    os : int
        The OS of the device.
    osraw : float
        The raw value of the OS.
    alpha : float
        the alpha value of the embeds
    r : list
        list of the raw data
    makon
        The multiplier for the damage.

    """
    r = ', '.join(r)
    embed_1_job = discord.Embed(title='職業', color=discord.Color.dark_green(),
                                url='https://wikiwiki.jp/thelow/%E8%81%B7%E6%A5%AD')
    embed_1_job.set_author(name=f"By {ctx.author}")

    embed_1_job.add_field(name='条件', value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n'
                                           f'魔法石： {r}\n魔法石倍率： {alpha}倍')
    embed_1_job.add_field(name='\U000025b6\U0000fe0fソルジャー', value=f'__**攻撃力：剣：+5%: {float(dmg * (osraw + 0.05)):.3f},'
                                                                  f' 弓：-2%: {float(dmg * (osraw - 0.02) * makon):.3f},'
                                                                  f' 魔法：-2%: {float(dmg * (osraw - 0.02)):.3f}**__\n\n'
                                                                  f'**聖剣 (Boss : {float(dmg * (osraw + 0.05) * 1.07):.3f} / '
                                                                  f'Mob : {float(dmg * (osraw + 0.05) * 0.70):.3f})\n'
                                                                  f'魔混系武器 : {float(dmg * (osraw - 0.02) * 1.70):.3f}**',
                          inline=False)

    embed_1_job.add_field(name='\U000025b6\U0000fe0fアーチャー', value=f"__**攻撃力：剣：-2%: {float(dmg * (osraw - 0.02)):.3f},"
                                                                  f" 弓：+5%: {float(dmg * (osraw + 0.05) * makon):.3f},"
                                                                  f" 魔法：-2%: {float(dmg * (osraw - 0.02)):.3f}**__\n\n"
                                                                  f"**聖剣 (Boss : {float(dmg * (osraw - 0.02) * 1.07):.3f} / "
                                                                  f"Mob : {float(dmg * (osraw - 0.02) * 0.70):.3f})\n"
                                                                  f"魔混系武器 : {float(dmg * (osraw + 0.05) * 1.70):.3f}**",
                          inline=False)

    embed_1_job.add_field(name='\U000025b6\U0000fe0fマジシャン', value=f"__**攻撃力：剣：-2%: {float(dmg * (osraw - 0.02)):.3f},"
                                                                  f" 弓：-2%: {float(dmg * (osraw - 0.02) * makon):.3f},"
                                                                  f" 魔法：+5%: {float(dmg * (osraw + 0.05)):.3f}**__\n\n"
                                                                  f"**聖剣 (Boss : {float(dmg * (osraw - 0.02) * 1.07):.3f} / "
                                                                  f"Mob : {float(dmg * (osraw - 0.02) * 0.70):.3f})\n"
                                                                  f"魔混系武器 : {float(dmg * (osraw - 0.02) * 1.70):.3f}**",
                          inline=False)

    embed_1_job.set_footer(text='Page 1 of 5')

    embed_2_job = discord.Embed(title='職業', color=discord.Color.dark_green(),
                                url='https://wikiwiki.jp/thelow/%E8%81%B7%E6%A5%AD')

    embed_2_job.set_author(name=f"By {ctx.author}")
    embed_2_job.add_field(name='条件', value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}'
                                           f'\n魔法石倍率： {alpha}倍')

    embed_2_job.add_field(name='\U000025b6\U0000fe0fウォーリア', value=f"__**攻撃力：剣：+10%: {float(dmg * (osraw + 0.10)):.3f},"
                                                                  f" 弓： -5%: {float(dmg * (osraw - 0.05) * makon):.3f},"
                                                                  f" 魔法： -5%: {float(dmg * (osraw - 0.05)):.3f}**__\n\n"
                                                                  f"**聖剣 (Boss : {float(dmg * (osraw + 0.10) * 1.07):.3f} / "
                                                                  f"Mob : {float(dmg * (osraw + 0.10) * 0.70):.3f})\n"
                                                                  f"魔混系武器 : {float(dmg * (osraw - 0.05) * 1.70):.3f}**",
                          inline=False)

    embed_2_job.add_field(name='\U000025b6\U0000fe0fボウマン', value=f"__**攻撃力：剣： -5%: {float(dmg * (osraw - 0.05)):.3f},"
                                                                 f" 弓：+10%: {float(dmg * (osraw + 0.10) * makon):.3f},"
                                                                 f" 魔法： -5%: {float(dmg * (osraw - 0.05)):.3f}**__\n\n"
                                                                 f"**聖剣 (Boss : {float(dmg * (osraw - 0.05) * 1.07):.3f} / "
                                                                 f"Mob : {float(dmg * (osraw - 0.05) * 0.70):.3f})\n"
                                                                 f"魔混系武器 : {float(dmg * (osraw + 0.10) * 1.70):.3f}**",
                          inline=False)

    embed_2_job.add_field(name='\U000025b6\U0000fe0fメイジ', value=f"__**攻撃力：剣： -5%: {float(dmg * (osraw - 0.05)):.3f},"
                                                                f" 弓： -5%: {float(dmg * (osraw - 0.05) * makon):.3f},"
                                                                f" 魔法：+10: {float(dmg * (osraw + 0.10)):.3f}**__\n\n"
                                                                f"**聖剣 (Boss : {float(dmg * (osraw - 0.05) * 1.07):.3f} / "
                                                                f"Mob : {float(dmg * (osraw - 0.05) * 0.70):.3f})\n"
                                                                f"魔混系武器 : {float(dmg * (osraw - 0.05) * 1.70):.3f}**",
                          inline=False)

    embed_2_job.set_footer(text='Page 2 of 5')

    embed_3_job = discord.Embed(title='職業', color=discord.Color.dark_green(),
                                url='https://wikiwiki.jp/thelow/%E8%81%B7%E6%A5%AD')

    embed_3_job.set_author(name=f"By {ctx.author}")
    embed_3_job.add_field(name='条件', value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n'
                                           f'魔法石倍率： {alpha}倍')

    embed_3_job.add_field(name='\U000025b6\U0000fe0fロウニン', value=f"__**攻撃力：剣：-4%: {float(dmg * (osraw - 0.04)):.3f},"
                                                                 f" 弓：-4%: {float(dmg * (osraw - 0.04) * makon):.3f},"
                                                                 f" 魔法：-4%: {float(dmg * (osraw - 0.04)):.3f}**__\n\n"
                                                                 f"**聖剣 (Boss : {float(dmg * (osraw - 0.04) * 1.07):.3f} / "
                                                                 f"Mob : {float(dmg * (osraw - 0.04) * 0.70):.3f})\n"
                                                                 f"魔混系武器 : {float(dmg * (osraw - 0.04) * 1.70):.3f}**",
                          inline=False)

    embed_3_job.add_field(name='\U000025b6\U0000fe0fドラゴンキラー',
                          value=f"__**攻撃力：剣：-2%: {float(dmg * (osraw - 0.02)):.3f}, "
                                f" 弓：+5%: {float(dmg * (osraw + 0.05) * makon):.3f},"
                                f" 魔法：-2%: {float(dmg * (osraw - 0.02)):.3f}**__\n\n"
                                f"**聖剣 (Boss : {float(dmg * (osraw - 0.02) * 1.07):.3f} / "
                                f"Mob : {float(dmg * (osraw - 0.02) * 0.70):.3f})\n"
                                f"魔混系武器 : {float(dmg * (osraw + 0.05) * 1.70):.3f}**",
                          inline=False)

    embed_3_job.add_field(name='\U000025b6\U0000fe0fプリースト', value=f"__**攻撃力：剣：-10%: {float(dmg * (osraw - 0.10)):.3f},"
                                                                  f" 弓：-10%: {float(dmg * (osraw - 0.10) * makon):.3f},"
                                                                  f" 魔法：-10%: {float(dmg * (osraw - 0.10)):.3f}**__\n\n"
                                                                  f"**聖剣 (Boss : {float(dmg * (osraw - 0.10) * 1.07):.3f} / "
                                                                  f"Mob : {float(dmg * (osraw - 0.10) * 0.70):.3f})\n"
                                                                  f"魔混系武器 : {float(dmg * (osraw - 0.10) * 1.70):.3f}**",
                          inline=False)

    embed_3_job.add_field(name='\U000025b6\U0000fe0fスカーミッシャー',
                          value=f"__**攻撃力：剣：+5%: {float(dmg * (osraw + 0.05)):.3f},"
                                f" 弓：{float(dmg * osraw * makon):.3f},"
                                f" 魔法：{float(dmg * osraw):.3f}**__\n\n"
                                f"**聖剣 (Boss : {float(dmg * (osraw + 0.05) * 1.07):.3f} / "
                                f"Mob : {float(dmg * osraw * 0.70):.3f})\n"
                                f"魔混系武器 : {float(dmg * osraw * 1.70):.3f}**",
                          inline=False)

    embed_3_job.set_footer(text='Page 3 of 5')

    embed_4_job = discord.Embed(title='職業', color=discord.Color.dark_green(),
                                url='https://wikiwiki.jp/thelow/%E8%81%B7%E6%A5%AD')

    embed_4_job.set_author(name=f"By {ctx.author}")
    embed_4_job.add_field(name='条件', value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n'
                                           f'魔法石倍率： {alpha}倍')

    embed_4_job.add_field(name='\U000025b6\U0000fe0fハグレモノ', value=f"__**攻撃力：剣：-7%: {float(dmg * (osraw - 0.07)):.3f},"
                                                                  f" 弓：-7%: {float(dmg * (osraw - 0.07) * makon):.3f},"
                                                                  f" 魔法：-7%: {float(dmg * (osraw - 0.07)):.3f}**__\n\n"
                                                                  f"**聖剣 (Boss : {float(dmg * (osraw - 0.07) * 1.07):.3f} / "
                                                                  f"Mob : {float(dmg * (osraw - 0.07) * 0.70):.3f})\n"
                                                                  f"魔混系武器 : {float(dmg * (osraw - 0.07) * 1.70):.3f}**",
                          inline=False)

    embed_4_job.add_field(name='\U000025b6\U0000fe0fルーンキャスター',
                          value=f"__**攻撃力：剣：-7%: {float(dmg * (osraw - 0.07)):.3f},"
                                f" 弓：-7%: {float(dmg * (osraw - 0.07) * makon):.3f},"
                                f" 魔法：+7%: {float(dmg * (osraw + 0.07)):.3f}**__\n\n"
                                f"**聖剣 (Boss : {float(dmg * (osraw - 0.07) * 1.07):.3f} / "
                                f"Mob : {float(dmg * (osraw - 0.07) * 0.70):.3f})\n"
                                f"魔混系武器 : {float(dmg * (osraw - 0.07) * 1.70):.3f}**",
                          inline=False)

    embed_4_job.add_field(name='\U000025b6\U0000fe0fスペランカー', value=f"__**攻撃力：剣：+10%: {float(dmg * (osraw + 0.10)):.3f},"
                                                                   f"  弓：+10%: {float(dmg * (osraw + 0.10) * makon):.3f},"
                                                                   f" 魔法：+10%: {float(dmg * (osraw + 0.10)):.3f}**__\n\n"
                                                                   f"**聖剣 (Boss : {float(dmg * (osraw + 0.10) * 1.07):.3f} / "
                                                                   f"Mob : {float(dmg * (osraw + 0.10) * 0.70):.3f})\n"
                                                                   f"魔混系武器 : {float(dmg * (osraw + 0.10) * 1.70):.3f}**",
                          inline=False)

    embed_4_job.add_field(name='\U000025b6\U0000fe0fアーサー', value=f"__**攻撃力：剣：+5%: {float(dmg * (osraw + 0.05)):.3f},"
                                                                 f" 弓: -5%：{float(dmg * (osraw - 0.05) * makon):.3f},"
                                                                 f" 魔法: +5%：{float(dmg * (osraw + 0.05)):.3f}**__\n\n"
                                                                 f"**聖剣 (Boss : {float(dmg * (osraw + 0.05) * 1.07):.3f} / "
                                                                 f"Mob : {float(dmg * (osraw + 0.05) * 0.70):.3f})\n"
                                                                 f"魔混系武器 : {float(dmg * osraw * 1.70):.3f}**",
                          inline=False)

    embed_4_job.add_field(name='\U000025b6\U0000fe0fシーカー', value=f"__**攻撃力：剣：-4%: {float(dmg * (osraw - 0.04)):.3f},"
                                                                 f" 弓：+5%: {float(dmg * (osraw + 0.05) * makon):.3f},"
                                                                 f" 魔法：-4%: {float(dmg * (osraw - 0.04)):.3f}**__\n\n"
                                                                 f"**聖剣 (Boss : {float(dmg * (osraw - 0.04) * 1.07):.3f} / "
                                                                 f"Mob : {float(dmg * (osraw - 0.04) * 0.70):.3f})\n"
                                                                 f"魔混系武器 : {float(dmg * (osraw + 0.05) * 1.70):.3f}**",
                          inline=False)

    embed_4_job.set_footer(text='Page 4 of 5')

    embed_5_job = discord.Embed(title='職業',
                                description='[2022年 2月 アップデート分](https://docs.google.com/document/d/1Xu8K0KvgjzsxZPcI-zzpXovgHduu_1AbfwcZ2e1-i6M/edit?usp=sharing)',
                                color=discord.Color.dark_green(),
                                url='https://wikiwiki.jp/thelow/%E8%81%B7%E6%A5%AD')
    embed_5_job.set_author(name=f"By {ctx.author}")
    embed_5_job.add_field(name='条件', value=f'素火力： {raw}\nOS： {os}\nOS倍率： {osraw}\n魔法石： {r}\n'
                                           f'魔法石倍率： {alpha}倍')

    embed_5_job.add_field(name='\U000025b6\U0000fe0fスカルピアサー：聖剣用職業',
                          value=f"__**攻撃力: 剣： {float(dmg * osraw):.3f}, / ゾンビ: -10% {float(dmg * osraw * 0.90):.3f}\n"
                                f" 弓: {float(dmg * osraw * makon):.3f}, / ゾンビ: -10%: {float(dmg * osraw * 0.90):.3f}\n"
                                f" 魔法: {float(dmg * osraw):.3f}, / ゾンビ: {float(dmg * (osraw * 0.90)):.3f}**__\n\n"
                                f"**聖剣 (Boss : {float(dmg * osraw * 1.30):.3f} (ゾンビ: {float(dmg * osraw * 0.90 * 1.30):.3f}) /\n"
                                f"Mob : {float(dmg * osraw * 0.70):.3f} (ゾンビ: {float(dmg * osraw * 0.90 * 0.70):.3f}))\n"
                                f"魔混系武器 : {float(dmg * osraw * 1.70):.3f} (ゾンビ: {float(dmg * (osraw - 0.10) * 1.70):.3f})**",
                          inline=False)

    embed_5_job.add_field(name='\U000025b6\U0000fe0fバタフライシーカー：エターナルペンデュラム用職業',
                          value=f"__**攻撃力: 剣：-7%: {float(dmg * (osraw - 0.07)):.3f}\n"
                                f" 弓：+10%: {float(dmg * (osraw + 0.10) * makon):.3f}\n"
                                f" 魔法: -7%: {float(dmg * (osraw - 0.07)):.3f}**__\n\n"
                                f"**聖剣 (Boss : {float(dmg * osraw * 1.07):.3f} / "
                                f"Mob : {float(dmg * osraw * 0.70):.3f})\n"
                                f"魔混系武器 : {float(dmg * osraw * 1.70):.3f}**",
                          inline=False)
    #####################################################################################################################################
    embed_5_job.add_field(name='\U000025b6\U0000fe0fアレイスター: 魔混用職業',
                          value=f"__**攻撃力: 剣：-5%: {float(dmg * (osraw - 0.05)):.3f}\n"
                                f" 弓: {float(dmg * osraw * makon):.3f}\n"
                                f" 魔法: {float(dmg * osraw):.3f}**__\n\n"
                                f"**聖剣 (Boss : {float(dmg * osraw * 1.07):.3f} /\n"
                                f"Mob : {float(dmg * osraw * 0.70):.3f})\n"
                                f"魔混系武器 : {float(dmg * osraw * 1.70):.3f}**",
                          inline=False)

    embed_5_job.add_field(name='\U000025b6\U0000fe0fダークブラスター：冥剣、アムル用職業\n アムル : Boss +10.0% / 冥剣&トワ剣　+30.0％ / スケ -10.0%',
                          value=f"__**攻撃力: 剣： {float(dmg * osraw):.3f}, / スケ: -10%: {float(dmg * osraw * 0.90):.3f}\n"
                                f" 弓: {float(dmg * osraw * makon):.3f}, / スケ: -10%: {float(dmg * osraw * 0.90):.3f}\n"
                                f" 魔法: {float(dmg * osraw):.3f}, / スケ: -10%: {float(dmg * osraw * 0.90):.3f}**__\n\n"
                                f"**聖剣: (Boss : {float(dmg * osraw * 1.07):.3f} (スケ: {float(dmg * osraw * 0.90 * 1.07):.3f}) /\n"
                                f"Mob : {float(dmg * osraw * 0.70):.3f} (スケ: {float(dmg * osraw * 0.90 * 0.70):.3f}))**\n"
                                f"**魔混系武器 : {float(dmg * osraw * 1.70):.3f} (スケ: {float(dmg * osraw * 0.90 * 1.70):.3f})\n\n"
                                f"アムルダート: Boss : {float(dmg * osraw * 1.1):.3f} (スケ: {float(dmg * osraw * 0.90):.3f}) /\n"
                                f"Mob: {float(dmg * osraw):.3f} (スケ: {float(dmg * osraw * 0.90):.3f})\n\n"
                                f"冥剣&トワ剣: (Boss : {float(dmg * osraw * 1.30):.3f} (スケ: {float(dmg * osraw * 0.90 * 1.30):.3f}) /\n"
                                f"Mob : {float(dmg * osraw * 0.70):.3f} (スケ: {float(dmg * osraw * 0.90 * 0.70):.3f}))**",
                          inline=False)

    embed_5_job.set_footer(text='Page 5 of 5')

    return [
        embed_1_job,
        embed_2_job,
        embed_3_job,
        embed_4_job,
        embed_5_job
    ]
