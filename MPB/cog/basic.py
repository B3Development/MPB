import discord

from discord.ext import commands
from random import randint

class Basic(commands.Cog):
    def __init__(self, client):
        self.client = client

################################ What's Next Command ################################

    @commands.command()
    async def whatsnext(self, ctx):

        embed = discord.Embed(title = "> What's to come?", description = "⌯ Music system\n⌯ Bug fixing\n⌯ Code cleanup", color = 0x7289da)

        await ctx.send(embed = embed)

################################### GitHub Command ###################################

    @commands.command()
    async def github(self, ctx):

        embed = discord.Embed(title = "> My GitHub Page!", description = "https://github.com/TheFwayne/MPB", color = 0x7289da)

        await ctx.send(embed = embed)

################################### Roll Command ###################################

    @commands.command(name = 'roll', description = "Rolls a random number between 1 and 10.")
    async def roll(self, ctx):
        """Rolls a random number between 1 and 10."""

        length = randint(1, 10)
        if length == 8:
            embed = discord.Embed(title = f"{ctx.author.name} rolled an **8**", color = 0x7289da)
            await ctx.send(embed = embed)
        else:
            embed = discord.Embed(title = f"{ctx.author.name} rolled a **{length}**", color = 0x7289da)
            await ctx.send(embed = embed)

################################### Ping Command ###################################

    @commands.command(name = 'ping', description = "Sends back client's ping in milliseconds.")
    async def ping(self, ctx):
        """Sends back client's ping in milliseconds."""

        embed = discord.Embed(title = f"**🏓   | ** *{round(self.client.latency * 1000)}ms*")

        await ctx.send(embed = embed)

################################### User Info Command ###################################

    @commands.command(name = 'userinfo', description = "Displays information about the user specified member.")
    async def userinfo(self, ctx, member: discord.Member = None):
        """Displays information about the user specified."""

        if not member:
            member = ctx.message.author
        roles = [role for role in member.roles]
        embed = discord.Embed(colour = discord.Colour.blurple(), timestamp = ctx.message.created_at, title = f"User Info - {member}")
        embed.set_thumbnail(url = member.avatar)
        embed.set_footer(text = f"Requested by {ctx.author}")

        embed.add_field(name  = "User ID", value = member.id)
        embed.add_field(name = "Display Name", value = member.display_name)
        embed.add_field(name = "Joined Server On", value = member.joined_at.strftime("%#d %B %Y"))
        embed.add_field(name = "Roles:", value = "".join([role.mention for role in roles]))

        await ctx.send(embed = embed)

################################### Server Info Command ###################################

    @commands.command(name = 'serverinfo', description = "Displays information about the server.")
    async def serverinfo(self, ctx):
        """Displays information about the server."""
        
        name = str(ctx.guild.name)
        description = str(ctx.guild.description)

        owner = str(ctx.guild.owner)
        id = str(ctx.guild.id)
        region = str(ctx.guild.region)
        memberCount = str(ctx.guild.member_count)

        icon = str(ctx.guild.icon)
        
        embed = discord.Embed(
            title = name + " | Server Information",
            description = description,
            timestamp = ctx.message.created_at,
            color = discord.Color.blurple()
            )
        embed.set_thumbnail(url = icon)
        embed.add_field(name = "Owner", value = owner, inline = True)
        embed.add_field(name = "Server ID", value = id, inline = True)
        embed.add_field(name = "Region", value = region, inline = True)
        embed.add_field(name = "Member Count", value = memberCount, inline = True)
        embed.set_footer(text = f"Requested by {ctx.author}")

        await ctx.send(embed = embed)

###########################################################################################

def setup(client):
    client.add_cog(Basic(client))