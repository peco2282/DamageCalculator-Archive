import discord
from discord.ext import commands
import asyncio

from .dictionary import osdict, emoji_1, emoji_2, emoji_3, emoji_4, emoji_5
from .definition import tokkoulist, command_log
from .embeds import embeds_list_job


class JobDamage(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='job')
    async def job_damage(self, ctx: commands.Context, raw: float, os: int = 0, *args: str):
        args: list = list(set(args) & {'1', '2', '3', '4', '4_5', '4.5', '5', 'leg'})
        if len(args) == 0:
            args = 'なし'

        if os >= len(osdict):
            await ctx.send(f'OS: {len(osdict)}以上は登録されていません。osを0として計算します')
            osval = 1.0

        else:
            osval = osdict[os]

        emojis = [emoji_1, emoji_2, emoji_3, emoji_4, emoji_5]
        attack, tokkou = await tokkoulist(ctx=ctx, dmg=raw, os_power=1.0, tokkou=args)
        embedlist = await embeds_list_job(ctx=ctx, dmg=attack, raw=raw, os=os, osraw=osval, alpha=tokkou, r=args)
        sent_message = await ctx.send(f'**{emoji_1} : ソルジャー, アーチャー, マジシャン\n'
                                      f'{emoji_2} : ウォーリ, ボウマン, メイジ\n'
                                      f'{emoji_3} : ロウニン , ドラゴンキラー, プリースト, スカーミッシャー\n'
                                      f'{emoji_4} : ハグレモノ, ルーンキャスター, スペランカー, アーサー, シーカー\n'
                                      f'{emoji_5} : スカルピアサー, バタフライシーカー, アレイスター, ダークブラスター**',
                                      embed=embedlist[0])
        await command_log(ctx=ctx, bot=self.bot, message=sent_message)

        for i in emojis:
            await sent_message.add_reaction(i)

        def check(reaction: discord.Reaction, user: discord.User):
            return user == ctx.author and reaction.message == sent_message and str(reaction.emoji) in emojis

        while True:
            try:
                # リアクションが付けられるまで待機
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

                if str(reaction.emoji) == emoji_5:
                    await sent_message.edit(embed=embedlist[4])

                await sent_message.remove_reaction(emoji=reaction.emoji, member=ctx.author)


def setup(bot: commands.Bot):
    bot.add_cog(JobDamage(bot))
