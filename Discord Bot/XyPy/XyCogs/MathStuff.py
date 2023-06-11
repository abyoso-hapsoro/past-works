import os, discord
from discord.ext import commands

os.environ['MPLCONFIGDIR'] = os.getcwd() + '/configs/'
import matplotlib.pyplot as plt

import numpy as np
from sympy import *
from sympy import symbols
from sympy.parsing.sympy_parser import parse_expr as parse
from sympy.parsing.sympy_parser import standard_transformations, implicit_multiplication_application

transformations = (standard_transformations +
                  (implicit_multiplication_application,))

###############################################################################

class MathStuff(commands.Cog):
  def __init__(self, bot):
    self.bot = bot


  @commands.command(
    help  = 'Can be used as a substitute calculator to some extent',
    brief = 'basic calculator'
  )
  async def calc(self, ctx, *args):
    context = ' '.join(args)
    await ctx.channel.send(parse(context))
  

  @commands.command(
    help  = 'syntax: _plot Plot[function, variable, start range, stop range, range step (optional, default = 1)]',
    brief = 'returns a plot with variable detection'
  )
  async def plot(self, ctx, *args):
    context = ''
    for arg in args:
      context += ' ' + arg.replace('\\', '').replace('^', '**')
    
    try:
      f, var, x0, x1, r = context[6:-1].split(',')     
    except ValueError:
      f, var, x0, x1    = context[6:-1].split(',')
      r       = 1
    
    f         = parse(f, transformations = transformations)
    var       = symbols(var)
    x0, x1, r = float(x0), float(x1), float(r)
    x_points  = np.arange(x0, x1 + r, r)
    y_points  = [f.subs(var, x_pt) for x_pt in x_points]
    
    image     = discord.File('your_plot.png')
    plt.plot(x_points, y_points, color = (44/255, 176/255, 55/255))
    
    plt.title(''); plt.xlabel(var)
    plt.ylabel(r'${}$'.format(str(f).replace('**', '^')))
    
    plt.xticks(x_points, [int(x_pt) if int(x_pt) == float(x_pt) else round(x_pt, 2) for x_pt in x_points])
    #plt.yticks(y_points, [int(y_pt) if int(y_pt) == float(y_pt) else round(y_pt, 2) for y_pt in y_points])
    
    plt.savefig('your_plot.png')
    plt.close()
    
    await ctx.channel.send(file = image)

def setup(bot):
  bot.add_cog(MathStuff(bot))