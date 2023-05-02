import asyncio
from pyrogram import Client

api_id = 1347918
api_hash = "5681581438678d9390cd4f67ee764f82"



async def main():
    async with Client("my_account", api_id, api_hash) as app:
        await app.send_message("me", "Greetings from **Pyrogram**!")


asyncio.run(main())