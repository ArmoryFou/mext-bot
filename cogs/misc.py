import discord
from discord.ext import commands

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Misc cog loaded\n-----')

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        channel = self.bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        user = self.bot.get_user(payload.user_id)
        if not user:
            user = await self.bot.fetch_user(payload.user_id)
        embed=discord.Embed(title="Mensaje guardado", description=message.content, color=0xFF5733)
        embed.set_author(name=message.author.name, icon_url=message.author.avatar)
        if message.attachments:
            embed.add_field(name="Adjunto", value=message.attachments[0].url, inline=False)
            if message.attachments[0].content_type.split('/')[0] == 'image':
                embed.set_image(url=message.attachments[0].url)
        await user.send(content=message.jump_url, embed=embed)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'pong!\n{round(self.bot.latency * 1000)}ms')
 
async def setup(bot):
    await bot.add_cog(Misc(bot))

