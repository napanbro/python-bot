import discord 
from discord.ext import commands
intents = discord.Intents(messages = True,guilds=True,reactions=True,members=True,presences=True)
Bot = commands.Bot(command_prefix=".",intents=intents)
@Bot.event
async def on_ready():
	print("Çalıştım man")

@Bot.command()
async def clear(ctx,amount=5):
	await ctx.channel.purge(limit= amount)
	
@Bot.command()
@commands.has_role("boss")
async def kick(ctx, member:discord.Member,*args,reason = "yok"):
	await member.kick(reason= reason)

@Bot.command()
@commands.has_role("boss")
async def ban(ctx, member:discord.Member,*args,reason = "yok"):
	await member.ban(reason= reason)
	
@Bot.command()
@commands.has_role("boss")
async def unban(ctx,*,member):
	banneds = await ctx.guild.bans()
	membername,memberid = member.split("#")
	for bans in banneds:
		user = bans.user
		if(user.name,user.discriminator) == (membername,memberid):
			await ctx.guild.unban(user)
			await ctx.send(f'  {user.mention} banı açıldı')
			return
			

Bot.run('ODAxNDAwNzg5NjExNTc3Mzc1.YAgIpQ.Vb5Kw3ZWaCVKShb7f8nuqsLhceE')