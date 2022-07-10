import discord
from discord.ext import commands

from . import osdict, embed_skill, tokkoulist


class SkillDamageAdditional(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot_check = bot

    @commands.command(name='adskill')
    async def skillalpha(self, ctx: commands.Context, raw: float, raw_add: float, os: int, *args):
        osval = osdict[os]
        dmg, alpha = await tokkoulist(ctx=ctx, dmg=raw + raw_add, os_power=1.0, tokkou=list(args))
        sp_dmg, sp_alpha = await tokkoulist(ctx=ctx, dmg=raw, os_power=1.0, tokkou=list(args))
        embeds = embed_skill(ctx=ctx, raw=raw, dmg=dmg, sp_dmg=sp_dmg, os=os, osval=osval, stone_list=list(args), stone_val=alpha)
        await ctx.send(embed=embeds[16])


def setup(bot: commands.Bot):
    bot.add_cog(SkillDamageAdditional(bot=bot))
