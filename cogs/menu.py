import discord
from discord.ext import commands
import json
import cogs.functions.document_functions as ds
import os 

class Select(discord.ui.Select):
    def __init__(self):
        with open('./formulas.json') as user_file:
            file_contents = user_file.read()
        data = json.loads(file_contents)
        options = [discord.SelectOption(label=key, description=f"Todas las formulas referidas a los {key}") for key, value in data.items()]
        super().__init__(placeholder="¿Que formula quieres?",
                         max_values=1, min_values=1, options=options)
    
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message("ELIGE UNA FORMULA", view=SelectView2(selected=self.values[0]))

class Select2(discord.ui.Select):
    def __init__(self, selected):
        with open('./formulas.json') as user_file:
            file_contents = user_file.read()
        data = json.loads(file_contents)[selected] 
        options = [discord.SelectOption(label=key, description=f"Todas las formulas referidas a los {key}") for key, value in data.items()]
        super().__init__(placeholder="¿Que formula quieres?",
                         max_values=1, min_values=1, options=options)
        self.selected = selected  

    async def callback(self, interaction: discord.Interaction):
        with open('./formulas.json') as user_file:
            file_contents = user_file.read()
        data2 = json.loads(file_contents)[self.selected]
        for key2, value2 in data2.items():
            print(value2)
            if self.values[0] == key2:
                ds.formula1(value2)
                print("Descargando Imagen")
                file = discord.File("/home/armory/Documents/Programming/Projects/mext-bot/Formula.png", filename="Formula.png")
                mensaje_embed = discord.Embed()
                mensaje_embed.add_field(name="Formula",value="")  
                mensaje_embed.set_image(url='attachment://Formula.png')
                await interaction.response.send_message(f"Enviando Formulas de {key2}" ,embed=mensaje_embed, file=file)
                os.remove("/home/armory/Documents/Programming/Projects/mext-bot/Formula.png")

class SelectView(discord.ui.View):
    def __init__(self, *, timeout=30):
        super().__init__(timeout=timeout)
        self.add_item(Select())

class SelectView2(discord.ui.View):
    def __init__(self, selected, *, timeout=30):
        super().__init__(timeout=timeout)
        self.selected = selected
        self.add_item(Select2(selected))

class Formula(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def formula(self, ctx):
        await ctx.channel.send("ELIGE UNA FORMULA", view=SelectView())

async def setup(bot):
    await bot.add_cog(Formula(bot))
