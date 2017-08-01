from search import youtube_search_video
from playlist_handler import playlists_insert, playlists_update, playlist_items_insert 
from apiclient.errors import HttpError
import ConfigParser

keyword_list = ["kings of leon", "the head I hold"]

if __name__ == "__main__":
  config_youtube = ConfigParser.ConfigParser()
  config_youtube.read("config.cfg")
  dev_key = config_youtube.get('defaults','DEVLOPER_KEY')

  # create a playlist
  playlist = playlists_insert(
            {'snippet.title': 'test_playlist',
             'snippet.description': 'a playlist created using youtube API',
             'snippet.tags[]': 'youtube_API, Rafik, Python', 
             'snippet.defaultLanguage': '',
             'status.privacyStatus': 'public'},
            part='snippet,status',
            onBehalfOfContentOwner='')

#   playlists_update(
#     {'id': playlist["id"],
#      'snippet.title': 'test_playlist',
#      'snippet.description': '',
#      'snippet.tags[]': '',
#      'status.privacyStatus': ''},
#     part='snippet,status',
#     onBehalfOfContentOwner='')
# 

  for keyword in keyword_list:
    try:
      # search for videos that match keywords
      #    keyword: keywords to use wheen sarching 
      #    dev_key: Youtube API key
      #    max_results: maximum number of returned results it goes from 1 to 50
      videoID = youtube_search_video(keyword=keyword,dev_key=dev_key,max_results=1
)
      # add the returned video to the playlist 
      playlist_items_insert(
        {'snippet.playlistId': playlist["id"],
         'snippet.resourceId.kind': 'youtube#video',
         'snippet.resourceId.videoId': videoID,
         'snippet.position': ''},
        part='snippet',
        onBehalfOfContentOwner='')
 
    except HttpError, e:
      print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)

