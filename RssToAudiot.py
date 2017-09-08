import feedparser
from mercury_parser import ParserAPI
import requests
import justext
from gtts import gTTS
from configparser import ConfigParser




config = ConfigParser()
config.read("config.ini")
mercuryAPI = config.get("auth", "mercury_key" )

mercury = ParserAPI(mercuryAPI)

feed = feedparser.parse("http://feeds.bbci.co.uk/news/rss.xml")
#AudioSegment.converter = "C:\\Users\\mihir\\ffmpeg\\bin\\ffmpeg"


numArticles = 0

for article in feed.entries:
    if (numArticles < 5):

        response = requests.get(article["link"])
        p = mercury.parse(article["link"])

        if (p.content != None):
            paragraphs = justext.justext(p.content, justext.get_stoplist("English"))

            articleText = article.title + ". "
            textFragment = ""

            for paragraph in paragraphs:
                articleText += paragraph.text + " "

            if(len(articleText) != 0):
                print(article.title)
                print(articleText)
                print("\n\n")

                filename = "article" + str(numArticles) +".mp3"

                output = gTTS(text=articleText, lang="en")
                output.save(filename)



                #articleWav = AudioSegment.from_file(filename)

                # y, sr = sf.read(filename)
                # y_stretch = pyrb.time_stretch(y, sr, 2.0)



                #articleWav.speedup(2.0)


                #articleWav = speedUp(articleWav)

                #articleWav.export(filename, format="wav")



            numArticles += 1

