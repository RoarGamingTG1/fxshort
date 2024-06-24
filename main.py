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
    account_message = await message.reply_text("Please enter your 11-digit Upi account number:")

    # Wait for the user's response and validate the account number
    async def validate_account_number():
        response = await app.listen(message.chat.id, timeout=60)
        account_number = response.text

        if len(account_number) == 11 and account_number.isdigit():
            await account_message.delete()
            await response.delete()
            await send_links(message)
        else:
            error_message = await message.reply_text("Invalid account number. Please enter an 11-digit Upi Number:")
            await validate_account_number()

    await validate_account_number()

# Function to send links
async def send_links(message):
    messages = [
        {
            "text": "TasK 1 Complete Join This To Complete ",
            "url": "https://t.me/Hamster_kombat_bot/start?startapp=kentId6298865570",
            "image": "https://telegra.ph/file/2b7c09dae3d436795fe73.jpg"
        },
        {
            "text": "TasK 2 Complete Join This To Complete",
            "url": "https://t.me/herewalletbot/app?startapp=8958752",
            "image": "https://telegra.ph/file/23d2548eff2b5a98ac8ff.jpg"
        }
    ]

    for msg in messages:
        reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Click Here To Earn ⭐", url=msg["url"])]]
        )
        sent_message = await message.reply_photo(
            photo=msg["image"],
            caption=msg["text"],
            reply_markup=reply_markup
        )

        # Wait for a short period before sending the next message
        await asyncio.sleep(3)

    # Wait for 60 seconds before sending task completion message
    await asyncio.sleep(60)
    await message.reply_text("Task completed! Reward 🎉 will be Sent Your Account in 24 hours 🌟 Stay Share With Friends To Earn More Chances 🏪")

# Main message handling function
@app.on_message(filters.text & ~filters.me)
async def handle_messages(client, message):
    if "start" in message.text.lower():
        await send_welcome_message(message)

# Run the bot
app.run()
