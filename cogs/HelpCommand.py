import discord
from discord.ext import commands

class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    @commands.Cog.listener()
    async def on_ready(self):
        print('HelpCommand is ready')
        print(".............................")  

    @commands.command(name='help')
    async def help(self, ctx):
        help_embed = discord.Embed(title='Help for Music Bot', description='List of commands', color=0x00ff00)
        
        help_embed.set_author(name='Music Bot')
        help_embed.add_field(name='!play', value='Play a song from Youtube url or title', inline=False)
        help_embed.add_field(name='!queue', value='Add a song to the queue', inline=False)
        help_embed.add_field(name='!skip', value='Skip the current song', inline=False)
        help_embed.add_field(name='!clear', value='Clear the queue', inline=False)
        help_embed.add_field(name='!pause', value='Pause the current song', inline=False)
        help_embed.add_field(name='!resume', value='Resume the current song', inline=False)
        help_embed.add_field(name='!stop', value='Stop the current song', inline=False)
  
        await ctx.send(embed=help_embed)

async def setup(bot):
    await bot.add_cog(HelpCommand(bot))