import discord
import responses

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)
        
        
def run_discord_bot():
    TOKEN = 'MTE0ODc0MDk1ODQwMjM5MjA4NA.GlGqII.6VYTg4vAc6sh6p58b3T8IsC-K-pcVI07JZRz4I'

    intents = discord.Intents.default()
    # intents.message_content = True
    client = discord.Client(intents=intents)
    
    @client.event
    async def on_ready():
        print(f'{client.user} is now running')
        

    
    @client.event
    async def on_message(message):
        # To make sure that the bot doesnt listen to itself
        if message.author == client.user:
            return
        
        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)
        
        print(f"Username : {username}, user message : {user_message}, channel : {channel}")
        
        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)


    client.run(TOKEN)
        