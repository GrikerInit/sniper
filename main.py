import discord
from discord.ext import commands
import os

client = commands.Bot(command_prefix=".")
token = os.getenv("DISCORD_BOT_TOKEN")
client.sniped_messages = {}

@client.event
async def on_ready() :
    await client.change_presence(status = discord.Status.idle, activity = discord.Game(".snipe by Rozeen"))
    print("I am online")

@client.event
async def on_message_delete(message):
    print(f'sniped message {message}')
    client.sniped_messages[message.guild.id] = (
        message.content, message.author, message.channel.name, message.created_at)


@client.command()
async def snipe(ctx):
    try:
        contents, author, channel_name, time = client.sniped_messages[ctx.guild.id]

    except:
        await ctx.channel.send("Couldn't find a message to snipe!")
        return

    embed = discord.Embed(description=contents,
                          color=discord.Color.purple(), timestamp=time)
    embed.set_author(
        name=f"{author.name}#{author.discriminator}", icon_url=author.avatar_url)
    embed.set_footer(text=f"Deleted in : #{channel_name}")

    await ctx.channel.send(embed=embed)


client.run(token)