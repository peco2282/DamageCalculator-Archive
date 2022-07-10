import asyncio

import discord
from discord import Option
from discord.ext import commands
from discord.ui import View, Button

from . import guild_ids
from .dictionary import osdict
from .definition import tokkou

mob_list = [
    'ゾンビ',
    'スケルトン',
    'アンデッド',
    '生物',
    'ゴーレム'
]
magicstonelist = ['1', '2', '3', '4', '4_5', '5', 'legend']


class AddDamage(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(
        name='additionaldmg',
        description='追加mobダメージを含めた値を計算します。',
        guild_ids=guild_ids
    )
    async def additional_damage(
            self,
            ctx: discord.ApplicationContext,
            raw: Option(float, description='素ダメ'),
            add: Option(float, description='mobに対する特殊ダメージ'),
            os: Option(int, description='OSPerk', required=False),
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

        if len(r) == 0:
            r = 'なし'

        dmg, alpha = await tokkou(ctx=ctx, raw=raw, osraw=osval, x=x)
        add_dmg, add_alpha = await tokkou(ctx=ctx, raw=raw + add, osraw=osval, x=x)
        sent_message = await ctx.respond(f'**By {ctx.author.name}**\n\n'
                                         f'素火力 : {raw}\n'
                                         f'OS値 : {os}\n'
                                         f'OS倍率 : {osval} 倍\n'
                                         f'魔法石 : {r}\n'
                                         f'魔法石倍率 : {alpha:.3f}\n\n'
                                         f'**__最終的な攻撃力 : {dmg:.3f}__**', view=view)

        while True:
            try:
                user_check: discord.Interaction = await self.bot.wait_for('interaction', check=check, timeout=100)

            except asyncio.TimeoutError:
                view.clear_items()
                break

            else:
                if user_check.data['custom_id'] == '聖剣':
                    await ctx.respond(dmg+add)
                    await sent_message.edit_original_message()


def setup(bot: commands.Bot):
    bot.add_cog(AddDamage(bot=bot))
