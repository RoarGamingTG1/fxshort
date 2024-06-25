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

# Function to send a welcome message and task links
async def send_welcome_message(message):
    welcome_message = "Welcome to FxShort Upi Earning! PPC 500 🌟"
    sent_message = await message.reply_text(welcome_message)

    # Wait for 15 seconds before sending task links
    await asyncio.sleep(15)
    await sent_message.delete()

    # Send task links
    await send_task_links(message)

# Function to send task links
async def send_task_links(message):
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

    # After tasks are completed, show buttons for withdrawal and refer a friend
    await show_completion_buttons(message)

# Function to show completion buttons
async def show_completion_buttons(message):
    completion_message = "Tasks completed! What would you like to do next?"
    completion_buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton("Withdrawal", callback_data="withdrawal"),
                InlineKeyboardButton("Refer a Friend", url="https://t.me/share/url?url=https://t.me/FxShortBot&text=Join @FxShortBot to earn rewards!")
            ]
        ]
    )
    await message.reply_text(completion_message, reply_markup=completion_buttons)

# Function to handle button clicks
@app.on_callback_query(filters.regex("^withdrawal$"))
async def handle_withdrawal_button(client, callback_query):
    await callback_query.answer()

    # Ask for UPI payment ID
    upi_message = await callback_query.message.reply_text("Please enter your UPI payment ID:")

    # Listen for the user's response
    async def validate_upi_id():
        try:
            response = await app.listen(callback_query.message.chat.id, timeout=120)
            upi_id = response.text.strip()

            # Confirm the UPI ID and process the withdrawal
            await upi_message.delete()
            await response.delete()
            confirmation_message = f"Your UPI payment ID ({upi_id}) has been received. Processing your withdrawal. You will receive your reward within 2 hours."
            await callback_query.message.reply_text(confirmation_message)

        except asyncio.TimeoutError:
            await callback_query.message.reply_text("You took too long to respond. Please start again if you wish to withdraw.")

    await validate_upi_id()

# Main message handling function
@app.on_message(filters.command("start"))
async def handle_start_command(client, message):
    await send_welcome_message(message)

# Run the bot
app.run()
                                   
