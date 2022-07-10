import re

from discord.ext import commands
from motor import motor_asyncio as motor
import discord

from . import mongo_url, command_log, error_log

dbclient = motor.AsyncIOMotorClient(mongo_url)
db = dbclient['DamageCalcutator']
db_tag = db['user_tags']
regex_discord_message_url = (
    '(?!<)https://(ptb.|canary.)?discord(app)?.com/channels/'
    '(?P<guild>[0-9]{18})/(?P<channel>[0-9]{18})/(?P<message>[0-9]{18})(?!>)'
)


class Tag(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.group(name='tag', invoke_without_command=True)
    async def message_tags_group(self, ctx: commands.Context):
        embed = discord.Embed(title='tag の使い方')
        embed.add_field(name=f'{self.bot.command_prefix}tag add', value='リプライ元を指定してtagを追加します。', inline=False)
        embed.add_field(name=f'{self.bot.command_prefix}tag show', value='ユーザーidを指定するとその人のtagが、指定しない場合は自分のtagが表示されます。', inline=False)
        embed.add_field(name=f'{self.bot.command_prefix}tag delete (番号)', value='1 ~ 10の指定したtagが削除されます。指定しない場合は1番目が削除対象です。', inline=False)
        embed.add_field(name=f'{self.bot.command_prefix}tag reset', value='自分のtagがすべてリセットされます。', inline=False)
        await ctx.send(embed=embed)
        await command_log(ctx=ctx, bot=self.bot, message=ctx.message)

    @message_tags_group.command(name='add')
    async def message_tags_add(self, ctx: commands.Context):
        global message_url_list
        try:
            message_url = ctx.channel.get_partial_message(ctx.message.reference.message_id).jump_url

            result = await db_tag.find_one(
                {
                    'user_id': ctx.author.id
                }
            )
            if result is None:
                await ctx.send('過去の tag が見つからなかったので新規追加します。')
                message_url_list = [message_url]
                await db_tag.insert_one(
                    {
                        'user_id': ctx.author.id,
                        'message_url': message_url_list
                    }
                )

            if result:
                message_url_list = result['message_url']
                if len(message_url_list) >= 10:
                    return await ctx.send('tag の数が10個を超えました。\n`tag del (番号)`1つ削除するか`tag reset` をして tag をリセットしてください。')
                await ctx.send('tag を追加します。')
                message_url_list.append(message_url)
                await db_tag.replace_one({
                        '_id': result['_id']
                    }, {
                        'user_id': ctx.author.id,
                        'message_url': message_url_list
                    }
                )
            await ctx.send('設定が完了しました。')

        except AttributeError:
            await ctx.send('リプライ元を指定してください。')
        finally:
            await command_log(ctx=ctx, bot=self.bot, message=ctx.message)

    @message_tags_group.command(name='show')
    async def message_tags_show(self, ctx: commands.Context, user_id: str = None):
        global command, message, content
        if user_id is None:
            user_id = str(ctx.author.id)

        if not user_id.isdigit():
            return await ctx.send('ユーザーidを数値で入力してください。')

        if self.bot.get_user(int(user_id)) is None:
            return await ctx.send(f'{user_id} は存在しませんでした。')

        data = await db_tag.find_one(
            {
                'user_id': int(user_id)
            }, {
                '_id': False
            }
        )
        if data is None:
            return await ctx.send(f'{user_id} のtag は見つかりませんでした。')
        
        embed = discord.Embed(title=f'{self.bot.get_user(int(user_id)).name} の tag 一覧')
        get_tag_url = data['message_url']
        if get_tag_url is None:
            return await ctx.send('tag が見つかりませんでした。')
        for num, url in enumerate(get_tag_url, 1):
            for ids in re.finditer(regex_discord_message_url, url):
                message = await self.bot.get_guild(
                    int(ids['guild'])
                ).get_channel(
                    int(ids['channel'])
                ).fetch_message(
                    int(ids['message'])
                )
                if message.embeds:
                    content = f'[Embed]({url})'
                    command = ''
                elif message.content.startswith(self.bot.command_prefix):
                    command = 'command: ' + message.content.split()[0].lstrip(self.bot.command_prefix)
                    content = f'[{message.content}]({url})'

                else:
                    command = ''
                    content = f'[{message.content}]({url})'

            embed.add_field(name=f'{num} {command}', value=content, inline=False)
        await ctx.send(embed=embed)
        await command_log(ctx=ctx, bot=self.bot, message=ctx.message)

    @message_tags_group.command(name='delete', aliases=['del'])
    async def message_tags_delete(self, ctx: commands.Context, pos: str = '1'):
        if pos.isdigit():
            return await ctx.send(f'数値で削除したいtagを指定してください。すべて削除する場合は {self.bot.command_prefix}tag reset をしてください。')

        result = await db_tag.find_one(
            {
                'user_id': ctx.author.id
            }
        )
        if result is None:
            return await ctx.send(f'tag が見つかりませんでした。')

        message_url: list = result['message_url']
        print(message_url)
        try:
            message_url.pop(int(pos) - 1)
            await ctx.send('remove complete')

        except (IndexError, KeyError) as e:
            print(e)
        print(message_url)
        await db_tag.replace_one(
            {
                '_id': result['_id']
            }, {
                'user_id': ctx.author.id,
                'message_url': message_url
            }
        )
        await command_log(ctx=ctx, bot=self.bot, message=ctx.message)

    @message_tags_group.command(name='reset', aliases=['clear'])
    async def message_tags_reset(self, ctx: commands.Context, user_id: str = None):
        if user_id is None:
            user_id = str(ctx.author.id)
        if not user_id.isdigit():
            return await ctx.send('miss')
        if user_id and int(ctx.author.id) != 378486322039357441:
            user_id = ctx.author.id
        result = await db_tag.delete_one(
            {
                'user_id': int(user_id)
            }
        )
        await ctx.send('reset complete')
        await command_log(ctx=ctx, bot=self.bot, message=ctx.message)

    @message_tags_group.error
    async def tag_error(self, ctx: commands.Context, error):
        await error_log(ctx=ctx, bot=self.bot, error=error)


def setup(bot: commands.Bot): bot.add_cog(Tag(bot=bot))
