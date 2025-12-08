#!/usr/bin/env python3
"""Find all re:Invent 2025 playlists from AWS Events channel."""
import os
from dotenv import load_dotenv
from googleapiclient.discovery import build

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
CHANNEL_ID = 'UCdoadna9HFHsxXWhafhNvKw'  # AWS Events Channel

def get_youtube_service():
    return build('youtube', 'v3', developerKey=GOOGLE_API_KEY)

def get_all_playlists(youtube, channel_id):
    """Get all playlists from a channel."""
    playlists = []
    next_page = None
    
    while True:
        request = youtube.playlists().list(
            part='snippet',
            channelId=channel_id,
            maxResults=50,
            pageToken=next_page
        )
        response = request.execute()
        
        for item in response['items']:
            playlists.append({
                'id': item['id'],
                'title': item['snippet']['title'],
                'published': item['snippet']['publishedAt'][:10]
            })
        
        next_page = response.get('nextPageToken')
        if not next_page:
            break
    
    return playlists

def main():
    youtube = get_youtube_service()
    
    print("Fetching all playlists from AWS Events channel...")
    all_playlists = get_all_playlists(youtube, CHANNEL_ID)
    
    print(f"\nTotal playlists found: {len(all_playlists)}")
    
    # Filter for re:Invent 2025
    reinvent_2025 = [p for p in all_playlists if 're:Invent 2025' in p['title'] or 'reinvent 2025' in p['title'].lower()]
    
    print(f"\nre:Invent 2025 playlists found: {len(reinvent_2025)}")
    print("\n" + "="*80)
    
    for pl in sorted(reinvent_2025, key=lambda x: x['title']):
        print(f"\nTitle: {pl['title']}")
        print(f"ID: {pl['id']}")
        print(f"Published: {pl['published']}")
    
    print("\n" + "="*80)
    print("\nPlaylist IDs only:")
    for pl in sorted(reinvent_2025, key=lambda x: x['title']):
        print(f"    - {pl['id']}  # {pl['title']}")

if __name__ == '__main__':
    main()
