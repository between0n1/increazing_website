class Platforms:
    def __init__(self):
        self.sources = {}
        self.count = 0
    def add(self, source):
        self.sources[source.name] = source
        self.count += 1
    def display(self):
        for i in self.sources:
            print(i)
    def get(self, sourceName):
        if self.sources.get(sourceName) != None:
            return self.sources.get(sourceName)
    def clear(self):
        self.sources = {}



class Source: # instagram, reddit, twitter
    def __init__(self, name, posts): # posts = array of post object
        self.name = name
        self.posts = posts
    def __repr__(self):
        return self.name
    def display(self):
        for elem in self.posts:
            print(elem.title, elem.volume)


class Twitter():
    def __init__(self, title = "",  link = None, volume = None, topHTML = None):
        self.topHTML = topHTML # a html script
        self.title = title # hashtag
        self.link = link
        self.volume = volume
        self.volumeUnit = "tweets"
    def addTop(self,html):
        self.topHTML = html



    def __repr__(self):
        return f"title: {self.title} volume: {str(self.volume)} link: {self.link}"
    def __lt__(self, other):
        return self.volume < other.volume
    def __eq__(self, other):
        return self.volume == other.volume


class Reddit():
    def __init__(self, title = "", text= "", link = None, volume = None, img = None, author = None, video = None, html = None):
        self.title = title
        self.text= text
        self.link = link
        self.volume = volume
        self.img = img
        self.author = author
        self.video = video
        self.volumeUnit = "upvotes"
        self.html = html
    def __repr__(self):
        return f"title: {self.title} volume: {str(self.volume)} link: {self.link}"
    def __lt__(self, other):
        return self.volume < other.volume
    def __eq__(self, other):
        return self.volume == other.volume


