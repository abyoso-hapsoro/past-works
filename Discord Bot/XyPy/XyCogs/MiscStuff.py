from discord.ext import commands
import asyncio
import wikipedia

###############################################################################

class MiscStuff(commands.Cog):
  
  def __init__(self, bot):
      self.bot = bot
  
  @commands.command(
    help  = 'Deletes the last X messages',
    brief = 'cleans messages'
  )
  async def purge(self, ctx, *args):
    try:
      if int(args[0]) == float(args[0]):
        context = int(args[0])
      if 0 < context < 101:
        pass
      else:
        raise
    except:
      await ctx.channel.send('Please input a integer greater than 0 and maximum of 100')
    await ctx.channel.send('XyPy will delete the last {} messages in 5 seconds, awaiting no if cancel is desired'.format(context))
    
    try:
      opt_to_cancel = await self.bot.wait_for('message', timeout = 5)
      if opt_to_cancel.content.lower() == 'no':
        await ctx.channel.send('Purging cancelled')
    except asyncio.TimeoutError:
      await ctx.channel.purge(limit = context + 2)
  
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