from discord.ext import commands

###############################################################################

class Information(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(
    help  = 'Information on the bot you are using',
    brief = 'background info and plans'
  )
  async def info(self, ctx):
    await ctx.channel.send('''
      Still a very bareback developing bot intended for basic Mathematics, Python commands, LaTeX, wiki inquiries, health support, and potentially Machine Learning on the fly without needing to access your computer''' + 
      
      '```Created by\t: Xyba\nLast Updated  : 8 April 2021```'
      )

def setup(bot):
  bot.add_cog(Information(bot))