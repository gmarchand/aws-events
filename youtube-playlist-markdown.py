"""
----------------------------------------------------------------------------
Author: Jeff Triplett <https://github.com/jefftriplett>
Copyright (c) 2023 - Jeff Triplett
License: PolyForm Noncommercial License 1.0.0 - https://polyformproject.org/licenses/noncommercial/1.0.0/
----------------------------------------------------------------------------

1. To extract video URLs, titles, and descriptions from a YouTube playlist using Python, you can use the google-api-python-client library. Here's a step-by-step guide on how to do this:

  Install the google-api-python-client library:

```shell
pip install google-api-python-client environs rich typer
```

2. Get an API key for the YouTube Data API:
  - Go to the Google Cloud Console: https://console.cloud.google.com/
  - Create a new project or select an existing one.
  - Click on "Enable APIs and Services" and search for "YouTube Data API v3".
  - Click "Enable" to enable the API for your project.
  - Click "Create credentials" and follow the steps to get an API key.

3. To use it:

```shell
export YOUTUBE_API_KEY=YOUR-API-KEY-HERE
python demo-youtube-playlist-to-markdown.py --playlist=PL2yQDdvlhXf8iyzg7ziZI924PxC8a8M-U
```

"""

import typer
import re
import googleapiclient.discovery

from environs import Env
from rich import print

from tomark import Tomark


env = Env()

YOUTUBE_API_KEY = env.str("GOOGLE_API_KEY")


def get_playlist_videos(
        *,
        playlist_id: str,
        playlist_url: str,
        max_results: int = 50,
):
    youtube = googleapiclient.discovery.build(
        "youtube", "v3", developerKey=YOUTUBE_API_KEY
    )

    request = youtube.playlistItems().list(
        part="snippet", maxResults=max_results, playlistId=playlist_id
    )
    videos = []

    while request:
        response = request.execute()
        for item in response["items"]:
            description = re.sub(r"\n|\r","",item["snippet"]["description"][0:600])
            video = {
                "url": f"https://www.youtube.com/watch?v={item['snippet']['resourceId']['videoId']}",
                "title": item["snippet"]["title"],
                "description": description,
            }
            videos.append(video)

        request = youtube.playlistItems().list_next(request, response)

    return videos


def main(
    playlist_id: str = typer.Option("PLcNrB7gPa-NedACvFYa9iVUIhnku_EBSz", "--playlist"),
    max_results: int = 50
):
    playlist_url = f"https://www.youtube.com/playlist?list={playlist_id}"
    playlist_videos = get_playlist_videos(
        playlist_id=playlist_id,
        playlist_url=playlist_url,
        max_results=max_results,
    )
    markdown = Tomark.table(playlist_videos)
    print(markdown)


if __name__ == "__main__":
    typer.run(main)