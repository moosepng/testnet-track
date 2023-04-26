import discord
import asyncio
import itemValue as i

bot_token = '###' #token is not here for privacy reasons
bot = discord.Client(intents=discord.Intents.default())

async def status_task():
    while True:
        item_name = i.puppyscan(2)
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"{item_name}"))
        print(item_name)
        await asyncio.sleep(300)

@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')
    bot.loop.create_task(status_task())
bot.run(bot_token)
