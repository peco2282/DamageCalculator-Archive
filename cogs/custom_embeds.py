import discord
from discord.ext import commands

url = "https://wikiwiki.jp/thelow/%E3%82%B9%E3%82%AD%E3%83%AB"


def custom_embed_skill(
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
    e_01 = discord.Embed(title='skill 一覧', url=url, description='**職業：ノービス**', colour=discord.Colour.brand_green())
    e_02 = discord.Embed(title='skill 一覧', url=url, description='**職業：ソルジャー**', colour=discord.Colour.brand_green())
    e_03 = discord.Embed(title='skill 一覧', url=url, description='**職業：アーチャー**', colour=discord.Colour.brand_green())
    e_04 = discord.Embed(title='skill 一覧', url=url, description='**職業：マジシャン**', colour=discord.Colour.brand_green())

    e_05 = discord.Embed(title='skill 一覧', url=url, description='**職業：ウォーリア**', colour=discord.Colour.brand_green())
    e_06 = discord.Embed(title='skill 一覧', url=url, description='**職業：ボウマン**', colour=discord.Colour.brand_green())
    e_07 = discord.Embed(title='skill 一覧', url=url, description='**職業：メイジ**', colour=discord.Colour.brand_green())

    e_08 = discord.Embed(title='skill 一覧', url=url, description='**職業：ロウニン**', colour=discord.Colour.brand_green())
    e_09 = discord.Embed(title='skill 一覧', url=url, description='**職業：ドラゴンキラー**', colour=discord.Colour.brand_green())
    e_10 = discord.Embed(title='skill 一覧', url=url, description='**職業：プリースト**', colour=discord.Colour.brand_green())
    e_11 = discord.Embed(title='skill 一覧', url=url, description='**職業：スカーミッシャー**', colour=discord.Colour.brand_green())

    e_12 = discord.Embed(title='skill 一覧', url=url, description='**職業：ハグレモノ**', colour=discord.Colour.brand_green())
    e_13 = discord.Embed(title='skill 一覧', url=url, description='**職業：ルーンキャスター**', colour=discord.Colour.brand_green())
    e_14 = discord.Embed(title='skill 一覧', url=url, description='**職業：スペランカー**', colour=discord.Colour.brand_green())
    e_15 = discord.Embed(title='skill 一覧', url=url, description='**職業：アーサー**', colour=discord.Colour.brand_green())
    e_16 = discord.Embed(title='skill 一覧', url=url, description='**職業：シーカー**', colour=discord.Colour.brand_green())

    e_17 = discord.Embed(title='skill 一覧', url=url, description='**職業：スカルピアサー**', colour=discord.Colour.brand_green())
    e_18 = discord.Embed(title='skill 一覧', url=url, description='**職業：バタフライシーカー**', colour=discord.Colour.brand_green())
    e_19 = discord.Embed(title='skill 一覧', url=url, description='**職業：アレイスター**', colour=discord.Colour.brand_green())
    e_20 = discord.Embed(title='skill 一覧', url=url, description='**職業：ダークブラスター 1**', colour=discord.Colour.brand_green())
    e_21 = discord.Embed(title='skill 一覧', url=url, description='**職業：ダークブラスター 2**', colour=discord.Colour.brand_green())

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
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * osval:.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * osval:.3f}__**', inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * osval:.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * osval:.3f}__**', inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * osval:.3f}__**', inline=False) \
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
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osval + 0.05):.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osval + 0.05):.3f}__**', inline=False) \
        .add_field(name=f'***-神弓- ブリザードテンスト*** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * (osval - 0.02):.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * (osval - 0.02):.3f}__**', inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osval + 0.05):.3f}__**', inline=False) \
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
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osval - 0.02):.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osval - 0.02):.3f}__**', inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * (osval + 0.05):.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * (osval + 0.05):.3f}__**', inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osval - 0.02):.3f}__**', inline=False) \
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
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osval - 0.02):.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osval - 0.02):.3f}__**', inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * (osval - 0.02):.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * (osval - 0.02):.3f}__**', inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osval - 0.02):.3f}__**', inline=False) \
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
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osval + 0.10):.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osval + 0.10):.3f}__**', inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * (osval - 0.05):.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * (osval - 0.05):.3f}__**', inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osval + 0.10):.3f}__**', inline=False) \
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
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osval - 0.05):.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osval - 0.05):.3f}__**', inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * (osval + 0.10):.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * (osval + 0.10):.3f}__**', inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osval - 0.05):.3f}__**', inline=False) \
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
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osval - 0.05):.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osval - 0.05):.3f}__**', inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * (osval - 0.05):.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * (osval - 0.05):.3f}__**', inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osval - 0.05):.3f}__**', inline=False) \
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
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osval - 0.04):.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osval - 0.04):.3f}__**', inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * (osval - 0.04):.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * (osval - 0.04):.3f}__**', inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osval - 0.04):.3f}__**', inline=False) \
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
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osval - 0.02):.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osval - 0.02):.3f}__**', inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * (osval + 0.05):.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * (osval + 0.05):.3f}__**', inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osval - 0.02):.3f}__**', inline=False) \
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
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osval - 0.10):.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osval - 0.10):.3f}__**', inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * (osval - 0.10):.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * (osval - 0.10):.3f}__**', inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osval - 0.10):.3f}__**', inline=False) \
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
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osval + 0.05):.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osval + 0.05):.3f}__**', inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * osval:.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * osval:.3f}__**', inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osval + 0.05):.3f}__**', inline=False) \
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
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osval - 0.07):.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osval - 0.07):.3f}__**', inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * (osval - 0.07):.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * (osval - 0.07):.3f}__**', inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osval - 0.07):.3f}__**', inline=False) \
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
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osval - 0.07):.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osval - 0.07):.3f}__**', inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * (osval - 0.07):.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * (osval - 0.07):.3f}__**', inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osval - 0.07):.3f}__**', inline=False) \
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
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osval + 0.10):.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osval + 0.10):.3f}__**', inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * (osval + 0.10):.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * (osval + 0.10):.3f}__**', inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osval + 0.10):.3f}__**', inline=False) \
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
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osval + 0.05):.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osval + 0.05):.3f}__**', inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * (osval - 0.05):.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * (osval - 0.05):.3f}__**', inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osval + 0.05):.3f}__**', inline=False) \
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
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osval - 0.04):.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osval - 0.04):.3f}__**', inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * (osval + 0.10):.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * (osval + 0.10):.3f}__**', inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osval - 0.04):.3f}__**', inline=False) \
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
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * osval:.3f},  ゾンビ: {dmg * 7 * osval * 0.90:.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * osval:.3f},  ゾンビ: {dmg * 4 * osval * 0.90:.3f}__**',
                   inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * osval:.3f},  ゾンビ: {sp_dmg * 1.1 * 7 * osval * 0.90:.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * osval:.3f},  ゾンビ: {sp_dmg * 4 * osval * 0.90:.3f}__**',
                   inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * osval:.3f},  ゾンビ: {dmg * 2.5 * osval * 0.90:.3f}__**',
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
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osval - 0.07):.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osval - 0.07):.3f}__**', inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * (osval + 0.10):.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * (osval + 0.10):.3f}__**', inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osval - 0.07):.3f}__**', inline=False) \
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
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * (osval - 0.05):.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * (osval - 0.05):.3f}__**', inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * osval:.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * osval:.3f}__**', inline=False) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * (osval - 0.05):.3f}__**', inline=False) \
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
        .add_field(name=f'**Angel_auf_Erden (In エイドリアン城)**',
                   value=f'ショックストーン (スペシャル)：**__{dmg * 7 * osval:.3f},  スケルトン: {sp_dmg * 7 * osval * 0.90:.3f}__**'
                         f'\nトゥルーロック (ノーマル)：**__{dmg * 4 * osval:.3f},  スケルトン: {sp_dmg * 4 * osval * 0.90:.3f}__**',
                   inline=False) \
        .add_field(name=f'**-神弓- ブリザードテンスト** (In Vaaasa)',
                   value=f'カオスブリザード (7発命中時、総和) (スペシャル)：**__{sp_dmg * 1.1 * 7 * osval:.3f},  スケルトン: {sp_dmg * 1.1 * 7 * osval * 0.90:.3f}__**'
                         f'\n雪柱 (ノーマル)：**__{sp_dmg * 4 * osval:.3f},  スケルトン: {sp_dmg * 4 * osval * 0.90:.3f}__**',
                   inline=False) \

    e_21.set_author(name=ctx.author.name) \
        .add_field(name=f'**Satans Bote (ストーリー報酬) (In エイドリアン城)**',
                   value=f'血の斬撃 (スペシャル)：**__{dmg * 2.5 * osval:.3f},  スケルトン: {dmg * 2.5 * osval * 0.90:.3f}__**',
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
