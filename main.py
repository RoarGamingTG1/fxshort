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

    # Add a message handler for the account number
    @app.on_message(filters.text & filters.reply & filters.user(message.from_user.id) & ~filters.me)
    async def validate_account_number(client, response):
        account_number = response.text

        if (len(account_number) == 11 and account_number.isdigit()) or (len(account_number) == 13 and account_number.startswith('+91') and account_number[1:].isdigit()):
            await account_message.delete()
            await response.delete()
            await send_links(message)
        else:
            error_message = await message.reply_text("Invalid account number. Please enter an 11-digit Upi account number or a +92 format phone number:")

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
    
    # Final message with the share button
    final_message = "Task completed! Reward 🎉 will be sent after you invite 2 friends to @FxShortBot 🌟"
    share_button = InlineKeyboardMarkup(
        [
            [InlineKeyboardButton("Share with friends", url="https://t.me/share/url?url=https://t.me/FxShortBot&text=Join @FxShortBot to earn rewards!")]
        ]
    )
    await message.reply_text(final_message, reply_markup=share_button)

# Main message handling function
@app.on_message(filters.text & ~filters.me)
async def handle_messages(client, message):
    if "start" in message.text.lower():
        await send_welcome_message(message)

# Run the bot
app.run()
