import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from random import randint
import manplotv0_5.manplot_2018 as manplot
import time


bot = commands.Bot(command_prefix='!')
RPS_players=0
Time=0
playerOne=""
playerTwo=""

async def draw(name,server):
	r=randint(0,2)
	if r==0:
		await bot.say(name+" cracked open")
		await bot.send_file(server,r"[INSERT DIRECTORY HERE]rock.png")
		#r="rock"
	elif r==1:
		await bot.say(name+" cracked open")
		await bot.send_file(server,r"[INSERT DIRECTORY HERE]scissors.png")
		#r="scissors"
	elif r==2:
		await bot.say(name+" cracked open")
		await bot.send_file(server,r"[INSERT DIRECTORY HERE]paper.png")
		#r="paper"
	else:
		print("Couldn't roll")
	return r	

@bot.event
async def on_ready(): 
	print ("I've got my shit together")
	print ("Time for " + bot.user.name+ "to fuck shit up")
	print ("ID: " + bot.user.id)

@bot.event
async def on_message(message):
	message.content=message.content.lower()
	await bot.process_commands(message)

@bot.command(pass_context=True)
async def poke(ctx):
	await bot.say("Don't touch me there.")
	print ("User has pinged" + bot.user.name)


@bot.command(pass_context=True)
async def rps(ctx):
	global playerOne
	global playerTwo
	global RPS_players
	global Time
	roll=randint(0,2)
	server=ctx.message.channel
	if (((time.time() - Time) > 60) and not (playerOne=="")):
		await bot.say("No one wanted to play with " + playerOne + ", how sad.")
		RPS_players=0
		playerOne=""
	if RPS_players==1:
		playerTwo=ctx.message.author.mention
		player1=await draw(playerOne,server)
		player2=await draw(playerTwo,server)
		if player1 == 0:
			if player2 == 1:
				await bot.say(playerTwo+" was smashed by " + playerOne)
			elif player2 == 2:
				await bot.say(playerTwo+" covered " + playerOne)
			elif player2 == 0:
				await bot.say(playerTwo+" tied with " + playerOne)
			else:
				print("Error determining winner")
		elif player1 == 1:
			if player2 == 1:
				await bot.say(playerTwo+" tied with " + playerOne)
			elif player2 == 2:
				await bot.say(playerTwo+" was shredded by " + playerOne)
			elif player2 == 0:
				await bot.say(playerTwo+" smashed " + playerOne)
			else:
				print("Error determining winner")
		elif player1 == 2:
			if player2 == 1:
				await bot.say(playerTwo+" shredded " + playerOne)
			elif player2 == 2:
				await bot.say(playerTwo+" tied with " + playerOne)
			elif player2 == 0:
				await bot.say(playerTwo+" was covered by " + playerOne)
			else:
				print("Error determining winner")
		RPS_players=0
		playerOne=""
		playerTwo=""
	elif RPS_players==0:
		playerOne=ctx.message.author.mention
		await bot.say(ctx.message.author.mention+" wants to play Rock Paper Scissors. Waiting for someone to join with #rps")
		RPS_players=1
		Time=time.time()

image_counter=0
@bot.command(pass_context=True)
async def fractal(ctx):
	global image_counter
	server=ctx.message.channel
	#await bot.say("THIS IS A SECRET!!!!! WRRRRRRRYYYYYYY!!!!!!!!")
	manplot.fractal_image(-2.0,1.0,-1.5,1.5,count=image_counter)
	await bot.send_file(server,r"[INSERT DIRECTORY HERE]"+str(image_counter)+".png")
	image_counter += 1

bot.run("[INSERT BOT TOKEN HERE]")
bot.connet(reconnect=True)