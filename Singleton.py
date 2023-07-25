from spotipy.oauth2 import SpotifyClientCredentials
from telethon.sync import TelegramClient
import spotipy
class Singleton:
    
    spotipyObj=None
    telethonClient=None
    api_id = 21830791
    api_hash = '041e0a1089a469a80ca4cc5d9c46196a'
    bot_token = '5918508248:AAHQeXJGa_UbhwqCHs7RH8jGniGIHCBeGAM'
    
    @staticmethod
    def getSpotipyInstance():
        if Singleton.spotipyObj is None:
            Singleton.spotipyObj=spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id='a145db3dcd564b9592dacf10649e4ed5',client_secret='389614e1ec874f17b8c99511c7baa2f6'))        
            #print("obj created")
        return Singleton.spotipyObj
        
    @staticmethod
    def gettelethonInstance():
        if Singleton.telethonClient is None:
           Singleton.telethonClient=TelegramClient('app',Singleton.api_id,Singleton.api_hash)
            #print("obj created")
        return Singleton.telethonClient
   
