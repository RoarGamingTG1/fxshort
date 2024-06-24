import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Bot credentials
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

# Create Pyrogram client
app = Client("Mining_Bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

# Function to send a welcome message
async def send_welcome_message(message):
    welcome_message = "Welcome to FxShort Upi Earning! PPC 500 🌟"
    sent_message = await message.reply_text(welcome_message)

    # Wait for 15 seconds before asking for Easypaisa account number
    await asyncio.sleep(15)
    await sent_message.delete()

    # Ask for Easypaisa account number
    account_message = await message.reply_text("Please enter your 11-digit Upi account number or +92 format phone number:")

    # Listen for the user's response and validate the account number
    async def validate_account_number():
        try:
            response = await app.listen(message.chat.id, timeout=60)
            account_number = response.text

            # Check if the entered account number is valid
            if (len(account_number) == 11 and account_number.isdigit()) or (len(account_number) == 13 and account_number.startswith('+92') and account_number[1:].isdigit()):
                await account_message.delete()
                await response.delete()
                await send_links(message)
            else:
                error_message =

