import os
import base64
from requests import *
import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import webbrowser
import socket

CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET_ID")
REDIRECT_URI = "http://127.0.0.1:8888/callback"
DEVICE_ID = "0f348876be4039d2be563b51db04117b236c9acb"
PLAYLIST_ID = "7zinWTOXGzANeThWROxTCC"
scope = "user-modify-playback-state user-read-playback-state"

# Start a simple web server to handle the redirect
try:
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('127.0.0.1', 8888))
    server_socket.listen(1)
except socket.error as e:
    print(f"Error starting local server: {e}")
    exit()

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=CLIENT_ID,
                                               client_secret=CLIENT_SECRET,
                                               redirect_uri=REDIRECT_URI,
                                               scope=scope,
                                               open_browser=False))  # Set open_browser=False

# print(sp.devices())
# exit()
# Manually open the authorization URL in the user's browser
auth_url = sp.auth_manager.get_authorize_url()
print(f"Please open this URL in your browser: {auth_url}")
webbrowser.open(auth_url)

# Wait for the redirect and extract the authorization code
print("Waiting for authorization...")
connection, address = server_socket.accept()
data = connection.recv(1024).decode('utf-8')

code = None
if 'code=' in data:
    redirect_url = data.split(" ")[1]
    if "code=" in redirect_url:
        code_with_extras = redirect_url.split('code=')[1]
        code = code_with_extras.split('&')[0]
        print(f"Authorization code received: {code}")
    else:
        print("Authorization code not found in redirect URL.")
        exit()
else:
    print("Authorization failed.")
    exit()

# Use the code to get the access token
token_info = sp.auth_manager.get_access_token(code)
if token_info:
    sp.auth_manager.cache_handler.save_token_to_cache(token_info)
    print("Successfully authenticated!")
else:
    print("Failed to retrieve access token.")
    exit()

# Now you can use 'sp' to make API calls (e.g., play a playlist)
try:
    sp.start_playback(context_uri=f'spotify:playlist:{PLAYLIST_ID}')
    print("Playing your playlist!")
except spotipy.exceptions.SpotifyException as e:
    print(f"Error: {e}")

connection.close()
server_socket.close()