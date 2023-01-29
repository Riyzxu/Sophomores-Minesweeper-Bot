import discord
from Minesweeper import generate_board

TOKEN = "TOKEN GOES HERE"

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

    if message.content.startswith('$ms'):
        if message.content[4:] == "invite":
            await message.channel.send("https://discord.com/oauth2/authorize?client_id=1069130432496533545&permissions=3072&scope=bot")

        elif "board" in message.content[4:]:
            inputs = [number for number in message.content[9:].split()]
            try:
                inputs[0] = int(inputs[0])
                inputs[1] = int(inputs[1])
                inputs[2] = int(inputs[2])
            except IndexError:
                await message.channel.send("Please provide all inputs!")
            else:
                try:
                    if inputs[3].lower() == "true":
                        inputs[3] = True
                    else:
                        inputs[3] = False
                except IndexError:
                    inputs.append(False)

                if inputs[2] > inputs[0] * inputs[1]:
                    await message.channel.send("Cant have more bombs than board size!")
                else:
                    if inputs:
                        board = generate_board(inputs[0], inputs[1], inputs[2], reveal=inputs[3])
                    else:
                        board = generate_board(4, 4, 3)

                    if inputs[0] >= 10 or inputs[1] >= 10:
                        await message.channel.send("Cant have a board this big! 9x9 is max size.")
                    else:
                        await message.channel.send(board)

        elif message.content[4:] == "help":
            await message.channel.send("Current commands:`help` `board` `invite`\n\nChoose the board size and bomb amount in the board command in the order row, col, bombs\nEg: `$ms board 3 3 2` (3x3 board with 2 bombs)\n\nThere is also optional feature to generate a board revealed fully, which you can set by typing `True` at the end of the board command\nEg: `$ms board 5 5 7 True` (5x5 board with 7 bombs and reveal set to true)")
        else:
            await message.channel.send("Wrong Command")


client.run(TOKEN)
