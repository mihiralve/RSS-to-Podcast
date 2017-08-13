import feedparser
import urllib.request
import goose

feed = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")

numArticles = 0

for article in feed.entries:
    if numArticles < 1:
        print(article.title + ": " + article.link)
        content = urllib.request.urlopen(article['link']).read()
        print(content)
        numArticles += 1

    else:
        break