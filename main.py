import datetime
import sys
import traceback
from os import getenv

import discord
import pytz
from aiohttp import ClientConnectorError
from discord import errors
from discord.ext import commands
from dotenv import load_dotenv

log_id = 934697584960888862

load_dotenv()

INITIAL_EXTENTIONS: list[str] = [
    # 'slash_add_damage',
    'CommandGames',
    'CommandHelp',
    'CommandJobStatus',
    'CommandTag',
    'Damage',
    'DamageAsk',
    'DamageCoolTime',
    'DamageJob',
    'DamageSkill',
    'DamageSkillSimple',
    'DiscordEventAction',
    'MessageExpand',
    'SlashDamage',
    'SlashDamageAlpha',
    'SlashDamageAsk',
    'SlashDamageCoolTime',
    'SlashDamageJob',
    'SlashDamageSkill'
]


class Main(commands.Bot):
    def __init__(
            self,
            command_prefix,
            intents,
            help_command,
            **kwargs
    ) -> None:
        super().__init__(
            command_prefix=command_prefix,
            intents=intents or discord.Intents.all(),
            help_command=help_command or None,
            **kwargs
        )
        self.lo = self.un = 0

    async def on_ready(self):
        """
        Returns
        -------

        """
        for cog in INITIAL_EXTENTIONS:
            try:
                self.load_extension('cogs.{}'.format(cog), package=None)
                self.lo += 1
                # await self.get_channel(950607627660967946).send(f'{cog} loaded!')
            except errors.ExtensionError as e:
                print(traceback.TracebackException.from_exception(e))
                self.un += 1

        print(f'Logged in {self.user.id} : {self.user.name}')
        print(discord.__version__)
        print("lo: {}, un {}".format(self.lo, self.un))
        time = datetime.datetime.now(pytz.timezone('Asia/Tokyo'))
        print(time)

        try:
            await self.get_channel(950607627660967946).send(f"{time.hour}時 {time.minute}分 {time.second}秒\nre-start!")
            await self.get_channel(log_id).send("**----------------------------------**")
        except AttributeError as s:
            print("AttributeError")

        except:
            pass

        if len(self.users) >= 100:
            await self.change_presence(
                activity=discord.Game(
                    name=f'{self.command_prefix}help | {len(self.users)} 人が {self.user.name}'
                )
            )


if __name__ == '__main__':
    intents = discord.Intents.all()
    bot: commands.Bot = Main(
        command_prefix='.',
        intents=intents,
        help_command=None
    )
    try:
        bot.run(getenv('TOKEN'))

    except (discord.LoginFailure, ClientConnectorError) as s:
        print(s)
