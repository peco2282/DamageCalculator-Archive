# import discord
from discord.ext import commands

from .dictionary import castimedict
from .definition import ctcalc, command_log


class CoolTime(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='cas', aliases=['ct'])
    async def cooltime(self, ctx: commands.Context, raw: float, perk: int = 0, *args: str):
        args = list(set(args) & {'1', '2', '3', '4', '4_5', '5'})
        if len(args) == 0:
            args = 'なし'
        args_cp = args.copy()
        print(f'{args} {args_cp}')
        finalct, a = await ctcalc(ctx=ctx, raw=raw, perkraw=castimedict[perk], x=args)
        strings = f'元のCT: {raw}\nパーク値: {perk}\nパークで減少する割合: {castimedict[perk]}\n魔法石: {args_cp}\n魔法石倍率: {a}\n\n**最終的なCT: {finalct: .3f}**'

        if raw == 220:
            strings += '\n恵みの泉は効果時間(20s)を含めて実際のctとなります。よって最速泉は36+20秒です。'
        sent_message = await ctx.send(strings)
        await command_log(ctx=ctx, bot=self.bot, message=sent_message)

    @cooltime.error
    async def cooltime_error(self, ctx: commands.Context, *args):
        if len(args[1:]) <= 0:
            sent_message = await ctx.send(f'**{ctx.author.name}**\n`{self.bot.command_prefix}ct [素のCT] (Quick Talk Spell の値, ない場合 0 となります) (魔法石)`')

        else:
            sent_message = await ctx.send(f'**{ctx.author.name}**\n必要事項が記入されていません。')

        await command_log(ctx=ctx, bot=self.bot, message=sent_message)


def setup(bot: commands.Bot):
    bot.add_cog(CoolTime(bot=bot))
