import os
import asyncio
from sclib.asyncio import SoundcloudAPI, Track, Playlist

api = SoundcloudAPI()

async def get_playlist(url):
    playlist = await api.resolve(url)
    assert type(playlist) is Playlist
    return playlist

async def write_track_to_file(track, filename):
    with open(filename, 'wb+') as file:
        await track.write_mp3_to(file)

async def download_playlist(url):
    playlist = await get_playlist(url)
    # Create 'downloads' directory if it doesn't exist
    if not os.path.exists('./downloads'):
        os.makedirs('./downloads')
    
    for track in playlist.tracks:
        filename = f'./downloads/{track.artist} - {track.title}.mp3'
        await write_track_to_file(track, filename)
        print(f'Downloaded: {filename}')

# Replace with your playlist URL
playlist_url = 'https://soundcloud.com/your_playlist_url'
asyncio.run(download_playlist(playlist_url))