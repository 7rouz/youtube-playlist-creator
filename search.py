import pprint

from apiclient.discovery import build
from oauth2client.tools import argparser
from oauth2_authentication import get_authenticated_service

def youtube_search_video(keyword, max_results):

  args = argparser.parse_args()
  youtube = get_authenticated_service(args)

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
      # print "Video title:\t",search_result["snippet"]["title"]," video ID: \t",search_result["id"]["videoId"]," From channel ", search_result["snippet"]["channelId"]

      video_details['title'] = search_result["snippet"]["title"]
      video_details['videoID'] = search_result["id"]["videoId"]
      video_details['channelID'] =  search_result["snippet"]["channelId"]
      videos.append(video_details)

  # pprint.pprint(videos)
  return video_details['videoID'], video_details['title']
