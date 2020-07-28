
import os
import discord
import numpy as np
from discord.ext import commands, tasks
from discord.ext.tasks import loop
from dotenv import Dotenv
import time
import asyncio
#import json
#import requests

#initialize variables for later
juanShot = 0
erikShot = 0
mackShot = 0
dadShot = 0
people = {}
timersKey = {}
timeVals = []





dotenv = Dotenv('/home/pi/Documents/DiscordBot/.env')
TOKEN = str(dotenv['DISCORD_TOKEN']) + 'Y'
GUILD = '623888011918180372'
client = discord.Client()

# Set prefix
bot = commands.Bot(command_prefix = '/')

#dictionary api
language = "en-gb"
word_id = "example"
app_id = "ff5dc17c"
app_key = " ef439ee7c67ce69d35aea42ee3c2cfe7"


@bot.event # print when connected
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')





# Rolling d100
    @bot.command(name ='roll') # look for prefix+'roll'
    async def rolling(ctx):
        number = str(np.random.randint(1,100)) #find random number
        author = str(ctx.message.author) #get author
        author = author[:-5] #delete author number

        response = '**' + author + ' rolls a ' + number + '**'  # Create response
        await ctx.send(response)  # Send response
        #Print online members
        onlineMember = bot.user









@bot.command(name ='nug') # look for prefix + 'nug'
async def rolling(ctx):
    response = '<:nugget:724445623906205756>' # Create emoji response

    await ctx.send(response) # send

@bot.command(name ='2nug') # look for prefix + '2nug'
async def rolling(ctx):
    response = '<:nugget:724445623906205756>' + '<:nugget:724445623906205756>' # Create emoji response

    await ctx.send(response) # send

@bot.command(name ='rollforgold') # look for prefix+'roll'
async def rolling(ctx):
    number = str(np.random.randint(1,100)) #find random number
    author = str(ctx.message.author) #get author
    author = author[:-5] #delete author number

    response = '**' + author + ' rolls a ' + number + '**'  # Create response
    #await ctx.send(response)  # Send response
    #Print online members
    i = 1
    for user in ctx.guild.members:
        if user.status == discord.Status.online:
            if (user.name != 'rollForGold'):
                number = str(np.random.randint(1, 100))
                num = str(user.id)
                ask =  "*" + user.name + " rolls a " + number+"*"
                await ctx.send(ask)

# @bot.command(name='shot')
# async def takingshot(ctx):
#     global juanShot
#     global mackShot
#     global erikShot
#     global dadShot
#     success = False
#
#     author = str(ctx.message.author)
#     me = ctx.message.content
#     print(me)
#
#     if (me.find('mack') != -1):
#         success = True
#         mackShot += 1
#         sstr = str(mackShot)
#         shotSay = 'Mack has taken ' + sstr + ' shots'
#         await ctx.send(shotSay)
#
#     if(me.find('mom') != -1):
#         success = True
#         juanShot += 1
#         sstr = str(juanShot)
#         shotSay = 'mom has taken ' + sstr + ' shots'
#         await ctx.send(shotSay)
#
#     if (me.find('juan') != -1):
#         success = True
#         juanShot += 1
#         sstr = str(juanShot)
#         shotSay = 'mom has taken ' + sstr + ' shots'
#         await ctx.send(shotSay)
#
#     if(me.find('erik') != -1):
#         success = True
#         erikShot += 1
#         sstr = str(erikShot)
#         shotSay = 'Erik has taken ' + sstr + ' shots'
#         await ctx.send(shotSay)
#     if(me.find('dad') != -1):
#         success = True
#         dadShot += 1
#         sstr = str(dadShot)
#         shotSay = 'Dad has taken ' + sstr + ' shots'
#         await ctx.send(shotSay)
#
#
#     if(success == False):
#
#         await ctx.send('AnOther OnE FaLls')
#         if (author == 'ToyotaPrius#0656'):
#             mackShot += 1
#             sstr = str(mackShot)
#             shotSay = 'Mack has taken ' + sstr + ' shots'
#             await ctx.send(shotSay)
#
#         if (author == 'Juan#5791'):
#             juanShot += 1
#             sstr = str(juanShot)
#             shotSay = 'mom has taken ' + sstr + ' shots'
#             await ctx.send(shotSay)
#
#         if (author == 'OldManPoole#3601'):
#             erikShot += 1
#             sstr = str(erikShot)
#             shotSay = 'Erik has taken ' + sstr + ' shots'
#             await ctx.send(shotSay)
#         if (author == 'Funky King#2073'):
#             dadShot += 1
#             sstr = str(dadShot)
#             shotSay = 'Dad has taken ' + sstr + ' shots'
#             await ctx.send(shotSay)

@bot.command(name='clearShot')
async def clear(ctx):
    await ctx.send('Clearing shots')
    global people
    people ={}
    
@bot.command(name = 'shot')
async def shots(ctx):
    global people
    me = ctx.message.content #read message
    me = me.lower()  # set to lower case
    # take out the bot command from text
    me = me.replace('/shot ','')
    me = me.replace('/shot','')

    me.lower() #set to lower case
    print(me)
    while (me == ''):
        await ctx.send('Please give a name')# send response
        break
    if (me in people): #if the person in message is in the dictionary
        people[me] += 1 #add one to their value
        shotSay = me + ' has taken ' + str(people[me]) + ' shots!' #type out response
        await ctx.send(shotSay) #send response
        print(people)
        print('if')


    else:
        people.update({me:1}) #add them to dictionary with a value of 1
        shotSay = me + ' has taken ' + str(people[me]) + ' shots!' #Type out the message
        await ctx.send(shotSay)   #send response
        print(people)
        print('else')


@bot.command(name='howmany')
async def count(ctx):
    for keys in people:
        print(keys)
        message = keys + ' has taken ' + str(people.get(keys)) + ' shots!'
        await ctx.send(message)

    

@bot.command(name='lib')
async def lib(ctx):
    number1 = str(np.random.randint(0, 1))
    number2 = str(np.random.randint(0, 9))
    number3 = str(np.random.randint(0, 9))

    link = 'https://www.madtakes.com/libs/' + number1 + number2 + number3 + '' + '.html'
    await ctx.send(link)

@bot.command(name ='giveme')
async def lib(ctx):
    global timersKey
    author = str(ctx.message.author)
    me = str(ctx.message.content)  # read message
    me = me.lower()  # set to lower case
    # take out the bot command from text
    min = int(str(me.replace('/giveme ', '')))
    min = int(str(me.replace('/giveme', '')))
    
    minStr = str(min)
    await ctx.send(author + " has " + minStr + " minutes to start playing WOW")
    
    start = (time.time())/60
    chn = ctx
    timersKey.update({author:[min,start,chn]})
    print(timersKey)
    
@bot.command(name = 'timer')
async def lib(ctx):
    global timersKey
    author = str(ctx.message.author)
    
    if author in timersKey:
        list = timersKey.get(author)
        timeLeft = int(list[0] - ((time.time() /60 )- list[1] ))
        
        await ctx.send(author + " has " + str(timeLeft) + " minutes to start playing WoW")
    else:
        await ctx.send("You do not have a timer")
        
# async def timers():
#     global timersKey
#     await bot.wait_until_ready()
#      
#     for keys in timersKey:
#         ready = time.time() - timersKey.get(keys[1])
#         print(timersKey)
#          
#     await asyncio.sleep(5)
@tasks.loop(seconds=1)
async def fun():
    global timersKey
    
    for keys in timersKey:
        list = timersKey.get(keys)
        readyCheck = (time.time() /60 ) - list[1] 
        
        if (readyCheck >= list[0]):
            print(keys + 'is ready')
            timersKey.pop(keys)
            print(timersKey)
            channel = list[2]
            await channel.send('@' + keys + ' needs to start playing WOW right fucking now')
            return
        else:
            print(readyCheck)
        print('looping')
    
fun.start()


bot.run(TOKEN)