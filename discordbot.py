import discord

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
    await ctx.send('こんにちは！私はpunra(ぷんら)。この鯖のお手伝いさんだよ！\nえ、誰かに似てるって？そ、、、そんなはずないでしょっ！')
    
@bot.command()
async def pnrhelp(ctx):
    await ctx.send('```【/ping】 pongと言い返すよ。テスト用だからしばらくしたらなくなるよ\n【/pnrhelp】このヘルプを呼び出すよ\n【/pnrhello】挨拶するよ！\n【/ppq、/cf、/sg、/notpnr】それぞれ、役職を付けるよ！詳しくは鯖の"#お知らせ"を見てね```')
    
@bot.command()
async def ppq(ctx):
    role = discord.utils.get(ctx.guild.roles, name='パトルプッシャーカンテサンス勢')
    await ctx.author.add_roles(role)
    reply = f'{ctx.author.mention} 役職を設定したよ！'
    await ctx.send(reply)
        
@bot.command()
async def cf(ctx):
    role = discord.utils.get(ctx.guild.roles, name='コズミックフィーバー勢')
    await ctx.author.add_roles(role)
    reply = f'{ctx.author.mention} 役職を設定したよ！'
    await ctx.send(reply)

@bot.command()
async def sg(ctx):
    role = discord.utils.get(ctx.guild.roles, name='スフィートガーデン勢')
    await ctx.author.add_roles(role)
    reply = f'{ctx.author.mention} 役職を設定したよ！'
    await ctx.send(reply)
    
@bot.command()
async def notpnr(ctx):
    role = discord.utils.get(ctx.guild.roles, name='そもそもPNRやってない勢')
    await ctx.author.add_roles(role)
    reply = f'{ctx.author.mention} 役職を設定したよ！'
    await ctx.send(reply)
    
@bot.command()
async def newshop(ctx):
    category = bot.get_channel(shop)
    await category.create_text_channel(ctx.author.name)
    
bot.run(token)
