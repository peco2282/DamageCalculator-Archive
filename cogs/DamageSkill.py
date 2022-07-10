import asyncio

import discord
from discord.ext import commands

from .embeds import embed_skill
from .definition import tokkoulist, command_log, error_log
from .dictionary import osdict, emoji_1, emoji_2, emoji_3, emoji_4, emoji_5, emoji_6, emoji_7, emoji_8, emoji_9

emoji_list = [emoji_1, emoji_2, emoji_3, emoji_4, emoji_5, emoji_6, emoji_7, emoji_8, emoji_9]

job1 = [f'{emoji_1}ノービス', f'{emoji_2}ソルジャー', f'{emoji_3}アーチャー', f'\n{emoji_4}マジシャン', f'{emoji_5}ウォーリア', f'{emoji_6}ボウマン', f'\n{emoji_7}メイジ']
job2 = [f'{emoji_1}ロウニン', f'{emoji_2}ドラゴンキラー', f'{emoji_3}プリースト', f'\n{emoji_4}スカーミッシャー', f'{emoji_5}ハグレモノ', f'{emoji_6}ルーンキャスター', f'\n{emoji_7}スペランカー', f'{emoji_8}アーサー', f'{emoji_9}シーカー']
job3 = [f'{emoji_1}スカルピアサー', f'{emoji_2}バタフライシーカー', f'{emoji_3}アレイスター', f'\n{emoji_4}ダークブラスター 1', f'{emoji_5}ダークブラスター 2']


class SkillDamage(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='skill1')
    async def skill_damage_1(self, ctx: commands.Context, raw: float, os: int = 0, *args: str):
        args = list(set(args) & {'1', '2', '3', '4', '4_5', '4.5', '5', 'leg'})
        if len(args) == 0:
            args = 'なし'

        if os > len(osdict):
            await ctx.send(f'OS: {len(osdict)}以上は登録されていません。osを0として計算します')
            osval = 1.0

        else:
            osval = osdict[os]

        raw_add = 0

        dmg, alpha = await tokkoulist(ctx=ctx, dmg=raw + raw_add, os_power=1.0, tokkou=list(args))
        # sp_dmg, sp_alpha = await tokkoulist(ctx=ctx, dmg=raw, os_power=1.0, tokkou=list(args))
        embeds = embed_skill(ctx=ctx, raw=raw, dmg=dmg, sp_dmg=dmg, os=os, osval=osval, stone_list=list(args), stone_val=alpha)

        # dmg, alpha = await tokkoulist(ctx=ctx, dmg=raw_dmg, os_power=1.0, tokkou=args)
        # embed_lists = await embed_list_skill(ctx=ctx, dmg=dmg, raw=raw_dmg, os=os, osraw=osval, r=args, alpha=alpha)
        sent_message = await ctx.send(', '.join(job1), embed=embeds[0])
        await command_log(ctx=ctx, bot=self.bot, message=sent_message)

        for i in range(7):
            await sent_message.add_reaction(emoji_list[i])

        def check(reaction: discord.Reaction, user: discord.User):
            return user == ctx.author and reaction.message == sent_message and str(reaction.emoji) in emoji_list

        while True:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=20, check=check)

            except asyncio.TimeoutError:
                await sent_message.clear_reactions()

            else:
                if str(reaction.emoji) == emoji_list[0]:
                    await sent_message.edit(embed=embeds[0])

                if str(reaction.emoji) == emoji_list[1]:
                    await sent_message.edit(embed=embeds[1])

                if str(reaction.emoji) == emoji_list[2]:
                    await sent_message.edit(embed=embeds[2])

                if str(reaction.emoji) == emoji_list[3]:
                    await sent_message.edit(embed=embeds[3])

                if str(reaction.emoji) == emoji_list[4]:
                    await sent_message.edit(embed=embeds[4])

                if str(reaction.emoji) == emoji_list[5]:
                    await sent_message.edit(embed=embeds[5])

                if str(reaction.emoji) == emoji_list[6]:
                    await sent_message.edit(embed=embeds[6])

                await sent_message.remove_reaction(emoji=reaction.emoji, member=ctx.author)

    @commands.command(name='skill2')
    async def skill_damage_2(self, ctx: commands.Context, raw: float, os: int = 0, *args: str):
        args = list(set(args) & {'1', '2', '3', '4', '4_5', '4.5', '5', 'leg'})
        if len(args) == 0:
            args = 'なし'

        if os > len(osdict):
            await ctx.send(f'OS: {len(osdict)}以上は登録されていません。osを0として計算します')
            osval = 1.0

        else:
            osval = osdict[os]

        raw_add = 0

        dmg, alpha = await tokkoulist(ctx=ctx, dmg=raw + raw_add, os_power=1.0, tokkou=list(args))
        sp_dmg, sp_alpha = await tokkoulist(ctx=ctx, dmg=raw, os_power=1.0, tokkou=list(args))
        embeds = embed_skill(ctx=ctx, raw=raw, dmg=dmg, sp_dmg=sp_dmg, os=os, osval=osval, stone_list=list(args), stone_val=alpha)

        # dmg, alpha = await tokkoulist(ctx=ctx, dmg=raw_dmg, os_power=1.0, tokkou=args)
        # embed_lists = await embed_list_skill(ctx=ctx, dmg=dmg, raw=raw_dmg, os=os, osraw=osval, r=args, alpha=alpha)
        # print(f'{dmg} {alpha} {embed_lists[0]}')
        sent_message = await ctx.send(', '.join(job2), embed=embeds[7])
        await command_log(ctx=ctx, bot=self.bot, message=sent_message)

        for i in range(8):
            await sent_message.add_reaction(emoji_list[i])

        def check(reaction: discord.Reaction, user: discord.User):
            return user == ctx.author and reaction.message == sent_message and str(reaction.emoji) in emoji_list

        while True:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=20, check=check)

            except asyncio.TimeoutError:
                await sent_message.clear_reactions()

            else:
                if str(reaction.emoji) == emoji_list[0]:
                    await sent_message.edit(embed=embeds[7])

                if str(reaction.emoji) == emoji_list[1]:
                    await sent_message.edit(embed=embeds[8])

                if str(reaction.emoji) == emoji_list[2]:
                    await sent_message.edit(embed=embeds[9])

                if str(reaction.emoji) == emoji_list[3]:
                    await sent_message.edit(embed=embeds[10])

                if str(reaction.emoji) == emoji_list[4]:
                    await sent_message.edit(embed=embeds[11])

                if str(reaction.emoji) == emoji_list[5]:
                    await sent_message.edit(embed=embeds[12])

                if str(reaction.emoji) == emoji_list[6]:
                    await sent_message.edit(embed=embeds[13])

                if str(reaction.emoji) == emoji_list[7]:
                    await sent_message.edit(embed=embeds[14])

                if str(reaction.emoji) == emoji_list[8]:
                    await sent_message.edit(embed=embeds[15])

                await sent_message.remove_reaction(emoji=reaction.emoji, member=ctx.author)

    @commands.command(name='skill3')
    async def skill_damage_3(self, ctx: commands.Context, raw: float, os: int = 0, *args: str):
        args = list(set(args) & {'1', '2', '3', '4', '4_5', '4.5', '5', 'leg'})
        if len(args) == 0:
            args = 'なし'

        if os > len(osdict):
            await ctx.send(f'OS: {len(osdict)}以上は登録されていません。osを0として計算します')
            osval = 1.0

        else:
            osval = osdict[os]

        raw_add = 0

        dmg, alpha = await tokkoulist(ctx=ctx, dmg=raw + raw_add, os_power=1.0, tokkou=list(args))
        sp_dmg, sp_alpha = await tokkoulist(ctx=ctx, dmg=raw, os_power=1.0, tokkou=list(args))
        embeds = embed_skill(ctx=ctx, raw=raw, dmg=dmg, sp_dmg=sp_dmg, os=os, osval=osval, stone_list=list(args), stone_val=alpha)

        # dmg, alpha = await tokkoulist(ctx=ctx, dmg=raw_dmg, os_power=1.0, tokkou=args)
        # embed_lists = await embed_list_skill(ctx=ctx, dmg=dmg, raw=raw_dmg, os=os, osraw=osval, r=args, alpha=alpha)
        # print(f'{dmg} {alpha} {embed_lists[0]}')
        sent_message = await ctx.send(', '.join(job3), embed=embeds[16])
        await command_log(ctx=ctx, bot=self.bot, message=sent_message)

        for i in range(5):
            await sent_message.add_reaction(emoji_list[i])

        def check(reaction: discord.Reaction, user: discord.User):
            return user == ctx.author and reaction.message == sent_message and str(reaction.emoji) in emoji_list

        while True:
            try:
                reaction, user = await self.bot.wait_for('reaction_add', timeout=20, check=check)

            except asyncio.TimeoutError:
                await sent_message.clear_reactions()

            else:
                if str(reaction.emoji) == emoji_list[0]:
                    await sent_message.edit(embed=embeds[16])

                if str(reaction.emoji) == emoji_list[1]:
                    await sent_message.edit(embed=embeds[17])

                if str(reaction.emoji) == emoji_list[2]:
                    await sent_message.edit(embed=embeds[18])

                if str(reaction.emoji) == emoji_list[3]:
                    await sent_message.edit(embed=embeds[19])

                if str(reaction.emoji) == emoji_list[4]:
                    await sent_message.edit(embed=embeds[20])

                await sent_message.remove_reaction(emoji=reaction.emoji, member=ctx.author)

    @skill_damage_1.error
    @skill_damage_2.error
    @skill_damage_3.error
    async def skill_error(self, ctx: commands.Context, error):
        print(error)
        await error_log(bot=self.bot, ctx=ctx, error=error)


def setup(bot: commands.Bot):
    bot.add_cog(SkillDamage(bot=bot))
