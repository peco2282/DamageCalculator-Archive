import datetime
from typing import Optional, Tuple

import discord
from discord.ext import commands
import traceback

from . import log_id, log_msg_id
print(log_id)


async def error_log(ctx: Optional[commands.Context], bot: commands.Bot, error: Exception, errormsg: Optional[str] = None) -> discord.Message:
    errormsg = errormsg or 'Error content'
    embed = discord.Embed(title='Error log', url=ctx.message.jump_url, timestamp=datetime.datetime.now(), color=discord.Color.red())
    embed.add_field(name=errormsg, value=f'```bash\n{traceback.TracebackException.from_exception(error)}\n```')
    embed.set_author(name=f'Sended by {ctx.author.name if ctx is not None else bot.user.name}')
    try:
        msg = bot.get_message(991924099955830825)
        print(msg.content)
        msg_content = int(msg.content)
        await msg.edit(content=str(msg_content + 1))

    except:
        pass
    return await bot.get_channel(log_id).send(embed=embed)


async def command_log(ctx: commands.Context, bot: commands.Bot, message: discord.Message) -> discord.Message:
    embed = discord.Embed(title='log_url', description=f'Used: In {ctx.guild.name} / {ctx.channel.name}\nBy: {ctx.author.name}',
                          url=message.jump_url, timestamp=datetime.datetime.now(), color=discord.Color.green())
    embed.add_field(name=f'use `{ctx.command}` command', value=f'message content : \n`{ctx.message.content}`\n\nresponse message : \n```{message.content}```')
    embed.set_author(name=ctx.author.name)
    try:
        msg = bot.get_message(991924099955830825)
        print(msg.content)
        msg_content = int(msg.content)
        await msg.edit(content=str(msg_content + 1))

    except:
        pass
    return await bot.get_channel(log_id).send(embed=embed)


async def tokkou(ctx: discord.ApplicationContext, raw: float, osraw: float, x: list) -> Tuple[float, float]:  # x: 魔法石
    a = 1.0
    alpha = 0
    if len(x) == 0:
        d_all = raw * osraw
        return d_all, a

    if '4_5' in x and '5' in x:
        print("SSSS")
        await ctx.respond('`4_5` と `5` は同時に装着できません。魔法石を除いて計算します。', ephemeral=True)
        return raw * osraw, a

    elif '5' in x and 'legend' in x:
        print("XXXX")
        await ctx.respond('`5` と `LEGEND` は同時に装着できません。魔法石を除いて計算します。', ephemeral=True)
        return raw * osraw, a

    elif '4_5' in x and 'legend' in x:
        print("ZZZZ")
        await ctx.respond('`4_5` と `LEGEND` は同時に装着できません。魔法石を除いて計算します。', ephemeral=True)
        return raw * osraw, a

    else:
        if '4.5' in x:
            x.remove('4.5')
            x.append('4_5')

        if '1' in x:
            a *= 1.10
            x.remove('1')

        if '2' in x:
            a *= 1.15
            x.remove('2')

        if '3' in x:
            a *= 1.23
            x.remove('3')

        if '4' in x:
            a *= 1.35
            x.remove('4')

        if '4_5' in x:
            a *= 1.40
            x.remove('4_5')

        if '5' in x:
            a *= 1.55
            x.remove('5')

        if 'leg' in x:
            a *= 1.55
            alpha = raw * 0.06
            x.remove('leg')

        if 'legend' in x:
            a *= 1.55
            alpha = raw * 0.06
            x.remove('legend')

        alldmg = raw * osraw * a + alpha
        return alldmg, a


async def ctcalc(ctx: discord.ApplicationContext, raw: float, perkraw: float, x: list) -> Tuple[float, float]:
    a = 1.0
    if '4.5' in x:
        x.remove('4.5')
        x.append('4_5')

    if '1' in x:
        a *= 0.95
        x.remove('1')

    if '2' in x:
        a *= 0.90
        x.remove('2')

    if '3' in x:
        a *= 0.84
        x.remove('3')

    if '4' in x:
        a *= 0.77
        x.remove('4')

    if '4_5' in x:
        a *= 0.72
        x.remove('4_5')

    if '5' in x:
        a *= 0.60
        x.remove('5')

    ct = raw * perkraw * a
    return ct, a


async def tokkoulist(ctx: commands.Context, dmg: float, os_power: float, tokkou: list) -> Tuple[float, float]:
    """This function takes the damage,
    the opponent's power, and the list of tokkou and returns the list of tokkou that
    were not used

    Parameters
    ----------
    ctx : commands.Context
        The context of the command.
    dmg : float
        The damage of the attack.
    os_power : float
        The power of the OS.
    tokkou : list
        list of tokkou

    Returns
    -------
    alldmg : float
        The damage of all (include stones).
    tokkou_add : float
        The additional stone magnification.
    """
    global tokkou_add, alpha
    tokkou = list(tokkou)
    tokkou_list = list(tokkou)
    tokkou_add = 1.0
    alpha = 0
    if len(tokkou) == 0:
        dmg_all = dmg * os_power
        return dmg_all, tokkou_add

    if '4.5' in tokkou:
        tokkou.remove('4.5')
        tokkou.append('4_5')

    elif 1 <= len(tokkou) <= 5:
        if len(tokkou) != len(tokkou_list):
            await ctx.send(f"{ctx.author.mention}, 重複しています。")

        elif (str("4_5") in tokkou) and (str("5") in tokkou):
            await ctx.send(f"{ctx.author.mention}, 4_5と5は同時に装着できません")

        elif (str('4_5') in tokkou) and (str('leg') in tokkou):
            await ctx.send(f"{ctx.author.mention}, 4_5とLEGEND石は同時に装着できません")

        elif (str('leg') in tokkou) and (str('5') in tokkou):
            await ctx.send(f"{ctx.author.mention}, 5とLEGEND石は同時に装着できません")

        else:
            if str('1') in tokkou:
                tokkou_add *= 1.1
                tokkou.remove("1")

            if str('2') in tokkou:
                tokkou_add *= 1.15
                tokkou.remove("2")

            if str('3') in tokkou:
                tokkou_add *= 1.23
                tokkou.remove("3")

            if str('4') in tokkou:
                tokkou_add *= 1.35
                tokkou.remove('4')

            if str('4_5') in tokkou:
                tokkou_add *= 1.40
                tokkou.remove("4_5")

            if str('5') in tokkou:
                tokkou_add *= 1.55
                tokkou.remove("5")

            if str('leg') in tokkou:
                alpha = (dmg * 0.06)
                tokkou_add *= 1.55
                tokkou.remove("leg")

            print(f'{dmg} * {os_power} * {tokkou_add} + {alpha}')
            alldmg: float = dmg * os_power * tokkou_add + alpha
            print(alldmg)
            tokkou_add = round(tokkou_add, 4)
            return alldmg, tokkou_add
