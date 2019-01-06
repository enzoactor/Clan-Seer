import discord

client = discord.Client()

######################################################
@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if message.content.startswith('!Tryout'):
        msg = 'Wanna Tryout? {0.author.mention}'.format(message)
        await client.send_message(message.channel, msg)
        
    elif message.content.startswith('!getstarted'):
        await client.send_message(message.channel, "DM the owner in order to get started")
        
    elif message.content.startswith('!help'):
        await client.send_message(message.channel, "join talk-with-the-owner to get help")
        
        
######################################################
@client.event
async def on_member_join(member):
    server = member.server
    fmt = "Hello {0.mention}, I a'm the clan seer. I am here to get you ready to tryout for {1.name}!"
    await client.send_message(server, fmt.format(member, server))
######################################################
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')





client.run('NTMxMzEyMzM3MjAyNzA4NDgw.DxMI9Q.WZq0u9yabk89zMEVwRxKGd4BK9o')
