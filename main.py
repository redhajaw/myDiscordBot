import os
import asyncio
from discord.ui import Button, View
import json #for API data
import requests
import random
import discord
from discord.ext import commands
#my_secret = os.environ['TOKEN']

intents = discord.Intents.all()

#add prefix as an ! for your robot commands
bot = commands.Bot(command_prefix='!redha',intents = intents)


#print a message to the console when your bot is online
@bot.event
async def on_connect():
  print("!redha")


@bot.command()
async def reply (ctx):
  await ctx.reply("Hello from RedhasBot")

@bot.command()
async def Name(ctx, name):
  await ctx.reply("Hello, " + name + " nice to meet you")

@bot.command()
async def Time(ctx, hour, ampm):
  if (ampm == 'am'):
    await ctx.reply('Good morning')

  else:
    hour2 = int(hour)
    if (hour2 >= 6):
      await ctx.reply('Good Evening')
  if hour == '12 pm':
    await ctx.reply("It's noon")
  
  if (ampm == 'pm'):
    await ctx.reply('Good Evening')

@bot.command()
async def Pic(ctx):
  await ctx.reply ('http://www.clipartbest.com/cliparts/4T9/LM8/4T9LM8jTE.png')


@bot.command()
async def RandPic(ctx):

  myList=["https://www.wilsoninfo.com/flowers/2021-purple-flowers.jpg" ,        "http://www.clipartbest.com/cliparts/4T9/LM8/4T9LM8jTE.png" ,                 "https://media.istockphoto.com/photos/otter-picture-id637219822?s=612x612" , "https://icatcare.org/app/uploads/2018/10/persian.jpg"]

  botchoice= random.choice(myList)


  await ctx.reply (botchoice)

@bot.command()
async def Add(ctx, num1, num2):
  num3 = int(num1) + int(num2)
  await ctx.reply(str(num1 + "+" + str(num2) + "=" + str(num3)))

@bot.command()
async def eightBall(ctx , *, phrase):
  eightList = ["without a doubt", "not likely", "maybe" , "yes slayyy"]

  ballchoice = random.choice(eightList)

  await ctx.reply (phrase + ballchoice)

@bot.command()
async def RPS(ctx, choice):

  myList = ["rock" , "paper", "scissors"]

  botchoice = random.choice(myList)
  choice=choice.lower()#turns choice into lowercase

  if botchoice == choice:
    await ctx.send("Tie , you chose" + choice + " , and bot chose" +              botchoice)
  if botchoice == "rock" + choice == "scissors":
    await ctx.send("You lost! you chose " + choice + "and bot chose " +           botchoice)
  if botchoice == "scissors" + choice == "rock":
    await ctx.send("You won! you chose " + choice + "and bot chose " +            botchoice)
  if botchoice == "paper" + choice == "scissors":
    await ctx.send("You won! you chose " + choice + "and bot chose " +            botchoice)
  if botchoice == "scissors" + choice == "paper":
    await ctx.send("You lost! you chose " + choice + "and bot chose " +           botchoice)
  if botchoice == "paper" + choice == "rock":
    await ctx.send("You lost! you chose " + choice + "and bot chose " +           botchoice)
  if botchoice == "rock" + choice == "paper":
    await ctx.send("You won! you chose " + choice + "and bot chose " +            botchoice)
  

#API intro
@bot.command()
async def Joke (ctx):
  #create a variable for the joke API url
  url = "https://official-joke-api.appspot.com/random_joke"
  #contact the url
  req = requests.get(url)
  #Get data from the joke url
  data = req.json()
  #pull the setup of the joke
  setup = data["setup"]
  #pull the punchline
  punchline = data["setup"]
  await ctx.send(setup)
  #await asyncio.sleep(3)
  await ctx.send[punchline]


@bot.command()
async def Weather(ctx, zip):
  #create a variable for the joke API url
  url = "https://api.openweathermap.org/data/2.5/weather?                       zip="+zip+",US&appid=f0fbcb5b3c9f71aca0c4dd6fb1fc6c42"
  #contact the url
  req = requests.get(url)
  #Get data from the weather API
  data = req.json()
#pull description for weather
  weather = data["weather"][0]["description"]
  temp = data["main"]["temp"]
#convert to farenheit
  temp = (temp - 273.15) * 9/5 + 32
  #round to the tenth
  temp = round(temp,1)
  await ctx.send(req)
  await ctx.send(weather + " " + str(temp) + "Degrees F")
  await ctx.send(temp)

@bot.command(brief = "Welcome")
async def button (ctx):
  button1=Button(label="Granada High School", url="https://www.livermoreschools.org/Domain/104")
  
  async def button1Clicked(interaction):
    await interaction.response.send_message("Thanks for clicking the button")

  button1.callback=button1Clicked

  view = View()
  view.add_item(button1)

  await ctx.send("Hello from Redha's bot check out the buttons", view=view)

  
  


  
  


#copy your bot token from discord developer

bot.run("MTAzNDM0MzI4NDI3MDcxNDkyMQ.Gy40R-.GskpLVo3_QL2FvYYvdRj2jKytmqySkAce0jhmQ")


'''
@bot.command()
async def Time(ctx, time, day):
  time = int(time)
  if day.lower() == "pm"
    if time == 12:
      await ctx.send("it's noon time")
    elif time < 5
      await ctx.send("Good Afternoon")
    elif time < 8:
      await ctx.send("Good Evening")
    else:
      await ctx.send("Good Night")
  elif day.lower() == "am"
    if time == 12:
    await ctx.send("it's midnight")
  else:
    await ctx.send("good morning")
    '''

