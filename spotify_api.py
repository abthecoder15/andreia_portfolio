import requests
from config import CLIENT_ID, CLIENT_SECRET


# # Spotify API credentials
# CLIENT_ID = 'insert your client ID'
# CLIENT_SECRET = 'insert your client secret'


# Function to retrieve access token
def get_access_token():
    token_url = 'https://accounts.spotify.com/api/token'
    response = requests.post(token_url, data={
        'grant_type': 'client_credentials',
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
    })
    token_data = response.json()
    return token_data.get('access_token')


# Function to search for an artist
def search_artist(artist_name, access_token):
    search_url = f'https://api.spotify.com/v1/search?q={artist_name}&type=artist'
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(search_url, headers=headers)
    data = response.json()
    artist = data['artists']['items'][0] if data['artists']['items'] else None
    return artist


# Function to retrieve an artist's albums
def get_artist_albums(artist_id, access_token):
    albums_url = f'https://api.spotify.com/v1/artists/{artist_id}/albums'
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(albums_url, headers=headers)
    albums_data = response.json()

    albums = albums_data.get('items', [])

    for album in albums:
        album['tracks'] = get_album_tracks(album['id'], access_token)
        album['release_year'] = album.get('release_date', '')[:4]

    return albums


# Function to retrieve album tracks
def get_album_tracks(album_id, access_token):
    tracks_url = f'https://api.spotify.com/v1/albums/{album_id}/tracks'
    headers = {'Authorization': f'Bearer {access_token}'}
    response = requests.get(tracks_url, headers=headers)
    tracks_data = response.json()
    return tracks_data.get('items', [])


# Main function
def main():
    artist_name = input("Enter artist name: ")
    access_token = get_access_token()

    artist = search_artist(artist_name, access_token)

    if artist:
        artist_id = artist['id']
        albums = get_artist_albums(artist_id, access_token)

        if not albums:
            print(f"No albums found for {artist_name}.")
        else:
            print(f"Albums by {artist_name}:")
            for album in albums:
                print(f"Album: {album['name']} ({album['release_year']})")
                if 'tracks' in album:
                    print("Tracks:")
                    for track in album['tracks']:
                        print(f"- {track['name']}")
                print("=" * 40)
    else:
        print(f"Artist {artist_name} not found.")


if __name__ == '__main__':
    main()
