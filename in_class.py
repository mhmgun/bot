import discord
from discord.ext import commands
import random


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')


@bot.command()
async def YetiskinCevreKoruma(ctx):
    with open("yetiskinlere.txt","r",encoding="utf8") as f:
        yetiskinler=f.readlines()
    with open("images/egzoz.jpg", "rb") as f:
        resim=discord.File(f)
    await ctx.send(random.choice(yetiskinler)) 
    await ctx.send(file=resim)

@bot.command()
async def GencCevreKoruma(ctx):
    with open("gencler.txt","r",encoding="utf8") as f:
        gencler=f.readlines()
    with open("images/pil.jpg", "rb") as f:
        resim1=discord.File(f)
    await ctx.send(random.choice(gencler))
    await ctx.send(file=resim1)


bot.run("TOKEN")
