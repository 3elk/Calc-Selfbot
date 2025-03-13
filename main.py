#TOOL BY ELK
#DISCORD: 2elk
#GITHUB: 3elk

import subprocess
import os
import sys
import discord
from discord.ext import commands
import asyncio
import msvcrt

def install_module(module_name):
    try:
        subprocess.check_call([os.sys.executable, "-m", "pip", "install", module_name])
    except subprocess.CalledProcessError:
        (f"Failed to install module {module_name}")
def import_discord():
    try:
        import discord
        return discord
    except ModuleNotFoundError:
        print("Discord module wasnt found, installing...")
        install_module("discord")
        import discord
        return discord
discord = import_discord()

token = "YOUR_TOKEN" # CHANGE THIS TO YOUR TOKEN
os.system("cls")
os.system("title CALC-SelfBot")
os.system("chcp 65001 >nul")
os.system("mode 70, 15")
bot = commands.Bot(command_prefix="$", self_bot=True, intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f"""
 .d8888b.        d8888 888      .d8888b.         .d8888b.  888888b.   
d88P  Y88b      d88888 888     d88P  Y88b       d88P  Y88b 888  "88b  
888    888     d88P888 888     888    888       Y88b.      888  .88P  
888           d88P 888 888     888               "Y888b.   8888888K.  
888          d88P  888 888     888                  "Y88b. 888  "Y88b 
888    888  d88P   888 888     888    888 888888      "888 888    888 
Y88b  d88P d8888888888 888     Y88b  d88P       Y88b  d88P 888   d88P 
 "Y8888P" d88P     888 88888888 "Y8888P"         "Y8888P"  8888888P"  
                                                                                                                              
                        CONNECTED >> {bot.user}
                    (TIP: Type "$h" for commands)""")
    async def check_exit():
        while True:
            await asyncio.sleep(1)
            if msvcrt.kbhit():
                if msvcrt.getch() == b"\x1a":
                    await bot.close()
                    sys.exit()
    bot.loop.create_task(check_exit())

@bot.command()
async def delete(ctx, amount:int):
    if amount <=0:
        await ctx.send("```INVALID AMOUNT```")
    deleted = 0
    async for message in ctx.channel.history(limit=amount):
        if message.author == ctx.author:
            await message.delete()
            deleted += 1

@bot.command()
async def ping(ctx):
    latency = round(bot.latency * 1000)
    response = f"""```Pong! | Latency >> {latency}ms```
    """
    await ctx.message.delete()
    await ctx.send(response)

@bot.command()
async def add(ctx, num1: int, num2: int):
    response = f"```{num1} + {num2} = {num1 + num2}```"
    await ctx.message.delete()
    await ctx.send(response)

@bot.command()
async def sub(ctx, num1: int, num2: int):
    response = f"```{num1} - {num2} = {num1 - num2}```"
    ctx.message.delete()
    await ctx.send(response)
@bot.command()
async def mul(ctx, num1: int, num2: int):
    await ctx.send(f"```{num1} * {num2} = {num1 * num2}```")
    await ctx.send(response)
@bot.command()
async def div(ctx, num1: int, num2: int):
    if num2 == 0:
        await ctx.send("```ERROR >> Cannot divide by zero```")
        await ctx.message.delete()
    else:
        await ctx.send(f"```{num1} / {num2} = {num1 / num2}```")
        await ctx.message.delete()
@bot.command()
async def mod(ctx, num1: int, num2: int):
    if num2 == 0:
        await ctx.send("```ERROR >> Cannot divide by zero```")
        await ctx.message.delete()
    else:
        await ctx.send(f"```{num1} % {num2} = {num1 % num2}```")
        await ctx.message.delete()
@bot.command()
async def pow(ctx, num1: int, num2: int):
    await ctx.send(f"```{num1} ^ {num2} = {num1 ** num2}```")
    await ctx.message.delete()
@bot.command()
async def sqr(ctx, num: int):
    await ctx.send(f"```√{num} = {num ** 0.5}```")
    await ctx.message.delete()
@bot.command()
async def dadd(ctx, num1: float, num2: float):
    result = num1 + num2
    await ctx.send(f"```{num1} + {num2} = {result}```")
    await ctx.message.delete()

@bot.command()
async def dmod(ctx, num1: float, num2: float):
    if num2 == 0:
        await ctx.send("```ERROR >> Cannot divide by zero```")
        await ctx.message.delete()
        return
    result = num1 % num2
    await ctx.send(f"```{num1} % {num2} = {result}```")
    await ctx.message.delete()

@bot.command()
async def dpow(ctx, num1: float, num2: float):
    result = num1 ** num2
    await ctx.send(f"```{num1} ^ {num2} = {result}```")
    await ctx.message.delete()

@bot.command()
async def dsqr(ctx, num1: float, num2: float):
    result = num1 ** (1/num2)
    await ctx.send(f"```{num1} ^ (1/{num2}) = {result}```")
    await ctx.message.delete()

@bot.command()
async def dsub(ctx, num1: float, num2: float):
    result = num1 - num2
    await ctx.send(f"```{num1} - {num2} = {result}```")
    await ctx.message.delete()

@bot.command()
async def dmul(ctx, num1: float, num2: float):
    result = num1 * num2
    await ctx.send(f"```{num1} * {num2} = {result}```")
    await ctx.message.delete()

@bot.command()
async def ddiv(ctx, num1: float, num2: float):
    if num2 == 0:
        await ctx.send("```ERROR >> Cannot divide by zero```")
        await ctx.message.delete()
        return
    result = num1 / num2
    await ctx.send(f"```{num1} / {num2} = {result}```")
    await ctx.message.delete()
@bot.command()
async def h(ctx):
    response = """
``` .d8888b.        d8888 888      .d8888b.         .d8888b.  888888b.   
d88P  Y88b      d88888 888     d88P  Y88b       d88P  Y88b 888  "88b  
888    888     d88P888 888     888    888       Y88b.      888  .88P  
888           d88P 888 888     888               "Y888b.   8888888K.  
888          d88P  888 888     888                  "Y88b. 888  "Y88b 
888    888  d88P   888 888     888    888 888888      "888 888    888 
Y88b  d88P d8888888888 888     Y88b  d88P       Y88b  d88P 888   d88P 
 "Y8888P" d88P     888 88888888 "Y8888P"         "Y8888P"  8888888P"```
## CALC Commands
==============================

    > $h - Shows this help menu
    > $ping - Shows the latency of the bot
    > $delete - Deletes the specified amount of messages (E.G, $delete 5)
    > $add - Adds two numbers (E.G, $add 26 24)
    > $dadd - Adds two decimal numbers (E.G, $dadd 26.5 24.5)
    > $sub - Subtracts two numbers (E.G, $sub 100 50)
    > $dsub - Subtracts two decimal numbers (E.G, $dsub 100.5 50.5)
    > $mul - Multiplies two numbers (E.G, $mul 5 5)
    > $dmul - Multiples two decimal numbers (E.G, $dmul 5.5 5.5)
    > $div - Divides two numbers (E.G, $div 50 2)
    > $ddiv - Divides two decimal numbers (E.G, $ddiv 50.5 2.5)
    > $mod - Modulus of two numbers (E.G, $mod 100 50)
    > $dmod - Modulus of two decimal numbers (E.G, $dmod 100.5 50.5)
    > $sqr - Gives the square root of a number (E.G, $sqr 5000)
    > $dsqr - Gives the square root of a decimal number (E.G, $dsqr 5000.5 2)
    > $pow - Raises a number to the power of another number (E.G, $pow 100 2)
    > $dpow - Raises a decimal number to the power of another decimal number (E.G, $dpow 100.5 2.5)

==============================
Made by: @2elk (on discord)

    """
    await ctx.message.delete()
    await ctx.send(response)

if __name__ == "__main__":
    bot.run(token, bot=False)
