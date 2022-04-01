import discord
from discord.ext.commands import Bot
bot = Bot(command_prefix='$')
TOKEN = '<OTU4OTE3MjM2NjMyOTgxNTI1.YkUTRQ.eQkWt7N2iQN6me9j1aGHykxIczs>'

@bot.event
async def on_ready():
	print(f'Bot connected as {bot.user}')
  
bot.run(token)
