import discord
import time

intents = discord.Intents.all()
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    running = True
    while running:
        for guild in client.guilds:
            for user in guild.members: # get all members in the server
                if user is not None: # first check is user is valid
                    if user.activities is not None: # check if any user activities
                        for activity in user.activities: # go through each activity
                            print(activity)
                            if activity.name == "League of Legends": # if it's the game that will not be mentioned, message them
                                await user.send("appropriate message :)")
        time.sleep(10)
        
client.run("no peeking ;)")