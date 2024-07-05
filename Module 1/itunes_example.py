import sys
import requests
import json


def main():
    if len(sys.argv) < 2:
        print('Usage: python itunes_example.py <search term>')
        sys.exit(1)
    
    artist = sys.argv[1]

    response = requests.get(f"https://itunes.apple.com/search?entity=song&limit=1&term={artist}")
    formatted_response = json.dumps(response.json(),  indent=4)
    data = response.json()
    print(formatted_response)
    print(f"Artist : {artist}")
    print("Song Information")

    for song in data["results"]:
        print(f" - Song Name : {song['trackName']}")
        print(f" - Album : {song['collectionName']}")

main()