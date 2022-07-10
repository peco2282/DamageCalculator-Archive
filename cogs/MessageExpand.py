import re

from discord import Message, Embed, Guild
from discord.ext import commands

regex_discord_message_url = (
    '(?!<)https://(ptb.|canary.)?discord(app)?.com/channels/'
    '(?P<guild>[0-9]{18})/(?P<channel>[0-9]{18})/(?P<message>[0-9]{18})(?!>)'
)
regex_extra_url = (
    r'\?base_aid=(?P<base_author_id>[0-9]{18})'
    '&aid=(?P<author_id>[0-9]{18})'
    '&extra=(?P<extra_messages>(|[0-9,]+))'
)


def compose_embed(message: Message) -> Embed:
    """It takes a message object and returns an embed object

    Parameters
    ----------
    message : Message
        Message - The message that was sent.

    Returns
    -------
        A discord.Embed object.
    """
    embed: Embed = Embed(
        description=message.content,
        timestamp=message.created_at,
        url=message.jump_url
    )\
        .set_author(
        name=message.author.name,
        # icon_url=message.author.avatar.url
    )\
        .set_footer(
        text=message.channel.name,
    )

    if message.attachments and message.attachments[0].proxy_url:
        embed.set_image(
            url=message.attachments[0].proxy_url
        )
    return embed


async def fetch_message_from_id(guild: Guild, channel_id: int, message_id: int) -> Message:
    """It fetches a message from a channel given the channel id and the message id

    Parameters
    ----------
    guild : int
        The guild object that the message is in.
    channel_id : int
        The ID of the channel where the message is located.
    message_id : int
        The ID of the message you want to fetch.

    Returns
    -------
        A Message object.

    """
    message = await guild.get_channel(channel_id).fetch_message(message_id)
    return message


async def extract_message(bot: commands.Bot, message: Message) -> list[Message]:
    """It takes a message and extracts all the message ids from it

    Parameters
    ----------
    bot : commands.Bot
    message : Message
        Message

    Returns
    -------
        A list of messages.
    """
    messages: list = []
    for ids in re.finditer(regex_discord_message_url, message.content):
        guild = bot.get_guild(int(ids['guild']))
        fetched_message = await fetch_message_from_id(
            guild=guild,
            channel_id=int(ids['channel']),
            message_id=int(ids['message']),
        )
        messages.append(fetched_message)
    return messages


async def expand(bot: commands.Bot, message: Message):
    """It takes a message object,
    extracts the content and attachments from it, and sends them to the channel

    Parameters
    ----------
    bot : commands.Bot
        Bot
    message : Message
        Message
    """
    messages = await extract_message(bot=bot, message=message)
    for msg in messages:
        sent_messages: list = []

        if msg.content or msg.attachments:
            sent_messages.append(
                await message.channel.send(embed=compose_embed(message=msg))
            )

        for attachment in msg.attachments[1:]:
            embed: Embed = Embed()\
                .set_image(
                url=attachment.proxy_url
            )
            sent_messages.append(await message.channel.send(embed=embed))

        for embed in msg.embeds:
            sent_messages.append(await message.channel.send(embed=embed))


class ExpandMessage(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message: Message):
        if message.author.bot:
            return
        await expand(bot=self.bot, message=message)


def setup(bot: commands.Bot):
    bot.add_cog(ExpandMessage(bot=bot))
