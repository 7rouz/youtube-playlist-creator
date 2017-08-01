from apiclient.discovery import build
from oauth2client.tools import argparser
import pprint

YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def youtube_search_video(keyword, max_results, dev_key):
  youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
    developerKey=dev_key)

  # Call the search.list method to retrieve results matching the specified
  # query term.
  search_response = youtube.search().list(
    q=keyword,
    part="id,snippet",
    maxResults=max_results
  ).execute()

  # list of all videos that match the search
  videos = []
  # a dict to save video title , ID and channelID 
  # video_details = {
  #   "title" = "title",
  #   "videoID" = "videoID"
  #   "channelID" = "channelID"
  # }
  video_details = {}

  # Add each result to the appropriate list, and then display the lists of
  # matching videos, channels, and playlists.
  for search_result in search_response.get("items", []):
    video_details = {}
    if search_result["id"]["kind"] == "youtube#video":
      # pprint.pprint(search_result)
      print "Video title:\t",search_result["snippet"]["title"]," video ID: \t",search_result["id"]["videoId"]," From channel ", search_result["snippet"]["channelId"]

      video_details['title'] = search_result["snippet"]["title"]
      video_details['videoID'] = search_result["id"]["videoId"]
      video_details['channelID'] =  search_result["snippet"]["channelId"]
      videos.append(video_details)

  pprint.pprint(videos)
  return video_details['videoID']
