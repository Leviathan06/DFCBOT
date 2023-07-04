import discord
import random

from discord.ext import commands

# bot = commands.Bot(command_prefix='$')ㄴ
# bot = commands.Bot(status=discord.Status.online)

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', activity=discord.Game(name='$추가,$추천') , intents=intents)

foods = ['돼지국밥','순대국밥','짜장면','짬뽕','전','조개구이','떡볶이','초밥','파스타','대창']

@bot.event
async def on_ready():
    print(f'Login bot: {bot.user}')
 
@bot.command()
async def 추천(ctx):
    menu = random.choice(foods)
    embed = discord.Embed(title="오늘의 메뉴추천", color=0xf15f5f)
    embed.set_footer(text='오늘의 메뉴는! %s 입니다. 메뉴를 추가하고 싶으시다면 $추가 명령어를 사용 해 주세요'% menu)

    await ctx.send(embed=embed)

# async def 추가(ctx):
#     ctx.
#     foods.append()
@bot.command()
async def 추가(ctx, food):
    
    if food in foods:
        await ctx.reply(f"{food}(이)가 추가되지 못했습니다.리스트에 중복되는 값이 있습니다.")
    else:
        foods.append(food)
        await ctx.reply(f"{food}가 추가되었습니다.")
    
 
bot.run('MTEyNTcyNDYzOTU0OTczMDgzNw.GcSdBW.HhWcn6ZBitu95A-ebuVEpEg9aSpRwsIcv5Ikqo')