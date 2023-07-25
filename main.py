from telethon.sync import events
from Singleton import Singleton
import spotify_helper


client = Singleton.gettelethonInstance()


@client.on(events.NewMessage(outgoing=True, pattern=r'https\:\/\/open\.spotify\.com\/track'))
async def handler(event):
    resp=spotify-helper.getTitleArtists(event.event.raw_text)
    await event.reply(resp)
    
    
    
with client:
    client.start()
    client.run_until_disconnected()
