import os
import random
import asyncio
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Bot credentials
BOT_TOKEN = os.environ.get("BOT_TOKEN")
API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")

# Create Pyrogram client
app = Client("Mining_Bot", bot_token=BOT_TOKEN, api_id=API_ID, api_hash=API_HASH)

# Function to send threatening reply with random dangerous messages
async def send_dangerous_reply(message):
    dangerous_messages = [
        "Mining Shuru Kren Aaj Se Hi! ⛏️😄",
        "Mining mein zindagi banaayein! 💎🚀",
        "Gold digging ki tarah, bas ghar baithe! 🏡💰",
        "Mining karein, sapne sajayein! 🌟⛏️",
        "Bitcoin mine kar ke millionaire banein! 🤑💸",
        "Chalo mining karne ka maza lo! 🎉⛏️",
        "Khudai karen, paisa banayein! 💵🔍",
        "Zameen ke neche chhupe khazaane dhoondein! 🗺️⛏️",
        "Digital sona dhoondhna shuru karein! 📲💎",
        "Aaj se mining, kal se Lamborghini! 🏎️💨"
    ]

    reply = random.choice(dangerous_messages)
    sent_message = await message.reply_text(reply)

    # Wait for 45 seconds before deleting the message
    await asyncio.sleep(45)

    # Delete the sent message
    await sent_message.delete()

# Function to send a series of 8 messages
async def send_series_of_messages(message):
    messages = [
        {
            "text": "MiningBot 1: Earn through Hamster Kombat Play",
            "url": "https://t.me/Hamster_kombat_bot/start?startapp=kentId6298865570",
            "image": "https://telegra.ph/file/1def17f220265924b3dc4.jpg"
        },
        {
            "text": "MiningBot 2: WCoin Play - Real Mining Earnings",
            "url": "https://t.me/wcoin_tapbot?start=NjI5ODg2NTU3MA==",
            "image": "https://telegra.ph/file/a8812258116b187b94eda.jpg"
        },
        {
            "text": "MiningBot 3: Earn with MemeFi Play",
            "url": "https://t.me/memefi_coin_bot?start=r_d9aa24376d",
            "image": "https://telegra.ph/file/d559e5d7915081ea2eb1c.jpg"
        },
        {
            "text": "MiningBot 4: YescCoin Play for Mining",
            "url": "https://t.me/yescoingame_bot?start=r_6298865570",
            "image": "https://telegra.ph/file/4cab774299246ae48c43e.jpg"
        },
        {
            "text": "MiningBot 5: Play with Gamee for Real Earnings",
            "url": "https://t.me/gamee?start=ref_6298865570",
            "image": "https://telegra.ph/file/ca27a1c86360ab20b602a.jpg"
        },
        {
            "text": "MiningBot 6: Tapswap Play - Start Mining",
            "url": "https://t.me/tapswap_mirror_bot?start=r_6298865570",
            "image": "https://telegra.ph/file/42c68116b51cd875b93a8.jpg"
        },
        {
            "text": "MiningBot 7: Earn with DotCoin Play",
            "url": "https://t.me/dotcoin_bot?start=r_6298865570",
            "image": "https://telegra.ph/file/ed844f9c4243cf73b3940.jpg"
        },
        {
            "text": "MiningBot 8: Earn With OnChain Play",
            "url": "https://t.me/onchaincoin_bot?start=user_6298865570",
            "image": "https://telegra.ph/file/c1f935787e2955e53cb5d.jpg"
        },
        {
            "text": "MiningBot 9: Near Wallet Hot 🔥 Play",
            "url": "https://t.me/onchaincoin_bot?start=user_6298865570",
            "image": "https://telegra.ph/file/0e7fc78f20344c8cd0d4e.jpg"
        },
        {
            "text": "MiningBot 10:Earn Pixel verse  🔥 Play use Vpn 1111 To Start",
            "url": "https://t.me/pixelversexyzbot?start=6298865570",
            "image": "https://telegra.ph/file/8b77aaac960815e530170.jpg"
        },
        {
            "text": "MiningBot 11:Blum 🔥 Play  Popular project 10M community 🧩⭐",
            "url": "https://t.me/BlumCryptoBot/start?startapp=ref_79sRdOH69z",
            "image": "https://telegra.ph/file/6146a1fbca7c1ec64c7b2.jpg"
        },
        {
            "text": "MiningBot 12: 💎 Gemz bot 🔥 Play  Same Hamster 🐹 Project",
            "url": "https://t.me/gemzcoin_bot/start?startapp=6sHOfy-UFUMjJM2bVfjN9PFc",
            "image": "https://telegra.ph/file/1ac74b321a1375dfdcba9.jpg"
        },
        {
            "text": "MiningBot 13:Mini Ton Play ⏯️",
            "url": "https://t.me/mini_ton_bot?start=6298865570",
            "image": "https://telegra.ph/file/4e8b8f960550e55eea5d5.jpg"
        }
    ]

    for msg in messages:
        reply_markup = InlineKeyboardMarkup(
            [[InlineKeyboardButton("Click Here To Mine ⭐", url=msg["url"])]]
        )
        sent_message = await message.reply_photo(
            photo=msg["image"],
            caption=msg["text"],
            reply_markup=reply_markup
        )

        # Wait for a short period before sending the next message
        await asyncio.sleep(3)

# Function to send intro message and then a series of messages
async def send_intro_message(message):
    intro_message = (
        "Friends! "
        "Yahan aapko mining se related sab kuch milega. Neeche diye gaye links ko follow karke mining start karein aur earning shuru kren. Aapne mining karni hai aur apne coins badhane hain. Jab inki listing hogi to apko acha profit milega 😊. Kuch log bolte hain samajh nahi aati 🙆 mining ki. Jab tak koi kaam start nahi karoge tab tak samajh nahi aayegi. To apna time mat barbad karein. Aaj se hi start karein 🥰🥰"
    )
    sent_message = await message.reply_text(intro_message)

    # Wait for 10 seconds before deleting the intro message
    await asyncio.sleep(15)

    # Delete the sent message
    await sent_message.delete()

    # Send the series of messages
    await send_series_of_messages(message)

# Main message handling function
@app.on_message(filters.text & ~filters.me)
async def handle_messages(client, message):
    if "start" in message.text.lower():
        await send_intro_message(message)
    else:
        trigger_words = [
            "hi", "hello", "bot", "how", "😒",
            "inbox", "dm", "ban", "😁", "banggfcxxx",
            "halgggccl", "hoggfffw", "mevgvvffcccc", "togvcccccxxxx"
        ]
        question = message.text.lower()
        for word in trigger_words:
            if word in question:
                await send_dangerous_reply(message)
                break

# Run the bot
app.run()

    
