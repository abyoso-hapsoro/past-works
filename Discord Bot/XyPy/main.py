import discord, os
from discord.ext import commands
from discord.ext.commands import CommandNotFound
from dotenv import load_dotenv

from keep_alive import keep_alive

###############################################################################


class XyClient(commands.Bot):

  def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)

  async def on_ready(self):
    for cog in cogs:
      await self.load_extension('XyCogs.' + cog)
    print('XyPy at the ready~')

  async def on_message(self, message):
    if message.content[1:] == 'hello':
      await message.channel.send('Hello .w.')
    elif message.content[1:] == 'badbot':
      image = discord.Embed()
      file = discord.File('badbot.png')
      image.set_image(url = 'attachment://badbot.png')
      await message.channel.send(file = file, embed = image)
    else:
      await self.process_commands(message)

  async def on_command_error(self, ctx, error):
    if isinstance(error, CommandNotFound):
      await ctx.channel.send("XyPy doesn't know how to do that :(")
      # await ctx.channel.send('XyPy currently under maintenance >w<')
    return


client = XyClient(intents = discord.Intents.all(),
                  command_prefix = '_',
                  case_insensitive = True)
cogs = ['Information', 'MathStuff', 'FunStuff', 'MiscStuff']

keep_alive()
load_dotenv()
TOKEN = os.environ.get('SECRET_TOKEN')

if __name__ == '__main__':
  client.run(TOKEN)
