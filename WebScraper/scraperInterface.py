import wx
import scraper

class interface:

    def __init__(self, title):
        self.title = title
        #self.app = wx.App()
        #self.drawWindow()
        #self.app.MainLoop()

    def drawTextUI(self):
        print("Web scraper")
        while(True):
            print("Options")
            print("1: Get new page")
            print("0: Exit")
            try:
                userIn = int(input("Enter selection here: "))
            except ValueError:
                userIn = 2
                print("Invalid input.\nMust use an integer")
            if(userIn == 1):
                try:
                    newURL = input("Enter url here: ")
                    self.addWebsite(newURL)
                    print("Page name - " + str(self.scrape.parser.title.text))
                    while(True):
                        print("Site options")
                        print("1: View HTML")
                        print("2: Scrape item by tag")
                        print("3: Scrape item by id")
                        print("4: Scrape item by class")
                        print("5: Save site data")
                        print("0: Back")
                        try:
                            userSelect = int(input("Enter selection here: "))
                        except ValueError:
                            print("Invalid input.\n Must use an integer")

                        if(userSelect == 1):
                            print(self.scrape.parser.prettify())

                        elif(userSelect == 2):
                            pass

                        elif(userSelect == 3):
                            try:
                                idSelect = str(input("Enter the id here: "))
                                idTag = str(input("Enter the search tag here: "))
                            except:
                                print("An error has occured")
                            self.scrape.getITemByID(idSelect, idTag)
                        elif(userSelect == 5):
                            try:
                                filename = str(input("Enter filename here: "))
                                self.scrape.saveData(filename)
                            except:
                                print("An error has occured")
                        elif(userSelect == 0):
                            break
                        else:
                            pass
                except:
                    print("Invalid URL")
                
            elif(userIn == 0):
                break
            else:
                pass
        

    def drawWindow(self):
        """
        draws the window in which the application runs
        """
        self.frame = wx.Frame(None, title='Web scraper', name='Web Scraper')
        self.frame.Show()

    def createGetSite(self):
        pass  

    def addWebsite(self, url):
        self.url = url
        self.scrape = scraper.scraper(url)

