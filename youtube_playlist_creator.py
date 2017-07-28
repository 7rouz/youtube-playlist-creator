from search import youtube_search_video
from apiclient.errors import HttpError
import ConfigParser

keyword_list = ["kings of leon", "the head I hold"]

if __name__ == "__main__":
  config_youtube = ConfigParser.ConfigParser()

  config_youtube.read("config.cfg")

  dev_key = config_youtube.get('defaults','DEVLOPER_KEY')

  for keyword in keyword_list:
    try:
      youtube_search_video(keyword=keyword,dev_key=dev_key,max_results=50)
    except HttpError, e:
      print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)

