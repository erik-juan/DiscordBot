import requests
import json

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
        "description": "descript",
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
