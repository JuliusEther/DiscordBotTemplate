from discord.ext.commands import Bot, Cog, command, Context
from discord.member import Member
from discord.channel import TextChannel

from bot.core import Core

def setup(bot: Bot):
	bot.add_cog(Greetings(bot))


class Greetings(Cog):
    
    def __init__(self, bot: Bot):
        self.bot = bot
        self.logger = Core.GetLogger()
    

    @Cog.listener()
    async def on_member_join(self, member: Member):
        self.logger.debug(f"member {member.display_name} joined.")
        channel: TextChannel = member.guild.system_channel
        if channel is not None:
            await channel.send(f"Welcome {member.mention}.")


    @command()
    async def hello(self, ctx: Context): 
        self.logger.debug(f"'hello' command called by {ctx.author}.")
        await ctx.send(f'Hello {ctx.author.name}.')

