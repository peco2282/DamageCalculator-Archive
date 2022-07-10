import asyncio

import discord
from discord import Option
from discord.ext import commands

from .definition import tokkou
from .dictionary import osdict
from .embeds import embed_list_skill
from . import guild_ids

magicstonelist = ['1', '2', '3', '4', '4_5', '5', 'legend']


class SlashSkillDamage(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name='skill', guild_ids=guild_ids, description='スキル使用時のダメージ計算をします。')
    async def skilldamage(
            self,
            ctx: discord.ApplicationContext,
            raw: Option(float, description='素ダメ'),
            os: Option(int, description='OS値', required=False),
            slot1: Option(str, description='スロット1', choices=magicstonelist, required=False),
            slot2: Option(str, description='スロット2', choices=magicstonelist, required=False),
            slot3: Option(str, description='スロット3', choices=magicstonelist, required=False),
            slot4: Option(str, description='スロット4', choices=magicstonelist, required=False),
            slot5: Option(str, description='スロット5', choices=magicstonelist, required=False)
    ) -> None:
        global sent_message
        if os is None:
            os = 0

        if os >= len(osdict):
            await ctx.respond(f'OSは{len(osdict)}までしか登録されていません。')
            return

        r = list()
        r_cp = list()
        osval = osdict[os]
        x = [slot1, slot2, slot3, slot4, slot5]
        for i in x:
            if i in r:
                if i is None:
                    pass

                else:
                    await ctx.respond("error\n\n数値が重複しています。重複したものは1つとしてカウントします。", ephemeral=True)
                    pass

            if i is None:
                pass

            else:
                r.append(i)

            await ctx.respond(
                f'\U0001f1e6 :  ノービス\n'
                f'\U0001f1e7 : ソルジャー , \U0001f1e8 : アーチャー , \U0001f1e9 : マジシャン\n'
                f'\U0001f1ea : ウォーリア , \U0001f1eb : ボウマン , 　\U0001f1ec : メイジ \n\n'
                f'\U0001f1ed : ロウニン , 　　　　\U0001f1ee : ドラゴンキラー , \U0001f1ef : プリースト\n'
                f'\U0001f1f0 : スカ―ミッシャー , \U0001f1f1 : ハグレモノ , 　　\U0001f1f2 : ルーンキャスター\n'
                f'\U0001f1f3 : スペランカー , 　　\U0001f1f4 : アーサー , 　　　\U0001f1f5 : シーカー', ephemeral=True)

            dmg, alpha = await tokkou(ctx=ctx, raw=raw, osraw=1.0, x=x)

            embed_lists = await embed_list_skill(ctx=ctx, dmg=dmg, raw=raw, os=os, osraw=osval, r=r, alpha=alpha)

            sent_message = await ctx.send(embed=embed_lists[0])

            emoji_list: list[str] = [
                '\U0001f1e6', '\U0001f1e7', '\U0001f1e8', '\U0001f1e9',
                '\U0001f1ea', '\U0001f1eb', '\U0001f1ec', '\U0001f1ed',
                '\U0001f1ee', '\U0001f1ef', '\U0001f1f0', '\U0001f1f1',
                '\U0001f1f2', '\U0001f1f3', '\U0001f1f4', '\U0001f1f5'
            ]

            for j in emoji_list:
                await sent_message.add_reaction(emoji=j)

                # リアクションチェック用の関数
            def check(reaction: discord.Reaction, user: discord.User) -> bool:
                # botを呼び出した本人からのリアクションのみ受け付ける
                # reaction.message == msg を入れないと複数出したときに全て連動して動いてしまう
                return user == ctx.author and reaction.message == sent_message and str(
                    reaction.emoji) in emoji_list

            while True:
                try:
                    # リアクションが付けられるまで待機
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=60.0, check=check)

                except asyncio.TimeoutError:
                    # 一定時間経ったら消す
                    # for remove_emoji in emoji_list:
                    # await sent_message.remove_reaction(emoji=remove_emoji, member=bot.user)
                    await sent_message.clear_reactions()
                    break

                else:
                    if str(reaction.emoji) == emoji_list[0]:
                        await sent_message.edit(embed=embed_lists[0])

                    if str(reaction.emoji) == emoji_list[1]:
                        await sent_message.edit(embed=embed_lists[1])

                    if str(reaction.emoji) == emoji_list[2]:
                        await sent_message.edit(embed=embed_lists[2])

                    if str(reaction.emoji) == emoji_list[3]:
                        await sent_message.edit(embed=embed_lists[3])

                    if str(reaction.emoji) == emoji_list[4]:
                        await sent_message.edit(embed=embed_lists[4])

                    if str(reaction.emoji) == emoji_list[5]:
                        await sent_message.edit(embed=embed_lists[5])

                    if str(reaction.emoji) == emoji_list[6]:
                        await sent_message.edit(embed=embed_lists[6])

                    if str(reaction.emoji) == emoji_list[7]:
                        await sent_message.edit(embed=embed_lists[7])

                    if str(reaction.emoji) == emoji_list[8]:
                        await sent_message.edit(embed=embed_lists[8])

                    if str(reaction.emoji) == emoji_list[9]:
                        await sent_message.edit(embed=embed_lists[9])

                    if str(reaction.emoji) == emoji_list[10]:
                        await sent_message.edit(embed=embed_lists[10])

                    if str(reaction.emoji) == emoji_list[11]:
                        await sent_message.edit(embed=embed_lists[11])

                    if str(reaction.emoji) == emoji_list[12]:
                        await sent_message.edit(embed=embed_lists[12])

                    if str(reaction.emoji) == emoji_list[13]:
                        await sent_message.edit(embed=embed_lists[13])

                    if str(reaction.emoji) == emoji_list[14]:
                        await sent_message.edit(embed=embed_lists[14])

                    if str(reaction.emoji) == emoji_list[15]:
                        await sent_message.edit(embed=embed_lists[15])

                    await sent_message.remove_reaction(emoji=reaction.emoji, member=ctx.author)


def setup(bot: commands.Bot):
    bot.add_cog(SlashSkillDamage(bot))
