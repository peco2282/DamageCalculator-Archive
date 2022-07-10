import asyncio
from typing import List, Any, Union

import discord
from discord import Option
from discord.ext import commands

from .definition import tokkou
from .dictionary import osdict, emoji_1, emoji_2, emoji_3, emoji_4
from . import guild_ids
from .embeds import embeds_list_job

magicstonelist = ['1', '2', '3', '4', '4_5', '5', 'legend']


class SlashJob(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name='job', guild_ids=guild_ids, description='職業ごとのダメージを算出')
    async def job_damage(
            self,
            ctx: discord.ApplicationContext,
            raw: Option(float, description='素ダメ'),
            os: Option(int, description='OS値', required=False),
            slot1: Option(str, description='スロット1', choices=magicstonelist, required=False),
            slot2: Option(str, description='スロット2', choices=magicstonelist, required=False),
            slot3: Option(str, description='スロット3', choices=magicstonelist, required=False),
            slot4: Option(str, description='スロット4', choices=magicstonelist, required=False),
            slot5: Option(str, description='スロット5', choices=magicstonelist, required=False)
    ):
        if os is None:
            os = 0

        if os >= len(osdict):
            await ctx.respond(f'OSは{len(osdict)}までしか登録されていません。')

        else:
            r = list()
            r_cp = list()
            x: list[Any] = [slot1, slot2, slot3, slot4, slot5]
            osval: Union[float, Any] = osdict[os]

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

            emojis: list[str] = [emoji_1, emoji_2, emoji_3, emoji_4]
            alpha: float
            dmg: float
            dmg, alpha = await tokkou(ctx=ctx, raw=raw, osraw=1.0, x=x)
            embedlist = await embeds_list_job(ctx=ctx, dmg=dmg, raw=raw, os=os, osraw=osval, alpha=alpha, r=r)
            await ctx.respond(f'**{emoji_1} : ソルジャー, アーチャー, マジシャン\n\n'
                              f'{emoji_2} : ウォーリ, ボウマン, メイジ\n\n'
                              f'{emoji_3} : ロウニン , ドラゴンキラー, プリースト, スカーミッシャー\n\n'
                              f'{emoji_4} : ハグレモノ, ルーンキャスター, スペランカー, アーサー, シーカー**', ephemeral=True)

            sent_message: discord.Message = await ctx.send(embed=embedlist[0])
            for i in emojis:
                await sent_message.add_reaction(i)

            def check(reaction: discord.Reaction, user: discord.User) -> bool:
                return user == ctx.author and reaction.message == sent_message and str(reaction.emoji) in emojis

            while True:
                try:
                    # リアクションが付けられるまで待機
                    reaction: discord.Reaction
                    user: discord.User
                    reaction, user = await self.bot.wait_for('reaction_add', timeout=20.0, check=check)

                except asyncio.TimeoutError:
                    # 一定時間経ったら消す
                    # for remove_emoji in emoji_list:
                    # await sent_message.remove_reaction(emoji=remove_emoji, member=bot.user)
                    await sent_message.clear_reactions()
                    break

                else:
                    if str(reaction.emoji) == emoji_1:
                        await sent_message.edit(embed=embedlist[0])

                    if str(reaction.emoji) == emoji_2:
                        await sent_message.edit(embed=embedlist[1])

                    if str(reaction.emoji) == emoji_3:
                        await sent_message.edit(embed=embedlist[2])

                    if str(reaction.emoji) == emoji_4:
                        await sent_message.edit(embed=embedlist[3])

                    await sent_message.remove_reaction(emoji=reaction.emoji, member=ctx.author)


def setup(bot: commands.Bot):
    bot.add_cog(SlashJob(bot))
