from discord.ext import commands

###############################################################################


class Information(commands.Cog):

  def __init__(self, bot):
    self.bot = bot

  @commands.command(
    help = 'Information on the bot you are using',
    brief = 'background info and plans'
  )
  async def info(self, ctx):
    await ctx.channel.send(
      '''
      Proof of concept bot for personal server. In the future, this bot may be improved or replaced entirely. Currently on version 0.38'''
      + '```Created by\t: Xyba\nLast Updated  : 27 June 2023```')

async def setup(bot):
  await bot.add_cog(Information(bot))