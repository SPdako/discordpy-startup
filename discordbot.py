from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def hello(ctx):
    await ctx.send('こんにちは！私はpunra(ぷんら)。この鯖のお手伝いさんだよ！~~(予定)~~え、誰かに似てるって？そ、、、そんなはずないでしょっ！')
    
    
bot.run(token)
