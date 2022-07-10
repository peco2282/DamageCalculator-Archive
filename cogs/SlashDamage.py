import asyncio

import discord
from discord import Option
from discord.ui import Button, View
from discord.ext import commands

from .definition import tokkou
from .dictionary import osdict
from . import guild_ids

magicstonelist = ['1', '2', '3', '4', '4_5', '5', 'legend']


class SlashDamage(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name='dmg', guild_ids=guild_ids, description='ダメージ計算')
    async def damage(
            self,
            ctx: discord.ApplicationContext,
            raw: Option(float, description='素ダメ'),
            add_dmg: Option(float, description='mobに対する特殊ダメージ', required=False),
            os: Option(int, description='OS値', required=False),
            slot1: Option(str, description='スロット1', choices=magicstonelist, required=False),
            slot2: Option(str, description='スロット2', choices=magicstonelist, required=False),
            slot3: Option(str, description='スロット3', choices=magicstonelist, required=False),
            slot4: Option(str, description='スロット4', choices=magicstonelist, required=False),
            slot5: Option(str, description='スロット5', choices=magicstonelist, required=False)
    ):

        r = list()
        x = [slot1, slot2, slot3, slot4, slot5]
        if os is None:
            os = 0

        seiken_button = Button(label='浮世の聖剣', style=discord.ButtonStyle.red, custom_id='聖剣')
        makon_button = Button(label='魔混系武器', style=discord.ButtonStyle.green, custom_id='魔混')
        view = View(timeout=30)
        view.add_item(seiken_button)
        view.add_item(makon_button)

        def check(user: discord.Interaction):
            return user.user == ctx.author and user.message == sent_message

        for i in x:
            if i in r:
                if i is None:
                    pass
                else:
                    await ctx.respond('ERROR!\n\n数値が重複しています。重複したものは1つとしてカウントします。', ephemeral=True)
            if i is None:
                pass

            else:
                r.append(i)

        osval = osdict[os]

        if add_dmg is None:
            add_dmg = 0

        dmg, alpha = await tokkou(ctx=ctx, raw=raw + add_dmg, osraw=osval, x=x)
        if len(r) == 0:
            r = 'なし'

        else:
            r = ', '.join(r)
        sent_message = await ctx.respond(f'**By {ctx.author.name}**\n\n'
                                         f'素火力 : {raw}\n'
                                         f'OS値 : {os}\n'
                                         f'OS倍率 : {osval} 倍\n'
                                         f'魔法石 : {r}\n'
                                         f'魔法石倍率 : {alpha:.3f}\n\n'
                                         f'**__最終的な攻撃力 : {dmg:.3f}__**', view=view)

        def check(interaction: discord.Interaction):
            print(f'送信　{sent_message.id}\n\n{interaction.message}\n\n{interaction}')
            return interaction.user == ctx.author

        while True:
            try:
                user_check: discord.Interaction = await self.bot.wait_for('interaction', check=check, timeout=20)

            except asyncio.TimeoutError:
                view.clear_items()
                break

            else:
                if user_check.data['custom_id'] == '聖剣':
                    await sent_message.edit_original_message(content=f'**By {ctx.author.name}**\n\n'
                                                                     f'素火力 : {raw}\n'
                                                                     f'OS値 : {os}\n'
                                                                     f'OS倍率 : {osval} 倍\n'
                                                                     f'魔法石 : {r}\n'
                                                                     f'魔法石倍率 : {alpha:.3f}\n\n'
                                                                     f'**__最終的な攻撃力 : {dmg:.3f}__**\n\n'
                                                                     f'__**BOSS : {dmg * 1.2:.3f}    MOB : {dmg * 0.7:.3f}**__',
                                                             view=view)

                if user_check.data['custom_id'] == '魔混':
                    await sent_message.edit_original_message(content=f'**By {ctx.author.name}**\n\n'
                                                                     f'素火力 : {raw}\n'
                                                                     f'OS値 : {os}\n'
                                                                     f'OS倍率 : {osval} 倍\n'
                                                                     f'魔法石 : {r}\n'
                                                                     f'魔法石倍率 : {alpha:.3f}\n\n'
                                                                     f'**__最終的な攻撃力 : {dmg:.3f}__**\n\n'
                                                                     f"__**魔混使用時 : {dmg * 1.7:.3f}**__", view=view)


def setup(bot: commands.Bot):
    bot.add_cog(SlashDamage(bot))
