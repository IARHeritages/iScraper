
###This code was developed as part of the IARH project
###Project IARH
###Author: Chiara Bonacchi

####This code extracts a page of results returned by a Google search (urls and titles)####

##Set working directory
setwd("~/Desktop/Google Scrape")

##Load libraries httr, XML, rvest
library(httr)
library(XML)
library(rvest)

##Search and extract the first 10 results returned by a Google sarch, focussing on the past year
search.term="US+mexican+border+%22roman+empire%22&hl=en&start="
url.name=paste0("https://www.google.com/search?q=", search.term)
url.get=GET(url.name)
url.content=content(url.get, as="text", encoding = "ISO-8859-1")
page <- read_html(url.content)
results.titles <- page %>% html_nodes("h3[class=r]") %>% html_text()
results.links <- page %>% html_nodes("cite") %>% html_text()


####This code loops through a vector of URLS, extract their html trees and saves them as distinct variables####

##Set working directory
setwd("~/Desktop/Google Scrape")

##Load libraries xlsx and XML
library(xlsx)
library(XML)

##import xlsx file with sheet containing one column names 'URL'
read.xlsx("test.xlsx", 1) -> data

##trsansform dataframe column named URL into a vector
URL <- data$URL
URL <- as.vector(URL)

##set parameters
length(URL) -> n
g = n+1
i=0

##loop through the vector of URLs, extracting the html tree for each URL and saving it as a distinct variable wp[[i]]
while (i < g) {
	
	url <- (URL[[i]])
	webpage <- readLines(url)
	wp <- htmlTreeParse(webpage)
	wp[[i]] <-wp
	i=i+1
	print(i)
}
