from random import choice
import asyncio
from pyrogram import Client
import json
import script


async def main():
    async with Client("my_account", api_id, api_hash) as app:
        await app.send_message("me", script.aaa(kudos))

if __name__=='__main__':
       
       with open("config/telegram.json","r") as telegram_api:
            data = json.load(telegram_api)
            api_id = data["api_id"]
            api_hash = data["api_hash"]
            chat_id = data["chat_id"]
            kudos = data["kudos"]
       
            asyncio.run(main())