import discord
import random
import time
from discord.ext import commands

intents = discord.Intents.default()

intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents)


@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba {bot.user}! Ben çevre dostu bir botum!')
    time.sleep(1)
    await ctx.send(f'Haydi biraz sohbet edelim')


@bot.command()
async def chat(ctx):
    await ctx.send(f'Merhaba! Kaç yaşındasınız?')

@bot.command()
async def cevre(ctx):
    await ctx.send(f'Çevre ve kirlilik hakkında bir şey yapmak istiyorsanız öneri komutunu kullanın!')

@bot.command()
async def oneri(ctx):
    await ctx.send(f'Geri dönüşüm ve hangi malzemelerin geri dönüştürülebileceği hakkında bilgi edinin ve günlük yaşamınızda geri dönüştürülebilir malzemeleri kullanın')
    time.sleep(1)
    await ctx.send(f'Eski eşyaları çöpe atmak yerine geri dönüştürün')
    time.sleep(1)
    await ctx.send(f'Tek kullanımlık ürünlerin kullanımını azaltmak için yeniden kullanılabilir ürünler kullanın.')
    time.sleep(1)
    await ctx.send(f'Hangi ürünlerin ve ambalajların geri dönüşüm için en iyi olduğunu araştırın ve satın alırken bunları seçin.')
    time.sleep(1)
    await ctx.send(f'Su kullanmadığınız zamanlarda musluğu açık bırakmayarak su tasarrufu yapın.')
    time.sleep(1)
    await ctx.send(f'Evde ampuller ve klimalar gibi enerji tasarruflu cihazlar kullanın..')
    time.sleep(1)
    await ctx.send(f'Ulaşım masraflarını azaltmak için yerel kaynaklardan yiyecek satın alın.')
    time.sleep(1)
    await ctx.send(f'Araba kullanmak yerine toplu taşıma araçlarını, bisikletleri ve kullanmaya çalışın.')

@bot.command()
async def resim(ctx):
    with open(r'Cevre_botum\Resimler\images.jpg', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
    time.sleep(1)
    await ctx.send(f'Hep birlikte tercih ve alışkanlıklarımızı değiştirerek çevre kirliliği sorununu çözmeye çalışalım ve dünyamızı temiz tutalım.')


@bot.command()
async def yas(ctx):
    await ctx.send("Merhaba, Kaç yaşındasın?")

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    try:
        message = await bot.wait_for('message', check=check)
        yas = int(message.content)

        if yas < 18:
            await ctx.send("cevre kirliliği ile ilgili bilgi")
        else:
            await ctx.send("su kirliliği")
        if yas < 35:
            await ctx.send("")

bot.run("")
