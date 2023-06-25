import discord
from discord.ext import commands
from random import randint

###############################################################################

class FunStuff(commands.Cog):
  
  def __init__(self, bot):
    self.bot = bot
  
  @commands.command(
    help  = 'Lofia from The Alchemist Code',
    brief = "Xyba's 2D waifu"
  )
  async def waifu(self, ctx):
    image = discord.Embed()
    image.set_image(url = 'https://cdn.alchemistcodedb.com/file/bb-acdb/images/UnitImages/rofi_xmas.png')
    await ctx.channel.send(embed = image)

  @commands.command(
    help  = 'P O N G',
    brief = 'pong'
  )
  async def ping(self, ctx):
    await ctx.channel.send('pong')

  @commands.command(
    help  = 'Guess a random integer from 1 to 100 with 5 tries. Guess -1 to abort midgame',
    brief = 'number guessing game'
  )
  async def ngg(self, ctx):
    init_auth, init_chan = ctx.author.id, ctx.channel.id
    await ctx.channel.send('Wanna play a game with XyPy? :o')
    
    async def check(msg):
      content  = msg.content.lower()
      response = True if content.startswith('y') or content.startswith('n') else False
      return msg.author.id == init_auth and msg.channel.id == init_chan and response

    async def num_check(msg):
      try:
        return msg.author.id == init_auth and msg.channel.id == init_chan and int(msg.content) == float(msg.content)
      except:
        await msg.channel.send('give XyPy an integer please~')
        return 0

    async def input_check():
      while True:
        guess = await self.bot.wait_for('message', check = num_check)
        try:
          guess = int(guess.content)
          return guess
        except:
          await msg.channel.send('give XyPy an integer please o.o')

    msg = await self.bot.wait_for('message', check = check)
    if msg.content.lower().startswith('y'):
      await msg.channel.send('yay~')
      await msg.channel.send('XyPy is thinking of a number between 1 and 100, you have 5 tries! owo')
      
      r_number, tries = randint(1, 100), 5
      await msg.channel.send('Go ahead and give a guess, first of five tries~')
            
      for Try in range(1, tries - 1):
        guess = await input_check()
        
        if guess == -1:
          await msg.channel.send('aw, aborting the game? play again soon~')
          break
        
        elif guess == r_number:
          await msg.channel.send('ooh you got it, thanks for playing with XyPy~')
          await msg.channel.send('you got it in {}'.format(Try))
          break
        
        elif guess < r_number - 3:
          await msg.channel.send('the number is higher, {} tries left'.format(tries - Try))
        
        elif guess > r_number + 3:
          await msg.channel.send('the number is lower, {} tries left'.format(tries - Try))
        
        else:
          await msg.channel.send('the number is close, {} tries left'.format(tries - Try))

      if guess != r_number:
        guess = await input_check()
        if guess == -1:
          await msg.channel.send('aw, aborting the game? play again soon~')
        
        elif guess == r_number:
          await msg.channel.send('ooh you got it, thanks for playing with XyPy~')
          await msg.channel.send('you got it in {}'.format(Try + 1))
        
        elif guess < r_number - 3:
          await msg.channel.send('the number is higher, final try~')
        
        elif guess > r_number + 3:
          await msg.channel.send('the number is lower, final try~')
        
        else:
          await msg.channel.send('the number is close, final try~')

      if guess != r_number:
        guess = await input_check()
        if guess == -1:
          await msg.channel.send('aw, aborting the game? play again soon~')
        
        elif guess == r_number:
          await msg.channel.send('ooh you got it, thanks for playing with XyPy~')
          await msg.channel.send('you got it in {}'.format(Try + 2))
        
        else:
          await msg.channel.send('haha you lose~, the number was {}'.format(r_number))
    
    else:
      await msg.channel.send('awww... (pout)')

async def setup(bot):
  await bot.add_cog(FunStuff(bot))