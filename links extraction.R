
###This code was developed as part of the IARH project
###Project IARH
###Author: Chiara Bonacchi
###The code extracts a page of results returned by a Google search (urls and titles)

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

