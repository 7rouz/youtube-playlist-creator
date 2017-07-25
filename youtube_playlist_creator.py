from search import youtube_search
from apiclient.errors import HttpError

keyword_list = ["kings of leon", "the head I hold"]

if __name__ == "__main__":
  for keyword in keyword_list:
    try:
      youtube_search(keyword,50)
    except HttpError, e:
      print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)

