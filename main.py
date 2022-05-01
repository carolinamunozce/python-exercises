#import sqlalchemy
import pandas as pd 
#from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import datetime
import datetime
import sqlite3


DATABASE_LOCATION = ""

# Data user SP

USER_ID = "carolina.munozce"
TOKEN = "BQBTfGz4U3O2HBoT7-HWCVIT9LKX-7XIlaCKp4VOf8PfgGCH4e3TgXXf8CxhW-nRZFbr8Y3ZtZIs05qKczmJzQu21ToCfTeTjbT1u91Wbwceq_0seNZC3_2OQ__083lIRKBf_4WsxPGgGNxk3_iuA3K51EVT"

if __name__ == "__main__":
    
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {token}".format(token=TOKEN)
    }
    #Convert unix timestamp in milliseconds
    today =datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_unix_timestamp = int(yesterday.timestamp())* 1000

    # Get request from SP last 24 hours

    r = requests.get("https://api.spotify.com/v1/me/player/recently-played?after={time}".format(time=yesterday_unix_timestamp), headers = headers)

    data = r.json()
   # print (data)

    song_names = []
    artist_names = []
    played_at_list = []
    timestamps = []

    for song in data["items"]:
        song_names.append(song["track"]["name"])
        artist_names.append(song["track"]["album"]["artists"][0]["name"])
        played_at_list.append(song["played_at"])
        timestamps.append(song["played_at"][0:10])

    song_dict = {
        "song_name": song_names,
        "artist_names": artist_names,
        "played_at": played_at_list,
        "timestamps": timestamps
    }

    song_df = pd.DataFrame(song_dict, columns= ["song_name","artist_name","played_at","timestamps"])

    print (song_df)

    