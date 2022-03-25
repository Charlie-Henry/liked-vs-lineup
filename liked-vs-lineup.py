# Shows a user's saved tracks (need to be authenticated via oauth)

import os

from dotenv import load_dotenv
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd

# CSV of lineup
lineup = pd.read_csv("edc2022.csv")

scope = 'user-library-read'

# Envriomnent variables
load_dotenv("spotify.env")

YOUR_APP_CLIENT_ID = os.environ.get("YOUR_APP_CLIENT_ID")
YOUR_APP_CLIENT_SECRET = os.environ.get("YOUR_APP_CLIENT_SECRET")
YOUR_APP_REDIRECT_URI = os.environ.get("YOUR_APP_REDIRECT_URI")

def show_tracks(results):
    for item in results['items']:
        track = item['track']
        print("%32.32s %s" % (track['artists'][0]['name'], track['name']))


sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=YOUR_APP_CLIENT_ID,
                                               client_secret=YOUR_APP_CLIENT_SECRET,
                                               redirect_uri=YOUR_APP_REDIRECT_URI,
                                               scope=scope))

results = sp.current_user_saved_tracks()

while results['next']:
    results = sp.next(results)
    
    # Go through each spotify Artist and compare to lineup
    for idx, item in enumerate(results['items']):
        track = item['track']
        curr_artist = track['artists'][0]['name']
        search_df = lineup['Band'].str.match(curr_artist.upper(),case=False)
        if not lineup[search_df].empty: 
            print(f"Found Artist: {lineup[search_df]['Band'].iloc[0]}")

            
    
