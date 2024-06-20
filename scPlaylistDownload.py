## this will downlaod all downloadable songs within a playlist to a folder named after your playlist

import os
import asyncio
from sclib.asyncio import SoundcloudAPI, Track, Playlist

api = SoundcloudAPI()

class UnsupportedFormatError(Exception):
    pass

async def get_playlist(url):
    playlist = await api.resolve(url)
    assert type(playlist) is Playlist
    return playlist

async def write_track_to_file(track, filename):
    with open(filename, 'wb+') as file:
        await track.write_mp3_to(file)
        
        
async def download_playlist(url):
    playlist = await get_playlist(url)
    playlist_dir = f'./playlist_downloads/{playlist.title}' # create directory named after the playlist if it doesn't exist
    if not os.path.exists(playlist_dir):
        os.makedirs(playlist_dir)
    
    for track in playlist.tracks:
        trackname = f'{track.artist} - {track.title}'
        filename = f'{playlist_dir}/{track.artist} - {track.title}.mp3'
        try:
            # attempt to get the stream URL to check if the track is downloadable
            stream_url = await track.get_stream_url()
            if not stream_url:
                raise UnsupportedFormatError("Track is not downloadable")
            await write_track_to_file(track, filename)
                # print nothing if successfully downloads
        except UnsupportedFormatError:
            print(f'Skipped: {trackname} Unsupported format')
        except Exception as e:
            print(f'Error downloading {trackname}: Unsupported HLS stream format')

# !! replace with your playlist URL
playlist_url = 'https://soundcloud.com/declank10/sets/the-boats-darty/s-8hp3T6ZT0wH?si=ac83ad6bb1004b388f02bdb9f7e8e83c&utm_source=clipboard&utm_medium=text&utm_campaign=social_sharing'
asyncio.run(download_playlist(playlist_url))




# previous attempts to try to ignore [unsupported download error]
"""
async def download_playlist(url):
    playlist = await get_playlist(url)
    # Create 'downloads' directory if it doesn't exist
    if not os.path.exists('./downloads'):
        os.makedirs('./downloads')
    
    for track in playlist.tracks:
        filename = f'./downloads/{track.artist} - {track.title}.mp3'
        await write_track_to_file(track, filename)
        print(f'Downloaded: {filename}')
        
        
        
async def download_playlist(url):
    playlist = await get_playlist(url)
    # Create 'downloads' directory if it doesn't exist
    if not os.path.exists('./downloads'):
        os.makedirs('./downloads')
    
    for track in playlist.tracks:
        filename = f'./downloads/{track.artist} - {track.title}.mp3'
        try:
            if not track.downloadable:
                raise UnsupportedFormatError("Track is not downloadable")
            await write_track_to_file(track, filename)
            print(f'Downloaded: {filename}')
        except UnsupportedFormatError:
            print(f'Skipped: {filename} (Unsupported format)')


async def download_playlist(url):
    playlist = await get_playlist(url)
    # Create 'downloads' directory if it doesn't exist
    if not os.path.exists('./downloads'):
        os.makedirs('./downloads')
    
    for track in playlist.tracks:
        filename = f'./downloads/{track.artist} - {track.title}.mp3'
        try:
            # Check if the track has a download URL or stream URL
            if not hasattr(track, 'download_url') and not hasattr(track, 'stream_url'):
                raise UnsupportedFormatError("Track is not downloadable")
            await write_track_to_file(track, filename)
            print(f'Downloaded: {filename}')
        except UnsupportedFormatError:
            print(f'Skipped: {filename} (Unsupported format)')
"""