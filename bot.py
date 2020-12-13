import os
import discord
import numpy as np
from discord.ext import commands, tasks  # Commands for bot listening, tasks TODO outside of commands
from discord.ext.tasks import loop
import time
import asyncio
# NEW IMPORTS
from spotifyFunction import create_playlist, removePlaylist, AddSong, getURI, get_userplaylist, refreshAuthorization

# initialize dictionaries and lists for later
people = {}
timersKey = {}
timeVals = []
pollCreator = ''
pollStep = 0
charResp = 'a'
pollDict = {}
fullResponse = ''
emojiResponse = []

# for spotify
playList = ""
playListOnTime = 0

emojiLetters = ["\N{REGIONAL INDICATOR SYMBOL LETTER A}",
                "\N{REGIONAL INDICATOR SYMBOL LETTER B}",
                "\N{REGIONAL INDICATOR SYMBOL LETTER C}",
                "\N{REGIONAL INDICATOR SYMBOL LETTER D}",
                "\N{REGIONAL INDICATOR SYMBOL LETTER E}",
                "\N{REGIONAL INDICATOR SYMBOL LETTER F}",
                "\N{REGIONAL INDICATOR SYMBOL LETTER G}",
                "\N{REGIONAL INDICATOR SYMBOL LETTER H}",
                "\N{REGIONAL INDICATOR SYMBOL LETTER I}",
                "\N{REGIONAL INDICATOR SYMBOL LETTER J}",
                "\N{REGIONAL INDICATOR SYMBOL LETTER K}",
                "\N{REGIONAL INDICATOR SYMBOL LETTER L}",
                "\N{REGIONAL INDICATOR SYMBOL LETTER M}",
                "\N{REGIONAL INDICATOR SYMBOL LETTER N}",
                "\N{REGIONAL INDICATOR SYMBOL LETTER O}",
                "\N{REGIONAL INDICATOR SYMBOL LETTER P}",
                "\N{REGIONAL INDICATOR SYMBOL LETTER Q}",
                "\N{REGIONAL INDICATOR SYMBOL LETTER R}",
                "\N{REGIONAL INDICATOR SYMBOL LETTER S}",
                "\N{REGIONAL INDICATOR SYMBOL LETTER T}",
                "\N{REGIONAL INDICATOR SYMBOL LETTER U}",
                "\N{REGIONAL INDICATOR SYMBOL LETTER V}",
                "\N{REGIONAL INDICATOR SYMBOL LETTER W}",
                "\N{REGIONAL INDICATOR SYMBOL LETTER X}",
                "\N{REGIONAL INDICATOR SYMBOL LETTER Y}",
                "\N{REGIONAL INDICATOR SYMBOL LETTER Z}"]

TOKEN = os.getenv('DISCORD_SECRET')
USER_ID = os.getenv('USER_ID')
CLIENT_ID = os.getenv('CLIENT_ID')
REFRESH_TOKEN = os.getenv('REFRESH_TOKEN')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')




resp = refreshAuthorization(REFRESH_TOKEN,CLIENT_ID,CLIENT_SECRET)
STOKEN = resp['access_token']
refreshTimer = time.time()
print("Token Refreshed")
intents = discord.Intents.all()
client = discord.Client()

# Set prefix
bot = commands.Bot(command_prefix='/',intents=intents)  # bot will listen for "/"


@bot.event  # print when connected
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')
    # create initial spotify playlist
    global playList
    global playListOnTime
    # read playlists
    playlistResponse = get_userplaylist(STOKEN, USER_ID)
    items = playlistResponse['items']
    # Check if playlist already created
    playlistNames = []

    for keys in items:
        playlistNames.append(keys['name'])
        name = keys['name']
        if name == 'Weenie Bot Playlist':
            print(keys['id'])
            playList = keys['id']

    print(playlistNames)

    if 'Weenie Bot Playlist' in playlistNames:
        print('There is already a Play List')
        print(playList)

    else:
        playList = create_playlist(STOKEN, USER_ID)
        print(playList)

    playListOnTime = time.time()/60



    # Rolling d100
    @bot.command(name='roll')  # look for prefix+'roll'
    async def rolling(ctx):
        number = str(np.random.randint(1, 100))  # find random number
        author = str(ctx.message.author)  # get author
        author = author[:-5]  # delete author number

        response = '**' + author + ' rolls a ' + number + '**'  # Create response
        await ctx.send(response)  # Send response


@bot.command(name='nug')  # look for prefix + 'nug'
async def rolling(ctx):
    response = '<:nugget:724445623906205756>'  # Create emoji response

    await ctx.send(response)  # send


@bot.command(name='2nug')  # look for prefix + '2nug'
async def rolling(ctx):
    response = '<:nugget:724445623906205756>' + '<:nugget:724445623906205756>'  # Create emoji response

    await ctx.send(response)  # send


@bot.command(name='rollforgold')  # look for prefix+'roll'
async def rolling(ctx):
    print("Rolling for Gold")
    number = str(np.random.randint(1, 100))  # find random number
    author = str(ctx.message.author)  # get author
    author = author[:-5]  # delete author number

    response = '**' + author + ' rolls a ' + number + '**'  # Create response
    # await ctx.send(response)  # Send response
    # Print online members
    i = 1
    print((ctx.guild.members))
    for user in ctx.guild.members:
        if user.status == discord.Status.online:
            if (user.name != 'Weenie Bot General'):
                number = str(np.random.randint(1, 100))
                num = str(user.id)
                ask = "*" + user.name + " rolls a " + number + "*"
                print(ask)
                await ctx.send(ask)


# Reset Shot Counter
@bot.command(name='clearShot')
async def clear(ctx):
    await ctx.send('Clearing shots')
    global people
    people = {}


# /shot "name" keeps track of shots for "name"
@bot.command(name='shot')
async def shots(ctx):
    global people
    me = ctx.message.content  # read message
    me = me.lower()  # set to lower case
    # take out the bot command from text
    me = me.replace('/shot ', '')
    me = me.replace('/shot', '')

    me.lower()  # set to lower case
    print(me)
    while (me == ''):
        await ctx.send('Please give a name')  # send response
        break
    if (me in people):  # if the person in message is in the dictionary
        people[me] += 1  # add one to their value
        shotSay = me + ' has taken ' + str(people[me]) + ' shots!'  # type out response
        await ctx.send(shotSay)  # send response
        print(people)
        print('if')


    else:
        people.update({me: 1})  # add them to dictionary with a value of 1
        shotSay = me + ' has taken ' + str(people[me]) + ' shots!'  # Type out the message
        await ctx.send(shotSay)  # send response
        print(people)
        print('else')


# prints how many shots have been taken
@bot.command(name='howmany')
async def count(ctx):
    for keys in people:
        print(keys)
        message = keys + ' has taken ' + str(people.get(keys)) + ' shots!'
        await ctx.send(message)


# finds a random madlib from website
@bot.command(name='lib')
async def lib(ctx):
    number1 = str(np.random.randint(0, 1))
    number2 = str(np.random.randint(0, 9))
    number3 = str(np.random.randint(0, 9))

    link = 'https://www.madtakes.com/libs/' + number1 + number2 + number3 + '' + '.html'
    await ctx.send(link)


# sets up timer for when someone has to get on WOW
@bot.command(name='giveme')
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

    start = (time.time()) / 60  # set start time
    chn = ctx  # save the message context. Used to send the message back to the same guild it came from
    timersKey.update({author: [min, start, chn]})  # update timer dictionary with list of values
    print(timersKey)


# print out timer for message author
@bot.command(name='timer')
async def lib(ctx):
    global timersKey
    author = str(ctx.message.author)

    if author in timersKey:  # if the author is in
        list = timersKey.get(author)
        timeLeft = int(list[0] - ((time.time() / 60) - list[1]))

        await ctx.send(author + " has " + str(timeLeft) + " minutes to start playing WoW")
    else:
        await ctx.send("You do not have a timer")


# Print out all active timers
@bot.command(name='alltimers')
async def lib(ctx):
    global timersKey
    for keys in timersKey:  # loop through all the people
        print(keys)
        list = timersKey.get(keys)  # get the values
        timeLeft = int(list[0] - ((time.time() / 60) - list[1]))  # calculate time left
        await ctx.send(keys + " has " + str(timeLeft) + " minutes to start playing WoW")


# Create a task to check for timer end and send message (loops once a second)
@tasks.loop(seconds=1)
async def fun():
    global timersKey
    global playList
    global playListOnTime
    global STOKEN
    global USER_ID
    global refreshTimer

    # loop through all keys
    for keys in timersKey:
        list = timersKey.get(keys)
        readyCheck = (time.time() / 60) - list[1]

        # if the timer is up send message to same guild it came from. (using context in dict)
        if (readyCheck >= list[0]):
            print(keys + 'is ready')
            timersKey.pop(keys)  # detele the dictionary value
            print(timersKey)
            channel = list[2]  # get contect from dictionary
            await channel.send('@' + keys + ' needs to start playing WOW right fucking now')  # send message
            return
        else:
            print(readyCheck)
        print('looping')
    #refresh access token
    if time.time() - refreshTimer > 3000:
        resp = refreshAuthorization(REFRESH_TOKEN,CLIENT_ID,CLIENT_SECRET)
        STOKEN = resp['access_token']
        refreshTimer = time.time()
        print("Token Refreshed")

    #check spotify end
    playListOffTime = playListOnTime + 360
    if (playListOffTime - (time.time()/60)) < 0:
        #remove playlist
        removePlaylist(STOKEN,playList)

        #creat new
        # read playlists
        playlistResponse = get_userplaylist(STOKEN, USER_ID)
        items = playlistResponse['items']
        # Check if playlist already created
        playlistNames = []

        for keys in items:
            playlistNames.append(keys['name'])
            name = keys['name']
            if name == 'Weenie Bot Playlist':
                print(keys['id'])
                playList = keys['id']

        print(playlistNames)

        if 'Weenie Bot Playlist' in playlistNames:
            print('There is already a Play List')
            print(playList)

        else:
            playList = create_playlist(STOKEN, USER_ID)
            print(playList)

        playListOnTime = time.time() / 60


#delete playlist restart timer
@bot.command(name='restartPlaylistEverything')
async def lib(ctx):
    global playList
    global STOKEN
    global playListOnTime

    #delete playlist
    removePlaylist(STOKEN,playList)

    #restart playlist
    #creat new
    # read playlists
    playlistResponse = get_userplaylist(STOKEN, USER_ID)
    items = playlistResponse['items']
    # Check if playlist already created
    playlistNames = []

    for keys in items:
        playlistNames.append(keys['name'])
        name = keys['name']
        if name == 'Weenie Bot Playlist':
            print(keys['id'])
            playList = keys['id']

    print(playlistNames)

    if 'Weenie Bot Playlist' in playlistNames:
        print('There is already a Play List')
        print(playList)

    else:
        playList = create_playlist(STOKEN, USER_ID)
        print(playList)

    playListOnTime = time.time() / 60
    await ctx.send("Playlist Restarted")




#get playlist URL
@bot.command(name = 'playlist')
async def lib(ctx):
    global playList

    #send the current playlist
    message = "The current playlist is:  " + "https://open.spotify.com/playlist/" + playList
    await ctx.send(message)


# Start poll command
@bot.command(name='poll')
async def lib(ctx):
    global pollCreator
    global pollStep
    global pollDict

    if (pollStep != 0):
        await ctx.send("Someone is already making a poll")
        return

    pollStep = 1  # Change the step of poll creation
    pollCreator = str(ctx.message.author)  # write who is creating poll
    pollStart = time.time() / 60
    pollEnd = pollStart + 60
    pollDict.update({pollCreator: [pollStart, pollEnd, ctx]})
    await ctx.send(pollCreator + ' please type a question')

#add song to spotify
@bot.command(name='addsong')
async def lib(ctx):
    global STOKEN
    global playList

    me = ctx.message.content  # read message
    me = me.lower()  # set to lower case

    noCommand = str(me.replace('/addsong ', ''))
    both = noCommand.split(', ')
    
    songToAdd = 0

    if len(both) > 1:
        song_name = both[0]
        artist = both[1]
        songToAdd = getURI(STOKEN,USER_ID,song_name,artist)

    else:
        await ctx.send("Put a comma between the artist and the song")


    if songToAdd == 0:
        await ctx.send('This is not a song')
    else:
        await ctx.send('Song Added')
        AddSong(STOKEN,songToAdd,playList)





@bot.event
async def on_message(message):
    global pollCreator
    global pollDict
    global pollStep
    global charResp
    global fullResponse
    global emojiResponse
    global emojiLetters
    if (str(message.author) == pollCreator):
        if (pollStep == 1):
            list = pollDict.get(pollCreator)
            (pollDict[pollCreator]).append(str(message.content))
            # print(list)
            await message.delete()
            await message.channel.send('Type the responses separated by commas')
            pollStep = 2
            await bot.process_commands(message)
            return
        if (pollStep == 2):
            (pollDict[pollCreator]).append(str(message.content))
            list = pollDict.get(pollCreator)
            # send the poll message
            print(list)
            question = list[3]
            response = list[4]
            splitResponse = response.split(',')
            print(splitResponse)

            fullResponse = '**' + question + '** \n'
            n = 0

            for i in splitResponse:
                emojiResponse.append(':regional_indicator_' + charResp + ':')

                charResp = ord(charResp[0]) + 1
                charResp = str(chr(charResp))
                fullResponse = fullResponse + splitResponse[n] + ': ' + emojiResponse[n] + '\n'
                n += 1

            chn = list[2]
            await message.delete()
            msg = await message.channel.send(fullResponse)
            y = 0
            for i in splitResponse:
                emojiResponse[y].replace('_', ' ')
                emojiResponse[y].upper()
                await msg.add_reaction(emojiLetters[y])  # need to figure out this unicode thing
                y += 1

            pollStep = 0
            n = 0


    else:
        await bot.process_commands(message)
        return

    await bot.process_commands(message)


# Start bot Start functions
fun.start()  # start looping the timer function
bot.run(TOKEN)  # run bot
