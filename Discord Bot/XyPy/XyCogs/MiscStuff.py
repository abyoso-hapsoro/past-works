import discord
from discord.ext import commands
import wikipedia

###############################################################################

class MiscStuff(commands.Cog):
  
  def __init__(self, bot):
      self.bot = bot
  
  @commands.command(
    help  = 'basic syntax: _wiki Query\nplanned optional syntax: after Query, iso 639-1 two letter country code for language',
    brief = 'search for anything in wikipedia'
  )
  async def wiki(self, ctx, *args):
    wikipedia.set_lang('en')
    page = wikipedia.page(''.join(args)).url
    await ctx.channel.send(page)

  @commands.command(
    help  = 'same function as wiki but in Indonesian',
    brief = 'search for anything in wikipedia ID'
  )
  async def wikiID(self, ctx, *args):
    wikipedia.set_lang('id')
    page = wikipedia.page(''.join(args)).url
    await ctx.channel.send(page)

async def setup(bot):
  await bot.add_cog(MiscStuff(bot))