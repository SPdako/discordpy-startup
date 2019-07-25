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
async def pnrhello(ctx):
    await ctx.send('こんにちは！私はpunra(ぷんら)。この鯖のお手伝いさんだよ！~~(予定)~~え、誰かに似てるって？そ、、、そんなはずないでしょっ！')
    
@bot.command()
async def pnrhelp(ctx):
    await ctx.send('```【/ping】 pongと言い返すよ。テスト用だからしばらくしたらなくなるよ　【/help】このヘルプを呼び出すよ　【/hello】挨拶するよ！```')
    
    
bot.run(token)
