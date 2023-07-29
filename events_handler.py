import requests
from Singleton import Singleton

env=Singleton.getEnvInstance();

def sendMsg(reqParam):
    requests.get(env.get('DEFAULT','telegram_baseurl')+env.get('DEFAULT','bot_token')+"/sendMessage",data=reqParam)
    