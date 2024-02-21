import discord
from discord.ext import commands
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib import font_manager
import logging
import io
import cogs.functions.document_functions as ds

logging.basicConfig(level=logging.WARNING)

class Document(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Latex cog loaded\n-----')

    @commands.command()
    async def document(self, ctx, *, formula):
        try:
            ds.formula1(formula)#descargar png
            file = discord.File("/home/armory/Documents/Programming/Projects/mext-bot/Formula.png", filename="Formula.png")#CONVIERTE EL PNG EN ARCHIVO PARA SUBIR AL MENSAJE
            mensaje_embed = discord.Embed()#CREA EL EMBED
            mensaje_embed.add_field(name="Formula",value="ESTO ES UNA PRUEBA")  
            mensaje_embed.set_image(url='attachment://Formula.png')#COMO URL DE IMAGEN SELECCIONA LA URL DEL ARCHIVO

            await ctx.send("Prubea",embed=mensaje_embed, file=file)
 
        except commands.BadArgument:
            await ctx.send("syntax bebe")
        except Exception as e:
            logging.error(f"Error in latex command: {e}")
            await ctx.send("chupala")

async def setup(bot):
    await bot.add_cog(Document(bot))

