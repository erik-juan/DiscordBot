import os
import requests
import json

STOKEN = os.getenv("SPOTIFY_TOKEN")
user_id = os.getenv("USER_ID")
print(user_id)

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


#read playlists
playlistResponse = get_userplaylist(STOKEN,user_id)
items = playlistResponse['items']
#Check if playlist already created
playlistNames = []

for keys in items:
    playlistNames.append(keys['name'])
    name = keys['name']
    if name == 'Weenie Bot Playlist':
        print(keys['id'])
        playList = keys['id']



print(playlistNames)
# if keys['name'] == 'Weenie Bot Playlist':
#     print("There is Already a Playlist")
# else:
#     pid = create_playlist(TOKEN, user_id)
#     print(pid)
#     Print("Playlist Created")
if 'Weenie Bot Playlist' in playlistNames:
    print('There is already a Play List')
    print(playList)

else:
    playList = create_playlist(STOKEN,user_id)
    print(playList)

















