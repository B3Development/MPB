import discord

from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

################################### Clear Command ###################################

    @commands.command(name = 'clear', description = "Removes specified amount of messages from current channel.", aliases = ['cc', 'purge'])
    @commands.has_permissions(manage_messages = True)
    async def clear(self, ctx, amount: int = 10):
        """Removes specified amount of messages from current channel."""

        await ctx.channel.purge(limit = amount)

################################### Echo Command ###################################

    @commands.command(name = 'echo', description = "Responds with the message provided.")
    @commands.has_permissions(administrator = True)
    async def echo(self, ctx, *, arg = ""):
        """Responds with the message provided."""

        await ctx.channel.purge(limit = 1)

        if arg == "":
            embed = discord.Embed(title = "What do you want me to say?", color = 0x7289da)
            await ctx.send(embed = embed)
        else:
            embed = discord.Embed(title = f"{arg}", color=0x7289da)
            await ctx.send(embed = embed)

################################### Kick Command ###################################

    @commands.command(name = 'kick', description = "Kicks specified member.")
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, member : discord.Member, *, reason = None):
        """Kicks specified member."""
        await member.kick(reason = reason)

    @commands.command(name = 'ban', description = "Bans specified member.")
    @commands.has_permissions(ban_members = True, kick_members = True)
    async def ban(self, ctx, member : discord.Member, *, reason = None):
        """Bans specified member."""
        await member.ban(reason = reason)

################################### Mute Command ###################################

    @commands.command(name = 'mute', description = "Mutes specified member.")
    @commands.has_permissions(ban_members = True, kick_members = True)
    async def mute(self, ctx, member : discord.Member, *, reason = None):
        """Mutes specified member."""
        guild = ctx.guild
        mutedRole = discord.utils.get(guild.roles, name = "Muted")

        if not mutedRole:
            mutedRole = await guild.create_role(name = "Muted")

            for channel in guild.channels:
                await channel.set_permissions(mutedRole, speak = False, send_messages = False)

        await member.add_roles(mutedRole, reason = reason)
        embed = discord.Embed(title = f"{member} has been muted!", color = 0x7289da)
        embed.set_thumbnail(url = member.avatar)
        embed.add_field(name  = "User ID", value = member.id)
        embed.add_field(name  = "Reason:", value = reason)

        await ctx.send(embed = embed)

################################### Unmute Command ###################################

    @commands.command(name = 'unmute', description = "Unmutes specified member.")
    @commands.has_permissions(ban_members = True, kick_members = True)
    async def unmute(self, ctx, member : discord.Member):
        """Unmutes specified member."""
        mutedRole = discord.utils.get(ctx.guild.roles, name = "Muted")

        await member.remove_roles(mutedRole)
        embed = discord.Embed(title = f"{member} has been unmuted!", color = 0x7289da)
        embed.set_thumbnail(url = member.avatar)
        embed.add_field(name  = "User ID", value = member.id)

        await ctx.send(embed = embed)

#########################################################################################

def setup(client):
    client.add_cog(Admin(client))