# Spotify Mood-Based Playlist Generator
# This program allows users to create Spotify playlists based on their mood preferences.

import json
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# How to set up for spotify credentials
file_path = 'spotify_api_authentication_instructions'

try:
    with open(file_path, 'r') as spotify_api:
        # Read and print the text content of the file
        spotify_instructions = spotify_api.read()
        print("Successfully loaded Spotify API authentication instructions:")
        print(spotify_instructions)
except FileNotFoundError:
    print(f"File not found: {file_path}")
except Exception as e:
    print(f"An error occurred: {e}")

# Read configuration from config.json
with open('config.json', 'r') as config_file:
    config = json.load(config_file)

with open('config.json', 'r') as config_file:
    config = config_file.read()

with open('config.json', 'w+') as config_file:
    config_file.write(config)

# Spotify API credentials (fill your credentials here)
SPOTIFY_CLIENT_ID = '6e74bcd0bd0d4a0d989ddb10b891cad6'
SPOTIFY_CLIENT_SECRET = 'c839dfe0bd9b448b95917c273ba958f3'
SPOTIFY_REDIRECT_URI = 'http://localhost:3000/callback'

# Specify file paths and directories
PARENT_DIRECTORY = '/Users/rg/PycharmProjects/cfg-python./CFGDEGREE'
SUBDIRECTORY = '/Users/rg/PycharmProjects/cfg-python./CFGDEGREE/Assignment 2 Andreia Byda'
JSON_FILE_PATH = os.path.join(PARENT_DIRECTORY, SUBDIRECTORY, 'recommended_tracks.json')

# List of valid moods
VALID_MOODS = [
    "aggressive", "calm", "chill", "dreamy", "energetic", "excited", "groovy", "happy",
    "inspirational", "melancholic", "mellow", "motivated", "nostalgic", "peaceful",
    "playful", "reflective", "relaxed", "romantic", "sad", "upbeat"
]


# Get the user's name from input
def get_user_name():
    name = input("Enter your name: ")
    return name


# Display valid mood options to the user
def display_valid_moods():
    print("Valid moods:")
    for mood in VALID_MOODS:
        print(f"- {mood}")


# Get valid user mood input
def get_valid_user_mood(name):
    display_valid_moods()
    while True:
        if name:
            mood = input(f"Hi {name}, enter your mood choosing from the list above: ").lower()
        else:
            mood = input("Enter your mood (e.g., happy, sad, relaxed): ").lower()

        if mood not in VALID_MOODS:
            print("Invalid mood. Please enter a valid mood from the list.")
        else:
            return mood


# Authenticate with the Spotify API
def authenticate_spotify():
    try:
        spotify_client = spotipy.Spotify(
            auth_manager=SpotifyOAuth(
                client_id=SPOTIFY_CLIENT_ID,
                client_secret=SPOTIFY_CLIENT_SECRET,
                redirect_uri=SPOTIFY_REDIRECT_URI,
                scope='user-library-read playlist-modify-public'
            )
        )
        return spotify_client
    except Exception as e:
        print(f"Error authenticating with Spotify API: {e}")
        return None


# Search for tracks based on user preferences
def search_tracks(spotify_client, mood):
    result = spotify_client.search(q=f'mood:{mood}', type='track', limit=10)
    return result


# Create a new playlist or add tracks to an existing playlist
def create_playlist(spotify_client, user_identifier, mood, track_uri):
    playlist_name = f'Mood-Based Playlist ({mood})'
    recommended_playlist = spotify_client.user_playlist_create(user_identifier, name=playlist_name, public=True)
    spotify_client.playlist_add_items(recommended_playlist['id'], track_uri)
    return recommended_playlist


# Get the release year of a track
def get_track_release_year(spotify_client, track_id):
    try:
        track_info = spotify_client.track(track_id)
        if 'album' in track_info and 'release_date' in track_info['album']:
            release_date = track_info['album']['release_date']
            return release_date.split('-')[0]  # Extract the year from the release date
    except Exception as e:
        print(f"Error getting track release year: {e}")
    return None


# Display recommended tracks and save them to a JSON file
def display_and_save_recommendations(result, spotify_client):
    recommended_tracks = []

    print("Recommended tracks:")
    for track in result['tracks']['items']:
        track_name = track['name'][:20]

        track_info = {
            'name': track_name,
            'artists': [artist['name'] for artist in track['artists']]
        }

        track_id = track['id']
        release_year = get_track_release_year(spotify_client, track_id)
        if release_year:
            track_info['release_year'] = release_year

        recommended_tracks.append(track_info)
        print(
            f"{track_info['name']} by {', '.join(track_info['artists'])} "
            f"({release_year if release_year else 'Unknown'})"
        )

    try:
        with open(JSON_FILE_PATH, 'w') as json_file:
            json.dump(recommended_tracks, json_file, indent=4)
    except Exception as e:
        print(f"Error saving the file: {e}")
    else:
        print("File saved successfully.")

    playlist_url = f"https://open.spotify.com/playlist/{playlist['id']}"
    print(f"You can listen to your recommended playlist here: {playlist_url}")


if __name__ == "__main__":
    sp = authenticate_spotify()
    user_id = sp.me()['id']
    user_name = get_user_name()
    user_mood = get_valid_user_mood(user_name)

    print(f"Searching for tracks with mood: {user_mood}")

    results = search_tracks(sp, user_mood)

    print(f"Received {len(results['tracks']['items'])} results")

    if len(results['tracks']['items']) == 0:
        print("No results found. Please try a different mood.")
    else:
        track_uris = [track['uri'] for track in results['tracks']['items']]
        playlist = create_playlist(sp, user_id, user_mood, track_uris)
        display_and_save_recommendations(results, sp)
