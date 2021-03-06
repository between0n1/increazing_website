def Convert(volume : int):
    if volume :
        if volume > 1000000:
            num = ((volume/1000000))
            unit = 'M'
        elif volume > 1000:
            num = ((volume/1000))
            unit = 'K'
        calculated_num = "{:.1f}".format(num) # round up to 1 decimal place
        return str(calculated_num) + unit + " "
    else:
        return '0'

class Platforms:
    def __init__(self):
        self.sources = {}
        self.count = 0
    def add(self, source):
        self.sources[source.name] = source
        self.count += 1
    def display(self):
        for i in self.sources:
            print(i, end = " ")
        print()
    def get(self, sourceName):
        if self.sources.get(sourceName) != None:
            return self.sources.get(sourceName)
    def clear(self):
        self.sources = {}

# we do not need this class
class Source: # instagram, reddit, twitter
    def __init__(self, name, posts, postCount): # posts = array of post object
        self.name = name
        self.posts = posts
        self.postCount = postCount
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
        self.vol = Convert(self.volume) + self.volumeUnit
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
        self.vol = Convert(self.volume) + self.volumeUnit
    def __repr__(self):
        return f"title: {self.title} volume: {str(self.volume)} link: {self.link}"
    def __lt__(self, other):
        return self.volume < other.volume
    def __eq__(self, other):
        return self.volume == other.volume

class Youtube():
    def __init__(self, video = None, title = None, volume = None):
        self.video = video
        self.link = video
        self.title = title
        self.volume = int(volume)
        self.volumeUnit = "views"
        self.vol = Convert(self.volume) + self.volumeUnit
    def __lt__(self, other):
        return self.volume < other.volume
    def __eq__(self, other):
        return self.volume == other.volume