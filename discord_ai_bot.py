# File: discord_ai_bot.py

import discord
from discord.ext import commands
import openai
import os

# Set up OpenAI API Key
from dotenv import load_dotenv
load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")

if not openai.api_key:
    raise ValueError("OpenAI API key not found. Set it as an environment variable.")

# Initialize Discord Bot
intents = discord.Intents.default()
intents.messages = True
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

# Event: Bot is ready
@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

# Command: AI chat
@bot.command()
async def chat(ctx, *, message: str):
    try:
        # Query GPT model
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # Use GPT-4 if available
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                {"role": "user", "content": message}
            ]
        )
        # Extract and send AI response
        reply = response['choices'][0]['message']['content']
        await ctx.send(reply)
    except Exception as e:
        await ctx.send("Sorry, I couldn't process that. Try again later.")
        print(f"Error: {e}")

# Run the bot
bot.run("MTMxMDY1MDUwNDA3ODE2NDA2OA.GcgsIh.uiR0e5eMDP13Wc96JmlORFBBI_AWUUL9Oh5Njw")
