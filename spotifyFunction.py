import requests
import json
import base64

def get_userplaylist(TOKEN,user_id):

    query = "https://api.spotify.com/v1/me/playlists"


    response = requests.get(
        query,
        headers={
            "Content-Type": "discordIntegration/json",
            "Authorization": "Bearer {}".format(TOKEN)
        }
    )
    response_json = response.json()
    return response_json



def create_playlist(TOKEN,user_id):
    request_body = json.dumps({
        "name": "Weenie Bot Playlist",
        "description": "The official Weenie Butt General PLaylist",
        "public": False
    })

    query = "https://api.spotify.com/v1/users/{}/playlists".format(user_id)
    response = requests.post(
        query,
        data=request_body,
        headers={
            "Content-Type": "discordIntegration/json",
            "Authorization": "Bearer {}".format(TOKEN)
        }
    )
    response_json = response.json()

    # playlist id
    return response_json["id"]

def getURI(TOKEN, user_id, song_name, artist):
    query = "https://api.spotify.com/v1/search?query=track%3A{}+artist%3A{}&type=track&offset=0&limit=20".format(
        song_name,
        artist
    )
    response = requests.get(
        query,
        headers={
            "Content-Type": "discordIntegration/json",
            "Authorization": "Bearer {}".format(TOKEN)
        }
    )
    response_json = response.json()
    songToAdd = response_json["tracks"]["items"]

    if songToAdd == []:
        id = 0

    else:
        id = songToAdd[0]["uri"]

    return id

def AddSong(TOKEN, songToAdd, playListID):

    query = "https://api.spotify.com/v1/playlists/{}/tracks".format(playListID)
    response = requests.post(
        query,
        json={
            "uris": [songToAdd]
        },
        headers={
            "Content-Type": "discordIntegration/json",
            "Authorization": "Bearer {}".format(TOKEN)
        }

    )
    response_json = response.json()

    return response_json

def getItems(TOKEN, user_id, Plist):
    query = "https://api.spotify.com/v1/playlists/{}/tracks".format(Plist)

    response = requests.get(
        query,
        headers={
            "Content-Type": "discordIntegration/json",
            "Authorization": "Bearer {}".format(TOKEN)
        }
    )
    response_json = response.json()
    items = response_json
    return items

def removePlaylist(TOKEN,Plist):
    query = "https://api.spotify.com/v1/playlists/{}/followers".format(Plist)
    response = requests.delete(
        query,
        headers={
            "Content-Type": "discordIntegration/json",
            "Authorization": "Bearer {}".format(TOKEN)
        }
    )

def authorize(client_secret):
    query = "https://accounts.spotify.com/authorize"

    reponse = requests.post(
        query,
        json={
            "client_id": [client_secret],
            "response_type": "token",
            "redirect_uri": "http://192.168.0.4" 
        },
        headers={
            "content-type": "discordintegration/json",
       
        }
        
        )
    response_json = response.json()
    return response_json

def requestAuthorization(REFRESH_TOKEN,CLIENT_ID,CLIENT_SECRET):
    query = "https://accounts.spotify.com/api/token"
    method = "POST"
    client_creds = f"{CLIENT_ID}:{CLIENT_SECRET}"
    client_creds64 = base64.b64encode(client_creds.encode())
    token_data = {
        "grant_type": "client_credentials"

        }
    tHeader = {
        "Authorization": f"Basic {client_creds64.decode()}",
        }

    response = requests.post(
        query,
        data=token_data,
        headers = tHeader
        
        )

    response_json = response.json()

    return response_json

def refreshAuthorization(REFRESH_TOKEN,CLIENT_ID,CLIENT_SECRET):
    query = "https://accounts.spotify.com/api/token"
    method = "POST"
    client_creds = f"{CLIENT_ID}:{CLIENT_SECRET}"
    client_creds64 = base64.b64encode(client_creds.encode())
    
    token_data = {
        "grant_type": "refresh_token",
        "refresh_token": REFRESH_TOKEN,
        

        }
    tHeader = {
        "Authorization": f"Basic {client_creds64.decode()}"
        }

    response = requests.post(
        query,
        data=token_data,
        headers = tHeader
        
        )

    response_json = response.json()

    return response_json

def playlist_songs(playList,STOKEN):
    query = "https://api.spotify.com/v1/playlists/{}/tracks".format(playList)

    response = requests.get(
        query,
        headers={
            "Content-Type": "discordIntegration/json",
            "Authorization": "Bearer {}".format(STOKEN)
        }
    )

    response_json = response.json()
    
    return response_json


