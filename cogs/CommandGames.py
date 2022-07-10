import pprint
import random
import re
from datetime import datetime
from typing import Dict, Any

import discord
import requests
from discord.ext import commands
from . import channel_ids, error_log

WIKI_URL = "https://ja.wikipedia.org/w/api.php?format=json&utf8&action=query&prop=revisions&rvprop=content&titles={}月{}日"


def channel_check(ctx: commands.Context):
    return ctx.channel.id in channel_ids


class GameCommands(commands.Cog):
    state_dict: Dict[int, Dict[str, Any]] = dict()

    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name='hb')
    @commands.check(channel_check)
    async def hit_and_blow(self, ctx: commands.Context, num: int = 3) -> None:
        """It starts a game of Hit and Blow.

        Parameters
        ----------
        ctx : commands.Context
            The context of the command.
        num : int, optional
            the number of digits to be guessed.

        Returns
        -------
            A string.

        """
        if ctx.author.bot:
            return
        print(self.state_dict)

        if ctx.author.id in self.state_dict:
            await ctx.send(f'{ctx.author} はゲームをプレイ中です。\n'
                           f'{self.bot.command_prefix}reset 又は'
                           f'{self.bot.command_prefix}res でゲームをリセットするか、'
                           f'回答を続けて下さい。')
            return

        await ctx.send(f'{ctx.author} が {num} 桁でゲームを開始しました。')
        correct = random.sample(list(range(10)), num)
        self.state_dict[ctx.author.id] = {'digit': num, 'times': 0, 'answer': correct, 'hit': 0, 'blow': 0}
        await ctx.send(f"{ctx.author} さん {num} 桁の数字を入力してください。")
        print(self.state_dict)

    @commands.command(name='reset', aliases=['res'])
    @commands.check(channel_check)
    async def reset_games(self, ctx: commands.Context):
        if ctx.author.bot:
            return

        if ctx.author.id not in self.state_dict:
            await ctx.send('あなたはゲームをしていません。')
            return
        await ctx.send(f'{ctx.author} がゲームをリセットしました。\n'
                       f'ただいまの挑戦回数: {self.state_dict[ctx.author.id]["times"]}\n'
                       f'解答: {self.state_dict[ctx.author.id]["answer"]}')
        del self.state_dict[ctx.author.id]

    @commands.Cog.listener()
    async def on_message(self, message: discord.Message):
        if message.author.id in self.state_dict \
                and not message.author.bot \
                and re.match(f'\d{{{self.state_dict[message.author.id]["digit"]}}}', message.content):
            self.state_dict[message.author.id]['times'] += 1
            answer = list(map(int, message.content[:]))
            hit = blow = 0

            for num in range(len(answer)):
                t = 'x'
                try:
                    t = list(self.state_dict[message.author.id]['answer']).index(answer[num])

                except ValueError:
                    pass

                if t != 'x':
                    if t == num:
                        hit += 1

                    else:
                        blow += 1

            await message.channel.send(f"{hit} Hit / {blow} Blow")
            if hit == self.state_dict[message.author.id]['digit']:
                await message.channel.send(f"{self.state_dict[message.author.id]['answer']} : "
                                           f"Correct! 挑戦回数：{self.state_dict[message.author.id]['times']} 回")
                del self.state_dict[message.author.id]

    # @commands.command(name='what', aliases=['wt'])
    # @commands.check(channel_check)
    async def what_the_day(self, ctx: commands.Context, month: str = str(datetime.now().month),
                           day: str = str(datetime.now().day)):
        if month.isdigit() & day.isdigit():
            month = int(month)
            day = int(day)
            print(type(month))
            if 1 <= month <= 12 & 1 <= day <= 31:
                if month in (4, 6, 9, 11):
                    pass
        r: dict = requests.get(url=WIKI_URL.format(month, day)).json()
        content = list(r["query"]["pages"].values())[0]["revisions"][0]["*"].split("\n")
        print()
        ctt = ''
        newlist = []

        def plus():
            pass
        if True:
            keepline = ""
            for line in content:

                if '[[ファイル:' in line or line.startswith("{{") or (line.startswith("<!--")):
                    continue

                if line == "== 出典 ==" or line == "== 関連項目 ==":
                    continue

                keepline = line
                ctt += line

                if line.startswith("==") or line.startswith("*"):
                    line = str(line).replace("[[", "").replace("]]", "")  # .replace(r"<ref>\{\{[A-z0-9 |=://.　\-?_\u4E00-\u9FD0｜\u30A1-\u30F4あ-ん]*\}\}</ref>", "")

            with open(file="file.txt", mode="a", encoding="utf8") as f:
                # ctt = re.sub(r"<ref>[A-z0-9 |=:/.\[\]{}\-?_\u4E00-\u9FD0｜\u30A1-\u30F4あ-ん～、。%+【】「」！？@ー々☆・／＼♡?!：〈〉]*</ref>", "", ctt)
                ctt = re.sub(r"<ref.*?/ref>", "", ctt)
                ctt = re.sub(r"<!--.*?-->", "", ctt)
                f.write(ctt.replace("[[", "").replace("]]", "") + "\n")
                print(ctt)

        pprint.pprint(ctt)

    @hit_and_blow.error
    @reset_games.error
    async def any_error(self, ctx: commands.Context, error: Exception) -> None:
        await error_log(bot=self.bot, ctx=ctx, error=error)


def setup(bot: commands.Bot):
    bot.add_cog(GameCommands(bot=bot))
