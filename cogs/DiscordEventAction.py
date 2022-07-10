import asyncio
import builtins
import datetime
import io
import re
import traceback

import discord
import sys
from discord.ext import commands
from . import log_id
from .definition import error_log


class Error(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_command_error(self, ctx: commands.Context, error: discord.errors):
        """It catches all errors that occur in the bot

        Parameters
        ----------
        ctx : commands.Context
            The context of where the message was sent
        error : discord.errors
            The error that was raised. This is always a discord.errors.DiscordException.

        """
        msg = None
        tpl = (
            f'{self.bot.command_prefix}ask',
            f'{self.bot.command_prefix}help',
            f'{self.bot.command_prefix}job',
            f'{self.bot.command_prefix}skill1',
            f'{self.bot.command_prefix}skill2',
            f'{self.bot.command_prefix}skill3',
            f'{self.bot.command_prefix}dmg',
            f'{self.bot.command_prefix}ct',
            f'{self.bot.command_prefix}cas'
        )
        if isinstance(error, commands.CommandNotFound):
            await ctx.send(f"This command not found! \n```\n{traceback.TracebackException.from_exception(error)}\n```")
            print(traceback.TracebackException.from_exception(error))

        elif isinstance(error, discord.HTTPException):
            try:
                await self.bot.get_channel(log_id).send(
                    f'HTTP Exeption {traceback.TracebackException.from_exception(error)} {error.code}')

            finally:
                print(traceback.TracebackException.from_exception(error))

        elif isinstance(error, builtins.ValueError):
            msg = 'Builtin error'
            await ctx.send(f'Builtin ValueError {traceback.TracebackException.from_exception(error)}')

        elif isinstance(error, discord.ext.commands.CommandInvokeError):
            await ctx.send(traceback.TracebackException.from_exception(error))

        elif isinstance(error, discord.InvalidArgument):
            await ctx.send(traceback.TracebackException.from_exception(error))
            await self.bot.get_channel(log_id).send(
                f'```bash\n{traceback.TracebackException.from_exception(error)}\n\n{error}```')

        elif isinstance(error, commands.CheckFailure):
            await ctx.send("このチャンネルではこのコマンドは使用できません。")

        elif ctx.message.content.startswith(tpl):
            await ctx.send('正しい引数を入力してください。')

        await error_log(ctx=ctx, bot=self.bot, error=error, errormsg=msg)

    @commands.Cog.listener()
    async def on_error(self, event, *args, **kwargs):
        print(f'{event}\n{args}\n{kwargs}')
        try:
            await self.bot.get_channel(log_id).send(f'```bash\n{sys.exc_info()}\n```')

        finally:
            pass

    @commands.command(name='ec')
    async def encoding(self, ctx: commands.Context, *, args: str):
        if ctx.channel.id in (886185192530780160, 931449554027544606, 926798315541114941, 944491200034005002):
            var = str(args.encode("unicode-escape"))[2:-1]
            print(var)
            var = re.sub(r"\\\\", r"\\", var)
            print(var)
            string = f'```\n' \
                     f'type=item\n' \
                     f'items=minecraft:アイテム名\n' \
                     f'texture=写真名.png\n' \
                     f'nbt.display.Name=ipattern:*{var}*' \
                     f'```'
            await ctx.send(string, file=discord.File(io.StringIO(string.replace("```", "")), filename=args + ".properties"))

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        try:
            if member.guild.id == 885757485871398985:
                if member.guild.get_role(949621722422857738):
                    await member.add_roles(member.guild.get_role(949621722422857738))
                    await self.bot.get_channel(885757485871398985).send(
                        embed=discord.Embed(title='メンバーの参加', description=f'user name: {member.name}\n ロール付与成功',
                                            timestamp=datetime.datetime.now()))

            if member.guild.id == 893402769254404117:
                print("$")
                await member.add_roles(member.guild.get_role(927184189076426862))

        except Exception as e:
            await error_log(ctx=None, bot=self.bot, error=str(e))
            pass

        else:
            await member.guild.system_channel.send(f'**{member.name}** が参加しました。')

    @commands.Cog.listener()
    async def on_member_remove(self, member: discord.Member):
        try:
            await member.guild.system_channel.send(f'{member.name} が脱退しました。')

        except:
            pass

    @commands.Cog.listener()
    async def on_guild_join(self, guild: discord.Guild):
        await self.bot.get_channel(log_id).send(
            f"{guild.id}: {guild.name} に参加。"
            f"<@!378486322039357441>"
        )

    @commands.command()
    async def roleadd(self, ctx: commands.Context):
        mems = ctx.guild.members
        for i in mems:
            if i.bot:
                return
            if i.get_role(949621722422857738) or i.get_role(927184189076426862):
                return
            await ctx.send(i)
            await asyncio.sleep(1)
            try:
                if ctx.guild.id == 885757485871398985:
                    if i.guild.get_role(949621722422857738):
                        await i.add_roles(i.guild.get_role(949621722422857738))
                        await self.bot.get_channel(885757485871398985).send(
                            embed=discord.Embed(title='メンバーの参加', description=f'user name: {i.name}\n ロール付与成功',
                                                timestamp=datetime.datetime.now()))

                if ctx.guild.id == 893402769254404117:
                    print("$")
                    await i.add_roles(i.guild.get_role(927184189076426862))

            except:
                pass


def setup(bot: commands.Bot):
    bot.add_cog(Error(bot))
