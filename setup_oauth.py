#!/usr/bin/env python3
"""
Setup OAuth2 for YouTube API to download captions.

Steps:
1. Go to https://console.cloud.google.com/apis/credentials
2. Create OAuth 2.0 Client ID (Desktop app)
3. Download JSON and save as 'client_secrets.json' in this directory
4. Run this script to authenticate
"""
import os
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
import pickle

SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']
TOKEN_FILE = 'youtube_token.pickle'
CLIENT_SECRETS = 'client_secrets.json'

def get_credentials():
    creds = None
    
    if os.path.exists(TOKEN_FILE):
        with open(TOKEN_FILE, 'rb') as f:
            creds = pickle.load(f)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            if not os.path.exists(CLIENT_SECRETS):
                print(f"ERROR: {CLIENT_SECRETS} not found!")
                print("\nTo create it:")
                print("1. Go to https://console.cloud.google.com/apis/credentials")
                print("2. Create OAuth 2.0 Client ID (type: Desktop app)")
                print("3. Download JSON and save as 'client_secrets.json'")
                return None
            
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRETS, SCOPES)
            creds = flow.run_local_server(port=0)
        
        with open(TOKEN_FILE, 'wb') as f:
            pickle.dump(creds, f)
    
    return creds

if __name__ == '__main__':
    creds = get_credentials()
    if creds:
        print("OAuth2 setup complete! Token saved to", TOKEN_FILE)
