# RSS-to-Podcast
Download articles from RSS feed, run them through a text summarizer and create a Podcast with TTS

Uses the feedparser and Mercury Parser libraries to extract an article from a news site RSS feed.
Uses the Google Text-To-Speech module (gtts) to convert the text to audio. 

Currently set to the BBC RSS Feed, change the feedURL variable to any other RSS Feed to access another website.

To use create a  config.ini file with the mercury parser API key in the following format:
[auth]
mercury_key = XXXXXXXXXXXXXXXXXXXXXX

Get key here: https://mercury.postlight.com/web-parser/
