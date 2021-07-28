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

class Post: # a post from sources
    def __init__(self, title = "", text = "", captions = None, images = None, link = None):
        self.title = title
        self.text = text
        self.images = images
        self.captions = captions # array of string
        self.link = link
    def __repr__(self):
        return self.title + ", " + self.text

class Twt(Post):
    def __init__(self, title = "", text= "", link = None, volume = None):
        super().__init__(title= title, text= text, link= link)
        self.volume = volume
    def __repr__(self):
        return f"title: {self.title} volume: {str(self.volume)} link: {self.link}"
    def __lt__(self, other):
        return self.volume < other.volume
    def __eq__(self, other):
        return self.volume == other.volume

