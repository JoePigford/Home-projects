import scraperOutput
from bs4 import BeautifulSoup
import requests

class scraper:

    def __init__(self, url):
        self.url = url
        siteData = requests.get(url)
        self.parser = BeautifulSoup(siteData.content, 'html.parser')
        self.pageTitle = self.parser.title.text

    def saveData(self, filename):
        self.out = scraperOutput.output(filename)
        self.out.getConnection()

    def getItemByClassname(self, classname):
        self.classname = classname

    def getITemByID(self, id, tag):
        self.id = id
        self.tag = tag

        if(self.tag  == "h1"):
            idTag = self.parser.h1.text
            print(idTag)
        elif(self.tag  == "h2"):
            pass
        else:
            pass

    def getImages(self):
        pass

