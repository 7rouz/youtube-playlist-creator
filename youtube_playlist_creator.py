from search import youtube_search_video
from playlist_handler import playlists_insert, playlists_update, playlist_items_insert 
from keywords_handler import get_keywords
from apiclient.errors import HttpError
import ConfigParser
from datetime import date 

# keyword_list = ["kings of leon", "the head I hold"]

if __name__ == "__main__":
  config_youtube = ConfigParser.ConfigParser()
  config_youtube.read("config.cfg")

  # TODO 
  # use fallback default values for playlist_title and keyword_file
  playlist_title = config_youtube.get('defaults', 'PLAYLIST_TITLE')
  keyword_file = config_youtube.get('defaults', 'KEYWORD_FILE')

  # create a playlist
  playlist = playlists_insert(
            {'snippet.title': playlist_title,
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

  keyword_list = get_keywords(keyword_file)
  for keyword in keyword_list:
    try:
      # search for videos that match keywords
      #    keyword: keywords to use wheen sarching 
      #    dev_key: Youtube API key
      #    max_results: maximum number of returned results it goes from 1 to 50
      videoID, video_title = youtube_search_video(keyword=keyword,
                                                  max_results=1)
      # add the returned video to the playlist 
      playlist_items_insert(
        {'snippet.playlistId': playlist["id"],
         'snippet.resourceId.kind': 'youtube#video',
         'snippet.resourceId.videoId': videoID,
         'snippet.position': ''},
        part='snippet',
        onBehalfOfContentOwner='')

      print video_title ,"has been added to", playlist_title  
    except HttpError, e:
      print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)

