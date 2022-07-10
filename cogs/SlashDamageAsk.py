import discord
from discord import Option
from discord.ext import commands

from . import guild_ids
from .definition import tokkou
from .dictionary import osdict

magicstonelist = ['1', '2', '3', '4', '4_5', '5', 'legend']


class SlashAskDamage(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name='ask', guild_ids=guild_ids, description='目的のダメージを出すには・・')
    async def ask_damage(
            self,
            ctx: discord.ApplicationContext,
            need: Option(float, description='欲しい火力'),
            raw: Option(float, description='素ダメ', required=False),
            os: Option(int, description='OS値', required=False),
            slot1: Option(str, description='スロット1', choices=magicstonelist, required=False),
            slot2: Option(str, description='スロット2', choices=magicstonelist, required=False),
            slot3: Option(str, description='スロット3', choices=magicstonelist, required=False),
            slot4: Option(str, description='スロット4', choices=magicstonelist, required=False),
            slot5: Option(str, description='スロット5', choices=magicstonelist, required=False)
    ):
        global sent_message
        if os is raw is None:
            await ctx.respond(f'どちらか1方は埋めてください', ephemeral=True)
            return

        if os is not None and raw is not None:
            await ctx.respond('どちらか1方のみ埋めてください', ephemeral=True)
            return

        r = list()
        x = [slot1, slot2, slot3, slot4, slot5]

        if os is not None:
            if os >= len(osdict):
                await ctx.respond(f'OSは{len(osdict)}までしか登録されていません。')
                return

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

            osval = osdict[os]
            dmg, alpha = await tokkou(ctx=ctx, raw=1.0, osraw=osval, x=x)
            times = need / dmg
            print(f"{need} {raw} {times}")
            await ctx.respond(
                f'欲しい火力: {need}\nOS値: {os}\nOS倍率: {osval}\n魔法石: {r}\n魔法石倍率: {alpha}\n\n**__必要な攻撃力: {times:.3f}__**')

        if raw is not None:
            osval = osdict[0]
            dmg, alpha = await tokkou(ctx, raw, osval, x)
            times = need / dmg

            for i in range(len(osdict)):
                if osdict[i] > times:
                    await ctx.respond(
                        f'欲しい火力: {need}\n攻撃力: {raw}\n魔法石: {r}\n魔法石倍率: {alpha}\n\n**__必要なOS: {i}__**  (OS倍率: {osdict[i]})')
                    break

                if times >= osdict[74]:
                    await ctx.respond(
                        f'欲しい火力: {need}\n攻撃力: {raw}\n魔法石: {r}\n魔法石倍率: {alpha}\n\n**この攻撃力では求める火力を出すことは不可能です。**')
                    break


def setup(bot: commands.Bot):
    bot.add_cog(SlashAskDamage(bot))
