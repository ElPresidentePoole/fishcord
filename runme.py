import discord

def main():
    token = 'REPLACE ME WITH YOUR BOT TOKEN'

    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'We have logged in as {client.user}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if 'fish' in message.content.lower() or 'fsh' in message.content.lower():
            with open('blub.mov', 'rb') as blub_file:
                df = discord.File(blub_file)
                await message.channel.send(f'{message.author.mention}',file=df)

    client.run(token)

if __name__ == '__main__':
    main()
