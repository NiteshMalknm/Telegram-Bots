from telethon.sync import TelegramClient,events


api_id = 21830791
api_hash = '041e0a1089a469a80ca4cc5d9c46196a'
bot_token = '5918508248:AAHQeXJGa_UbhwqCHs7RH8jGniGIHCBeGAM'


client = TelegramClient('app', api_id, api_hash)


@client.on(events.NewMessage(outgoing=True, pattern=r'\/audio'))
async def handler(event):
    print(event)
    
with client:
    client.start()
    client.run_until_disconnected()
