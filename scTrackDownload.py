# 1. create a 'downloads' folder in same directory as this file
# 2. get track url from soundcloud (go to track's page) -> paste url
# 3. click file -> opens in itunes -> enjoy! 

## pip3 install soundcloud-lib
import asyncio
from sclib.asyncio import SoundcloudAPI, Track, Playlist

api = SoundcloudAPI()  

async def get_track():
    track = await api.resolve('https://soundcloud.com/casso-wav/prada') ### !! paste song url
    assert type(track) is Track
    return track


async def write_track_to_file(track, filename):
    with open(filename, 'wb+') as file:
        await track.write_mp3_to(file)

track = asyncio.run(get_track())
filename = f'./downloads/{track.artist} - {track.title}.mp3'
asyncio.run(write_track_to_file(track, filename)) ### file will be saved in 'downloads' folder in currect directory


