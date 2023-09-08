import discord
import openai


openai.api_key =

async def send_message(message, user_message, is_private):
    try:
        response = openai.Completion.create(
                model="text-davinci-003",
                prompt=user_message,
                max_tokens=3000,
                temperature=0.7
            )
        await message.author.send(response["choices"][0]["text"]) if is_private else await message.channel.send(response["choices"][0]["text"])

    except Exception as e:
        print(e)

def run_discord_bot():
    TOKEN =
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)
    # client = discord.Client()

    @client.event
    async def on_ready():
        print(f'{client.user} is now running!')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f'{username} said: "{user_message}" ({channel})')

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)


    client.run(TOKEN)
