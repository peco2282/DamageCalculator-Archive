import discord
from discord import Option
from discord.ext import commands

from . import guild_ids
from .dictionary import castimedict
from .definition import ctcalc

casmagiclist = ['1', '2', '3', '4', '4_5', '5']
ctperk = [i for i in range(11)]


class SlashCoolTime(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name='ct', guild_ids=guild_ids, description='スキルcooltimeの計算')
    async def cooltime(
            self,
            ctx: discord.ApplicationContext,
            ct: Option(int, description='All Cool Time'),
            perk: Option(int, description='Quick Talk Spell の値', choices=ctperk),
            slot1: Option(str, description='スロット1', choices=casmagiclist, required=False),
            slot2: Option(str, description='スロット2', choices=casmagiclist, required=False),
            slot3: Option(str, description='スロット3', choices=casmagiclist, required=False),
            slot4: Option(str, description='スロット4', choices=casmagiclist, required=False),
            slot5: Option(str, description='スロット5', choices=casmagiclist, required=False)
    ):
        if perk >= len(castimedict):
            await ctx.respond(f'Perkは{len(castimedict)}までしか登録されていません。')
            return

        r = list()
        r_cp = list()
        x = [slot1, slot2, slot3, slot4, slot5]

        for i in x:
            if i in r:
                if i is None:
                    pass
                else:
                    await ctx.respond("error", ephemeral=True)
                    pass

            if i is None:
                pass

            else:
                r.append(i)
        if len(r) == 0:
            r = 'なし'

        finalct, a = await ctcalc(ctx, raw=ct, perkraw=castimedict[perk], x=x)
        strings = f'元のCT: {ct}\nパーク値: {perk}\nパークで減少する割合: {castimedict[perk]}\n魔法石: {r}\n魔法石倍率: {a}\n\n**最終的なCT: {finalct: .3f}**'

        if ct == 220:
            strings += '\n恵みの泉は効果時間(20s)を含めて実際のctとなります。よって最速泉は36+20秒です。'
        await ctx.respond(strings)


def setup(bot: commands.Bot):
    bot.add_cog(SlashCoolTime(bot=bot))
