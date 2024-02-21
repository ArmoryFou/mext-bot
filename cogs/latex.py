import discord
from discord.ext import commands
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import font_manager
import logging
import io

logging.basicConfig(level=logging.WARNING)

class Latex(commands.Cog):
    def __init__(self, bot):        
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Latex cog loaded\n-----')

    @commands.command()
    async def latex(self, ctx, *, formula):
        plt.rcParams.update(plt.rcParamsDefault)
        try:

            font_dirs = ["./fonts"]
            font_files = font_manager.findSystemFonts(fontpaths=font_dirs)
            for font_file in font_files:
                print(font_file)
                font_manager.fontManager.addfont(font_file)
            font = {'family': 'Noto Sans Math',
            'color':  'darkred',
            'weight': 'normal',
            'size': 50,
            }
            plt.rcParams['mathtext.fontset'] = 'custom'
            plt.rcParams['mathtext.rm'] = 'PazoMath'
            plt.rcParams['mathtext.it'] = 'PazoMath'
            plt.rcParams['mathtext.bf'] = 'PazoMath'
            fig, ax = plt.subplots()
            ax.axis('off')
            ax.text(0.5, 0.5, formula, ha='center', va='center', fontdict=font)
            data_stream = io.BytesIO()
            plt.savefig(data_stream, format='png', bbox_inches='tight', dpi=80)
            plt.close()

            data_stream.seek(0)
            file = discord.File(data_stream, filename="formula.png")

            embed = discord.Embed(title="LaTeX", description=formula, color=0xFF5733)
            embed.set_image(url="attachment://formula.png")
            await ctx.send(embed=embed, file=file)

        except commands.BadArgument:
            await ctx.send("syntax bebe")
        except Exception as e:
            logging.error(f"Error in latex command: {e}")
            await ctx.send("chupala")

async def setup(bot):
    await bot.add_cog(Latex(bot))

