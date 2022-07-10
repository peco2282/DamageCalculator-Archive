import asyncio

import discord
from discord.ui import Button, View
from discord.ext import commands

from .dictionary import osdict
from .definition import tokkoulist, command_log


class Damage(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    # noinspection PyUnboundLocalVariable
    @commands.command(name='dmg')
    async def damage(self, ctx: discord.ApplicationContext, raw: float, os: int = 0, *args: str):
        seiken_button = Button(label='浮世の聖剣', style=discord.ButtonStyle.red, custom_id='聖剣')
        makon_button = Button(label='魔混系武器', style=discord.ButtonStyle.green, custom_id='魔混')
        view = View(timeout=30)
        view.add_item(seiken_button)
        view.add_item(makon_button)

        def check(user: discord.Interaction):
            return user.user == ctx.author and user.message == sent_message

        print(f'{raw}  {os}  {args}')
        args = list(set(args) & {'1', '2', '3', '4', '4_5', '5', 'leg'})

        if os > len(osdict):
            await ctx.send(f'OS: {len(osdict)}以上は登録されていません。osを0として計算します')
            osval = 1.0

        else:
            osval = osdict[os]

        attack, tokkou = await tokkoulist(ctx=ctx, dmg=raw, os_power=osval, tokkou=args)

        if len(args) == 0:
            args = 'なし'

        else:
            args = ', '.join(args)
        r = f"**By：{ctx.author.name}**\n\n" \
            f"素火力 : {raw}\n" \
            f"OS値 : {os}\n" \
            f"OS倍率 : {osval} 倍\n" \
            f"魔法石：{args}\n" \
            f"魔法石倍率：{tokkou:.3f}倍\n" \
            f"__**最終的な攻撃力 : {attack:.3f}  (Critical: {attack * 1.15:.3f} )**__"
        sent_message = await ctx.send(r, view=view)
        await command_log(ctx=ctx, bot=self.bot, message=sent_message)

        while True:
            try:
                user_check: discord.Interaction = await self.bot.wait_for('interaction', check=check, timeout=20)

            except asyncio.TimeoutError:
                view.clear_items()
                await sent_message.edit(view=view)
                break

            else:
                if user_check.data['custom_id'] == '聖剣':
                    p = f"__**BOSS : {attack * 1.07:.3f}    MOB : {attack * 0.7:.3f}**__"

                if user_check.data['custom_id'] == '魔混':
                    p = f"__**魔混使用時 : {attack * 1.7:.3f}**__"

                s = f'{r}\n\n{p}'
                await sent_message.edit(content=s, view=view)
                view.stop()

    @damage.error
    async def damage_error(self, ctx: commands.Context, *args):
        if args is None:
            return
        print(len(args))
        print(args)
        if len(args[1:]) <= 0:
            print(ctx.message.content)

        sent_message = await ctx.send(f'**{ctx.author.name}** \n`{self.bot.command_prefix}dmg [素ダメージ] [os] (魔法石)`')
        await command_log(ctx=ctx, bot=self.bot, message=sent_message)


def setup(bot: commands.Bot):
    bot.add_cog(Damage(bot=bot))
