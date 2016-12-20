'''
Created on Dec 11, 2016

@author: maltaweel
'''
from scrape.youTubeScraperII import YouTubeHandler
import csv
 
search_key = '%22Roman Empire%22 Britain' #keywords
yy = YouTubeHandler(search_key)
yy.download_as_audio =1 # 1- download as audio format, 0 - download as video
yy.set_num_playlist_to_extract(1000) # number of playlist to download
 
print 'Get all the playlist'
yy.get_playlist_url_list()
#print yy.playlist_url_list
 
## Get all the individual video and title from each of the playlist

yy.get_video_link_fr_all_playlist()
fieldnames = ['Title', 'Link']

with open('YouTubeLinks.csv', 'w') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in yy.video_link_title_dict:
        print(i)
        print(yy.video_link_title_dict[i])
        writer.writerow({'Title': i.encode('utf-8').strip(), 'Link': yy.video_link_title_dict[i].encode('utf-8').strip()})

