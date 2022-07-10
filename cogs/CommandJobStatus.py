import asyncio

import discord

from discord.ext import commands


class JobStatus(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='jobstatus', aliases=['js'])
    async def job_status(self, ctx: commands.Context):
        e_1 = discord.Embed(title='職業詳細', 
                            url='https://wikiwiki.jp/thelow/%E8%81%B7%E6%A5%AD', color=discord.Color.blurple()) \
            .add_field(name='\U0001f389ソルジャー',
                       value='剣: 60lv.~: +5.0% & hp -10.0\n'
                             '   ~59lv.: +10%\n\n'
                             '弓 & 魔法: -2.0%', inline=False)\
            .add_field(name='\U0001f389アーチャー',
                       value='弓: +5.0%\n\n'
                             '剣 & 魔法: -2.0%', inline=False)\
            .add_field(name='\U0001f389マジシャン',
                       value='魔法: +5.0%\n\n'
                             '剣 & 弓: -2.0%', inline=False)

        e_2 = discord.Embed(title='職業詳細', 
                            url='https://wikiwiki.jp/thelow/%E8%81%B7%E6%A5%AD', color=discord.Color.blurple())\
            .add_field(name='\U0001f389ウォーリア',
                       value='剣: 60lv.~: +10.0% & hp -24.0\n'
                             '   ~59lv.: +15.0%\n\n'
                             '弓 & 魔法: -5.0%\n\n'
                             '剣転生5回以上\n', inline=False)\
            .add_field(name='\U0001f389ボウマン',
                       value='弓: +10.0%\n\n'
                             '剣 & 魔法: -5.0%\n\n'
                             '弓転生5回以上\n', inline=False)\
            .add_field(name='\U0001f389メイジ',
                       value='魔法: +10.0%\n\n'
                             '剣 & 弓: -5.0%\n\n'
                             '魔法転生5回以上\n', inline=False)

        e_3 = discord.Embed(title='職業詳細', 
                            url='https://wikiwiki.jp/thelow/%E8%81%B7%E6%A5%AD', color=discord.Color.blurple())\
            .add_field(name='\U0001f389ロウニン',
                       value='剣: -4.0%, 弓 -4.0%,  魔法 -4.0%,  最大体力 -15.0', inline=False)\
            .add_field(name='\U0001f389ドラゴンキラー',
                       value='	弓: +5.0% & Dorachenbogen・HässlichesBogenに龍の刻印を付与\n\n'
                             '	剣 & 魔法: -2.0%\n\n'
                             '総転生回数5回以上\nロウニンで「ドラゴンの谷」2回クリア\n', inline=False)\
            .add_field(name='\U0001f389プリースト',
                       value='最大MP +20.0,「恵みの泉」・「ホーリーブラッド」の効果が上昇する。\n\n'
                             '剣 & 弓 & 魔法: -10.0%,\n'
                             '周囲にプレイヤーがいると自身にデバフ\n'
                             '・他のプレイヤーが1人以上いる場合:弱体化3と移動速度低下3を付与\n'
                             '・他のプレイヤーが2人以上いる場合:追加で最大HPが30.0になる\n\n'
                             'ロウニンで「魔界:ココリ山」を2回クリア\n', inline=False)\
            .add_field(name='\U0001f389ハグレモノ',
                       value='剣 & 弓 & 魔法: -7.0%, 最大体力: -30.0, Food効果80%\n\n'
                             'ロウニンで「エイドリアン城」を1回クリア\n'
                             'ロウニンで「Clay Dangeon」を1回クリア\n', inline=False)\
            .add_field(name='\U0001f389スペランカー',
                       value='剣 & 弓 & 魔法: +10.0%, 落下・火のダメージ無効\n\n'
                             'hp が 1 に固定。防御力が0になる', inline=False)

        e_4 = discord.Embed(title='職業詳細', 
                            url='https://wikiwiki.jp/thelow/%E8%81%B7%E6%A5%AD', color=discord.Color.blurple())\
            .add_field(name='\U0001f389スカーミッッシャー',
                       value='剣: +5.0%, 最大体力: +4.0\n\n'
                             '最大MP: -6.0\n\n'
                             'ロウニンで「冥界」を2回クリア\n', inline=False)\
            .add_field(name='\U0001f389ルーンキャスター',
                       value='魔法: +7.0%, 最大MP: +20, Rune of Arcadiaにファイア・ボルケーノを付与\n\n'
                             '剣 & 弓: -7.0%\n\n'
                             'ハグレモノで「Lux et Tenebrae-光-」を2回クリア\n'
                             'ハグレモノで「追憶と創成の間」を2回クリア\n'
                             'ハグレモノで「輝煌の残滓」を2回クリア\n', inline=False)\
            .add_field(name='\U0001f389アーサー',
                       value='剣 & 魔法: +5.0%, 最大体力: +4.0, アーマーポイント: +5.0\n\n'
                             '弓: -5.0%, 最大MP: -6.0, 最大体力: +6.0\n\n'
                             'スぺランカーで「Estrada Of Cave」を2回クリア\n'
                             'スペランカーで「マリンディ鉱山」を2回クリア\n', inline=False)\
            .add_field(name='\U0001f389シーカー',
                       value='弓: +5.0%,矢の消費を10%で無効, 武器スキル「百花繚乱」発動時、敵がnodelayに\n\n'
                             '剣 & 魔法: -4.0%, 最大体力: -10.0\n\n'
                             'スペランカーで「Tower of Judgement」を1回クリア\n', inline=False)

        e_5 = discord.Embed(title='職業詳細', 
                            url='https://wikiwiki.jp/thelow/%E8%81%B7%E6%A5%AD', color=discord.Color.blurple()) \
            .add_field(name='\U0001f389アレイスター',
                       value='魔混消費量: -20.0% サテライトキャノンの魔混消費量を 5 個に\n\n'
                             '剣: -5.0%\n\n'
                             'ロウニンで「魔界:ヘルスラ」を1回クリア\n'
                             'ロウニンで「魔界:ココリ山」を1回クリア\n', inline=False) \
            .add_field(name='\U0001f389スカルピアサー',
                       value='聖剣使用時 ボス: +30.0%\n\n'
                             'ゾンビに対して: -10.0%\n\n'
                             'ロウニンで「浮世の砂海」を2回クリア\n', inline=False) \
            .add_field(name='\U0001f389ダークブラスター',
                       value='アムルダート使用時 ボス: +10.0%, 冥剣使用時 ボス: +30.0%\n\n'
                             'スケルトンに対して: +10.0%\n\n'
                             'ルーンキャスターで「冥界」を1回クリア\n', inline=False) \
            .add_field(name='\U0001f389バタフライシーカー',
                       value='弓の攻撃力: +10.0% 最大MP: +20.0\n\n'
                             '剣 & 魔法: -7.0% アーマーポイント: -40.0% 最大体力: -60.0\n\n'
                             'シーカーで「Last Judgement」を1回クリア\n', inline=False)

        e_list = [e_1, e_2, e_3, e_4, e_5]
        page = 0
        sent_message = await ctx.send(embed=e_1.set_footer(text=f'page {page + 1} of {len(e_list) + 1}'))

        def check(reaction: discord.Reaction, user: discord.User):
            return user == ctx.author and reaction.message == sent_message and str(reaction.emoji) in ('\U000023ea', '\U000023e9')
        for i in '\u23ea', '\u23e9':
            await sent_message.add_reaction(i)

        while True:
            try:
                reaction, user = await self.bot.wait_for(event='reaction_add', timeout=20, check=check)

            except asyncio.TimeoutError:
                await sent_message.clear_reactions()
                break

            else:
                if str(reaction.emoji) == '\u23ea':
                    page = (page - 1) % len(e_list)
                    await sent_message.edit(embed=e_list[page].set_footer(text=f'page {page + 1} of {len(e_list) + 1}'))

                if str(reaction.emoji) == '\u23e9':
                    page = (page + 1) % len(e_list)
                    await sent_message.edit(embed=e_list[page].set_footer(text=f'page {page + 1} of {len(e_list) + 1}'))

                await sent_message.remove_reaction(emoji=reaction.emoji, member=ctx.author)


def setup(bot: commands.Bot):
    bot.add_cog(JobStatus(bot=bot))
