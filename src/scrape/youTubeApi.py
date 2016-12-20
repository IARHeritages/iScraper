'''
Created on Dec 11, 2016

@author: maltaweel
'''
from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser
import gdata.youtube
import gdata.youtube.service
import argparse

key='AIzaSyA8XJm8lda2bCjACudSN0VffMhUdF3f-7Q'
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"

def SearchAndPrint(search_terms):
  yt_service = gdata.youtube.service.YouTubeService()
  query = gdata.youtube.service.YouTubeVideoQuery()
  query.vq = search_terms
  query.orderby = 'viewCount'
  query.racy = 'include'
  feed = yt_service.YouTubeQuery(query)
  
  PrintVideoFeed(feed)

def PrintVideoFeed(feed):
  for entry in feed.entry:
    PrintEntryDetails(entry)
    
def PrintEntryDetails(entry):
  print 'Video title: %s' % entry.media.title.text
  print 'Video published on: %s ' % entry.published.text
  print 'Video description: %s' % entry.media.description.text
  print 'Video tags: %s' % entry.media.keywords.text
  print 'Video watch page: %s' % entry.media.player.url
  print 'Video flash player URL: %s' % entry.GetSwfUrl()
  print 'Video duration: %s' % entry.media.duration.seconds

  # non entry.media attributes
  print 'Video geo location: %s' % entry.geo.location()
  print 'Video view count: %s' % entry.statistics.view_count
  print 'Video rating: %s' % entry.rating.average

  # show alternate formats
  for alternate_format in entry.media.content:
    if 'isDefault' not in alternate_format.extension_attributes:
      print 'Alternate format: %s | url: %s ' % (alternate_format.type,
                                                 alternate_format.url)

  # show thumbnails
  for thumbnail in entry.media.thumbnail:
    print 'Thumbnail url: %s' % thumbnail.url


def SearchAndPrintVideosByKeywords(list_of_search_terms):
    youtube = build(
                    YOUTUBE_API_SERVICE_NAME, 
                    YOUTUBE_API_VERSION, 
                    developerKey='AIzaSyA8XJm8lda2bCjACudSN0VffMhUdF3f-7Q'
                    )
    yt_service = gdata.youtube.service.YouTubeService()
    query = gdata.youtube.service.YouTubeVideoQuery()
    query.orderby = 'viewCount'
    query.racy = 'include'
  
    for search_term in list_of_search_terms:
        new_term = search_term.lower()
        query.categories.append('/%s' % new_term)
    
    feed = yt_service.YouTubeQuery(query)
    PrintVideoFeed(feed)
  
# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.

def search_by_keyword(qTerm):
    youtube = build(
                    YOUTUBE_API_SERVICE_NAME, 
                    YOUTUBE_API_VERSION, 
                    developerKey='AIzaSyA8XJm8lda2bCjACudSN0VffMhUdF3f-7Q'
                    )
    search_response = youtube.search().list(
                                            q=qTerm,
                                            part="id,snippet",
                                            maxResults=25
                                            ).execute()

    
    videos = []

    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            videos.append("%s (%s)" % (search_result["snippet"]["title"],
                                   search_result["id"]["videoId"]))
            return videos

term1="Roman Empire"
term2="Britain"

terms=[]
terms.append(term1)
terms.append(term2)


lst=search_by_keyword(terms)

for i in lst:
    print(i)