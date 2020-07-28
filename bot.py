import os
import discord
import numpy as np
from discord.ext import commands, tasks #Commands for bot listening, tasks TODO outside of commands
from discord.ext.tasks import loop
from dotenv import Dotenv
import time
import asyncio


#initialize dictionaries and lists for later
people = {}
timersKey = {}
timeVals = []




dotenv = Dotenv('/home/pi/Documents/DiscordBot/.env')
TOKEN = str(dotenv['DISCORD_TOKEN']) + 'Y'
GUILD = '623888011918180372'
client = discord.Client()

# Set prefix
bot = commands.Bot(command_prefix = '/') #bot will listen for "/"


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

#Reset Shot Counter
@bot.command(name='clearShot')
async def clear(ctx):
    await ctx.send('Clearing shots')
    global people
    people ={}
    
#/shot "name" keeps track of shots for "name"    
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

#prints how many shots have been taken
@bot.command(name='howmany')
async def count(ctx):
    for keys in people:
        print(keys)
        message = keys + ' has taken ' + str(people.get(keys)) + ' shots!'
        await ctx.send(message)

    
#finds a random madlib from website
@bot.command(name='lib')
async def lib(ctx):
    number1 = str(np.random.randint(0, 1))
    number2 = str(np.random.randint(0, 9))
    number3 = str(np.random.randint(0, 9))

    link = 'https://www.madtakes.com/libs/' + number1 + number2 + number3 + '' + '.html'
    await ctx.send(link)

#sets up timer for when someone has to get on WOW
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
    
    start = (time.time())/60 #set start time
    chn = ctx #save the message context. Used to send the message back to the same guild it came from
    timersKey.update({author:[min,start,chn]}) #update timer dictionary with list of values 
    print(timersKey)
    
#print out timer for message author
@bot.command(name = 'timer')
async def lib(ctx):
    global timersKey
    author = str(ctx.message.author)
    
    if author in timersKey: #if the author is in 
        list = timersKey.get(author)
        timeLeft = int(list[0] - ((time.time() /60 )- list[1] ))
        
        await ctx.send(author + " has " + str(timeLeft) + " minutes to start playing WoW")
    else:
        await ctx.send("You do not have a timer")
        
#Create a task to check for timer end and send message (loops once a second)
@tasks.loop(seconds=1)
async def fun():
    global timersKey
    
    #loop through all keys
    for keys in timersKey:
        list = timersKey.get(keys)
        readyCheck = (time.time() /60 ) - list[1] 
        
        #if the timer is up send message to same guild it came from. (using context in dict)
        if (readyCheck >= list[0]):
            print(keys + 'is ready')
            timersKey.pop(keys) #detele the dictionary value
            print(timersKey)
            channel = list[2] #get contect from dictionary
            await channel.send('@' + keys + ' needs to start playing WOW right fucking now') #send message
            return
        else:
            print(readyCheck)
        print('looping')
    
fun.start() #start looping the timer function


bot.run(TOKEN) #run bot