import discord
from discord.ext import commands

from .definition import tokkoulist, command_log, error_log
from .dictionary import osdict


class AskDamage(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='ask')
    async def ask_damage(self, ctx: commands.Context, want_dmg: float, raw_dmg: str, os: str, *args: str):
        print(f'{ctx}\n{want_dmg}\n{type(raw_dmg)}\n{type(os)}\n{args}')
        global sent_message
        if len(args) == 0:
            args = '魔法石なし'

        if os.isdigit() and raw_dmg.isdigit():
            await ctx.send('どちらか一方を `?` で埋めてください。')
            return
        '''
        if os.isdigit() is raw_dmg.isdigit() is False or os is raw_dmg == '?':
            await ctx.send('どちらか一方のみを `?` で埋めてください。')
            return
        '''
        args = list(set(args) & {'1', '2', '3', '4', '4_5', '5', 'leg'})
        if raw_dmg.isdigit() and os == '?':  # os不明
            osval = osdict[0]
            raw_dmg = float(raw_dmg)
            dmg, alpha = await tokkoulist(ctx=ctx, dmg=raw_dmg, os_power=osval, tokkou=args)
            times = want_dmg / dmg
            for i in osdict:
                if times < osdict[0]:
                    sent_message = await ctx.send('OSを積む必要はありません。')
                    break

                if times <= osdict[i]:
                    # sent_message = await ctx.send(f"{raw_dmg}で{want_dmg}を出すには\n__**OSは{i}以上**__とってください。")
                    sent_message = await ctx.send(f"欲しい火力 : {want_dmg}\n魔法石 : {args}\n魔法石倍率 : {alpha:.3f}\n{raw_dmg}で{want_dmg}を出すには\n__**OSは{i}以上 (倍率 : {osdict[i]})**__とってください。")
                    break

                if times > osdict[len(osdict) - 1]:
                    sent_message = await ctx.send(f"OSが{len(osdict)}以上必要、又は不可能な値です。")
                    break

        elif os.isdigit() and raw_dmg == '?':  # 素ダメ不明
            os = int(os)
            if os >= len(osdict):
                await ctx.send(f'OSは{len(osdict)}までしか登録されていません。')
                return

            osval = osdict[os]
            dmg, alpha = await tokkoulist(ctx=ctx, dmg=1.0, os_power=osval, tokkou=args)
            times = want_dmg / dmg
            sent_message = await ctx.send(
                f'欲しい火力: {want_dmg}\nOS値: {os}\nOS倍率: {osval}\n魔法石: {args}\n魔法石倍率: {alpha}\n\n**__必要な攻撃力: {times:.3f}__**')

        else:
            await ctx.send(f'{self.bot.command_prefix}ask [目的のダメージ] [素ダメ] (魔法石)  又は\n/ask [目的のダメージ] [OS] (魔法石)')
        await command_log(ctx=ctx, bot=self.bot, message=sent_message)


def setup(bot: commands.Bot):
    bot.add_cog(AskDamage(bot=bot))
