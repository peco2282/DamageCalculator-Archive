import discord
from discord import Interaction
from discord.ext import commands
from discord.ui import Select, View
from discord.components import SelectOption

from . import command_log, error_log
from . import guild_ids, channel_ids
from . import A, C, D, E, G, H, J, S, T


class Help(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name='help', guild_id=guild_ids, description='ヘルプの表示')
    async def slash_help(self, ctx: discord.ApplicationContext):
        embed = discord.Embed(title='help', color=discord.Color.green())
        embed.set_author(name=ctx.author.name)
        embed.add_field(name='help', value='/help この画面を表示します。', inline=False)
        embed.add_field(name='dmg', value='/dmg [素ダメ] (OS, ないときは 0 となります。) (魔法石)', inline=False)
        embed.add_field(name='job', value='/job [素ダメ] (OS, ないときは 0 となります。) (魔法石)', inline=False)
        embed.add_field(name='ct', value='/ct [そのままのCoolTime] [Quick Talk Spell Perk の値] (魔法石)', inline=False)
        embed.add_field(name='ask', value='/ask [目的のダメージ] [素ダメ] (魔法石)  又は\n/ask [目的のダメージ] [OS] (魔法石)', inline=False)
        embed.add_field(name='skill', value='/skill [素ダメ] (OS, ないときは 0 となります) (魔法石)', inline=False)
        await ctx.respond(embed=embed, ephemeral=True)

    # @commands.command(name='help')
    @commands.group(name='help', invoke_without_command=True)
    async def command_help(self, ctx: commands.Context, *, obj: str = None):
        channel_txt = list(f"#{self.bot.get_channel(ch_id).name}" for ch_id in channel_ids)
        embed = discord.Embed(title='help', color=discord.Color.green(), timestamp=ctx.message.created_at)
        embed.set_author(name=ctx.author.name, icon_url=ctx.author.avatar.url)
        embed.add_field(name="ヘルプ", value="下のドロップダウンメニューからコマンドを選んでください。\n\n"
                                          f'{self.bot.command_prefix}help この画面を表示します。\n'
                                          f'**<argument>**: 必須\n'
                                          f'**[argument]**: 選択\n'
                                          f'**[A|B]**: A 又は B', inline=False)
        """
        embed.add_field(name='help', value=f'{self.bot.command_prefix}help この画面を表示します。', inline=False)
        embed.add_field(name='dmg', value=f'{self.bot.command_prefix}dmg [素ダメ] (OS, ないときは 0 となります。) (魔法石)', inline=False)
        embed.add_field(name='job', value=f'{self.bot.command_prefix}job [素ダメ] (OS, ないときは 0 となります。) (魔法石)', inline=False)
        embed.add_field(name='ct', value=f'{self.bot.command_prefix}ct [そのままのCoolTime] [Quick Talk Spell Perk の値] (魔法石)', inline=False)
        embed.add_field(name='ask', value=f'{self.bot.command_prefix}ask [目的のダメージ] [素ダメ] (魔法石)  又は\n/ask [目的のダメージ] [OS] (魔法石)', inline=False)
        embed.add_field(name='skill', value=f'{self.bot.command_prefix}skill(1 ~ 3) [素ダメ] (OS, ないときは 0 となります) (魔法石)', inline=False)
        embed.add_field(name='sskill', value=f'{self.bot.command_prefix}__sskill(1-3)__ [素ダメ] (OS, ないときは 0 となります) (魔法石)\n***[alias: {self.bot.command_prefix}ss(1-3)]***', inline=False)
        embed.add_field(name='jobstatus (alias `js`)', value=f'{self.bot.command_prefix}js', inline=False)
        embed.add_field(name='tag', value=f'{self.bot.command_prefix}tag (option) 詳しくは `{self.bot.command_prefix}help tag` 又は `{self.bot.command_prefix}tag` を参照', inline=False)

        if ctx.channel.id in channel_ids:    # ctx.guild.id == 893402769254404117 or ctx.guild.id == 920561679266373642:
            embed.add_field(name='encode', value=f'{self.bot.command_prefix}ec `単語`', inline=False)
            embed.add_field(name='hb', value=f'#ゲーム, #ダメージ計算 内で Hit and Blow ができます。', inline=False)
        """
        sent_message = await ctx.send(embed=embed, view=DropView(bot=self.bot, ctx=ctx))
        await command_log(ctx=ctx, bot=self.bot, message=sent_message)

    """
    @command_help.command(name='dmg')
    async def damage_help(self, ctx: commands.Context, *args):
        await ctx.send(embed=discord.Embed(description=f'{self.bot.command_prefix}dmg [素ダメ] (OS, ないときは 0 となります。) (魔法石)'))

    @command_help.command(name='tag')
    async def tag_help(self, ctx: commands.Context, *args):
        embed = discord.Embed(title='tag の使い方')
        embed.add_field(name=f'{self.bot.command_prefix}tag add', value='リプライ元を指定してtagを追加します。', inline=False)
        embed.add_field(name=f'{self.bot.command_prefix}tag show', value='ユーザーidを指定するとその人のtagが、指定しない場合は自分のtagが表示されます。', inline=False)
        embed.add_field(name=f'{self.bot.command_prefix}tag delete (番号)', value='1 ~ 10の指定したtagが削除されます。指定しない場合は1番目が削除対象です。', inline=False)
        embed.add_field(name=f'{self.bot.command_prefix}tag reset', value='自分のtagがすべてリセットされます。', inline=False)
        await ctx.send(embed=embed)
        await command_log(ctx=ctx, bot=self.bot, message=ctx.message)
    """


class Dropdown(Select):
    def __init__(
            self,
            bot: commands.Bot,
            ctx: commands.Context
    ):
        self.bot = bot
        self.ctx = ctx
        options: list[SelectOption] = [
            SelectOption(
                label="Help",
                description="show this Select-option",
                emoji=H
            ),
            SelectOption(
                label="Damage",
                description="calculate damage",
                emoji=D
            ),
            SelectOption(
                label="Job",
                description="calculate damage of Job",
                emoji=J
            ),
            SelectOption(
                label="CoolTime",
                description="calculate all cooltime",
                emoji=C
            ),
            SelectOption(
                label="Ask Damage",
                description="calculate require damage",
                emoji=A
            ),
            SelectOption(
                label="Skill",
                description="calculate damage of skill",
                emoji=S
            ),
            SelectOption(
                label="Skill Simple",
                description="simple embed of skill command",
                emoji=S
            ),
            SelectOption(
                label="Tag",
                description="about Tag",
                emoji=T
            )
        ]
        if ctx.channel.id in channel_ids:
            options.extend(
                [
                    SelectOption(
                        label="Encode",
                        description="Encode to UTF-16",
                        emoji=E
                    ),
                    SelectOption(
                        label="Game",
                        description="start game Hit and Blow",
                        emoji=G
                    )
                ]
            )
        super().__init__(
            custom_id="commands",
            placeholder="Choose a command...",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: Interaction):
        embed = discord.Embed(
            title="help",
            colour=discord.Colour.green(),
            timestamp=interaction.message.created_at
        )
        embed.set_author(name=self.ctx.author.name, icon_url=self.ctx.author.avatar.url)
        match self.values[0]:
            case "Help":
                embed.title = "`help`"
                embed.description = f'{self.bot.command_prefix}help この画面を表示します。\n' \
                                    f'**<argument>**: 必須\n' \
                                    f'**[argument]**: 選択\n' \
                                    f'**[A|B]**: A 又は B'

            case "Damage":
                embed.title = "`Damage`"
                embed.description = f'{self.bot.command_prefix}dmg <素ダメ> <OS> [魔法石 1 ~ leg]\n\n' \
                                    f'ダメージを算出します。'

            case "Job":
                embed.title = "Job"
                embed.description = f'{self.bot.command_prefix}job <素ダメ> <OS> [魔法石 1 ~ leg]\n\n' \
                                    f'職業補正をかけたダメージを算出します。'

            case "CoolTime":
                embed.title = "`CoolTime`"
                embed.description = f'{self.bot.command_prefix}ct <そのままのCoolTime> <Quick Talk Spell Perk の値> [魔法石 1 ~ 5]\n\n' \
                                    f'石を付けた時のCTを算出します。'

            case "Ask Damage":
                embed.title = "`Ask Damage`"
                embed.description = f'{self.bot.command_prefix}ask <目的のダメージ> <素ダメ> ? [魔法石 1 ~ leg]  又は\n' \
                                    f'{self.bot.command_prefix}ask <目的のダメージ> ? <OS> [魔法石 1 ~ leg]\n\n' \
                                    f'目的のダメージを与えるための最低火力又はOS値を算出します。'

            case "Skill":
                embed.title = "`Skill`"
                embed.description = f'{self.bot.command_prefix}skill[1|2|3] <素ダメ> <OS> [魔法石 1 ~ leg]\n\n' \
                                    f'複数のスキルを職業ごとに算出します。'

            case "Skill Simple":
                embed.title = "`Skill Simple`",
                embed.description = f'{self.bot.command_prefix}sskill[1|2|3] <素ダメ> <OS> [魔法石 1 ~ leg]\n' \
                                    f'**[aliases: {self.bot.command_prefix}ss[1|2|3]]**\n\n' \
                                    f'skillコマンドのembedフィールドを減らして算出します。'

            case "Tag":
                embed = discord.Embed(title='tag の使い方', colour=discord.Colour.green())
                embed.add_field(name=f'{self.bot.command_prefix}tag add', value='リプライ元を指定してtagを追加します。', inline=False)
                embed.add_field(name=f'{self.bot.command_prefix}tag show',
                                value='ユーザーidを指定するとその人のtagが、指定しない場合は自分のtagが表示されます。', inline=False)
                embed.add_field(name=f'{self.bot.command_prefix}tag delete (番号)',
                                value='1 ~ 10の指定したtagが削除されます。指定しない場合は1番目が削除対象です。', inline=False)
                embed.add_field(name=f'{self.bot.command_prefix}tag reset', value='自分のtagがすべてリセットされます。', inline=False)

            case "Encode":
                embed.title = "encode"
                embed.description = f'{self.bot.command_prefix}ec <単語>\n' \
                                    f'単語をアイテム名としたテクスチャ用プロパティを作り、また、`.properties` ファイルを添付します。'

            case "Game":
                embed.title = "hit and blow"
                embed.description = f'{self.bot.command_prefix}hb\n\n' \
                                    f'#ゲーム, #ダメージ計算 内で Hit and Blow ができます。'

            case _:
                await error_log(ctx=self.ctx, bot=self.bot, error=KeyError("KeyError"))
                raise KeyError("KeyError")

        await interaction.response.edit_message(embed=embed)


class DropView(View):
    def __init__(self, bot: commands.Bot, ctx: commands.Context):
        super().__init__(
            timeout=180
        )
        self.bot = bot
        self.add_item(
            Dropdown(
                bot=self.bot,
                ctx=ctx
            )
        )


def setup(bot: commands.Bot):
    bot.add_cog(Help(bot))
