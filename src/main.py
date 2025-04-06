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
import threading
import customtkinter as ctk
from dotenv import load_dotenv
import win32gui
import win32con
import ctypes
from pyfiglet import Figlet

load_dotenv()
token = os.getenv('DISCORD_TOKEN')
bot = commands.Bot(command_prefix="$", self_bot=True, intents=discord.Intents.default())

def hide_console():
    console_window = win32gui.GetForegroundWindow()
    win32gui.ShowWindow(console_window, win32con.SW_HIDE)
    kernel32 = ctypes.WinDLL('kernel32')
    user32 = ctypes.WinDLL('user32')
    SW_HIDE = 0
    hWnd = kernel32.GetConsoleWindow()
    if hWnd:
        user32.ShowWindow(hWnd, SW_HIDE)

def create_gui():

    hide_console()
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("dark-blue")
    

    window = ctk.CTk()
    window.title("CALC-SB PRO")
    window.geometry("800x600")
    window.minsize(800, 600)
    window.resizable(False, False)
    window._set_appearance_mode("dark")

    main_container = ctk.CTkFrame(
        window,
        fg_color=("#1a1625", "#0d0714"),
        corner_radius=20
    )
    main_container.pack(fill="both", expand=True, padx=20, pady=20)
    

    header_frame = ctk.CTkFrame(
        main_container,
        fg_color=("#2d1f42", "#1a1228"),
        corner_radius=15,
        height=60
    )
    header_frame.pack(fill="x", padx=15, pady=(15, 5))
    

    title_label = ctk.CTkLabel(
        header_frame, 
        text="                               Calculator-Selfbot PRO",
        font=("Segoe UI", 24, "bold"),
        text_color="#c4b5fd"
    )
    title_label.pack(side="left", padx=20, pady=10)


    content_frame = ctk.CTkFrame(
        main_container,
        fg_color=("#2d1f42", "#1a1228"),
        corner_radius=15,
        border_width=2,
        border_color="#7c3aed",
        width=465,
        height=250
    )
    content_frame.pack(fill="both", expand=True, padx=15, pady=15)
    
    
    
    text_box = ctk.CTkTextbox(
        content_frame,
        width=465,
        height=250,
        fg_color=("#1a1625", "#0d0714"),
        text_color="#c4b5fd",
        font=("Consolas", 12)
    )
    text_box.pack(padx=20, pady=20)


    figlet = Figlet(font="slant")
    ascii_art = figlet.renderText("CALC-Selfbot")
    lines = ascii_art.split("\n")
    max_length = max(len(line) for line in lines)
    
   
    text_box.insert("end", "\n" * 2)
    
  
    for line in lines:
        spaces = " " * ((max_length - len(line)) // 2)
        text_box.insert("end", f"{spaces}{line}\n")
    
   
    text_box.insert("end", f"                   C O N N E C T E D >> {bot.user}")
 
    text_box.configure(state="disabled")

    footer_frame = ctk.CTkFrame(
        main_container,
        fg_color=("#2d1f42", "#1a1228"),
        corner_radius=15,
        width=465,
        height=250
    )
    footer_frame.pack(fill="x", padx=15, pady=(5, 15))

    status_label = ctk.CTkLabel(
        footer_frame,
        text="● Online",
        font=("Segoe UI", 12),
        text_color="#4ade80"
    )
    status_label.pack(side="left", padx=20)

    # Add modern controls hint
    controls_label = ctk.CTkLabel(
        footer_frame,
        text="Press Alt + F4 to exit",
        font=("Segoe UI", 12),
        text_color="#94a3b8"
    )
    controls_label.pack(side="right", padx=20)

    # Add version badge
    version_label = ctk.CTkLabel(
        footer_frame,
        text="v2.0 Pro",
        font=("Segoe UI", 12, "bold"),
        text_color="#7c3aed"
    )
    version_label.pack(side="right", padx=20)

    return window
@bot.event
async def on_ready():
    def run_gui():
        hide_console()
        window = create_gui()
        window.mainloop()
    
    threading.Thread(target=run_gui, daemon=True).start()
    
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
    await ctx.message.delete()
    response = await ctx.send(f"```{num1} + {num2} = {num1 + num2}```")
    await ctx.message.delete()
    await ctx.send(response)

@bot.command()
async def sub(ctx, num1: int, num2: int):
    await ctx.message.delete()
    response = await ctx.send(f"```{num1} - {num2} = {num1 - num2}```")
    await ctx.message.delete()
    await ctx.send(response)

@bot.command()
async def mul(ctx, num1: int, num2: int):
    await ctx.message.delete()
    response = await ctx.send(f"```{num1} * {num2} = {num1 * num2}```")
    await ctx.message.delete()
    await ctx.send(response)

@bot.command()
async def div(ctx, num1: int, num2: int):
    await ctx.message.delete()
    if num2 == 0:
        response = await ctx.send("```ERROR >> Cannot divide by zero```")
        await asyncio.sleep(2)
        await response.delete()
        return
    response = await ctx.send(f"```{num1} / {num2} = {num1 / num2}```")
    await ctx.message.delete()
    await ctx.send(response)

@bot.command()
async def dadd(ctx, num1: float, num2: float):
    await ctx.message.delete()
    response = await ctx.send(f"```{num1} + {num2} = {num1 + num2}```")
    await ctx.message.delete()
    await ctx.send(response)

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
