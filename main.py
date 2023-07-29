from Singleton import Singleton
import spotify_helper
import time
import requests
import events_handler
from threading import Thread

env=Singleton.getEnvInstance();

def events_reader():
    offset=int(env.get('DEFAULT','offset'))
    while True:
        time.sleep(int(env.get('DEFAULT','read_msg_timeout')))
        param={"offset":offset}
        resp=requests.get(env.get('DEFAULT','telegram_baseurl')+env.get('DEFAULT','bot_token')+"/getUpdates",param)
        resp=resp.json()
        print('Number of msg '+str(len(resp["result"]))+' in current cycle')
        if len(resp["result"]) != 0:
            for result in resp["result"]:
                if result["message"]["text"] == 'hi':
                        reqParam={
                                "chat_id":result["message"]["chat"]["id"],
                                "text":"Hello"
                        }
                        print(reqParam)
                        events_handler.sendMsg(reqParam)
                        
                elif result["message"]["text"] == '/Start':
                        Thread(target = msgStart, args = (result,)).start()
                elif result["message"]["text"].startswith('https://open.spotify.com/track'):
                        Thread(target = msgSpotifyLink, args = (result,)).start()
            offset=resp["result"][-1]["update_id"] + 1
        
        
        
        

        
        
def msgStart(result):
    reqParam={
              "chat_id":result["message"]["chat"]["id"],
              "text":"Welcome to SpotyMusic Bot\n This Bot help you to download song from spoity\n Just Share me spotify music link"
             }
    events_handler.sendMsg(reqParam)
    
def msgSpotifyLink(result):
    resp=spotify_helper.getTitleArtists(result["message"]["text"])
    reqParam={
             "chat_id":result["message"]["chat"]["id"],
              "text":resp,
              "reply_to_message_id":result["message"]["message_id"]
             }
    events_handler.sendMsg(reqParam)
    
    
    
events_reader()