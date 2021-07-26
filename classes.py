class Source: # instagram, reddit, twitter
    def __init__(self, posts): # posts = array of post object
        self.posts = posts
class Post: # a post from sources
    def __init__(self, title, text, captions, images, link):
        self.title = title
        self.text = text
        self.images = images
        self.captions = captions # array of string
        self.link = link
    def __repr__(self):
        return self.title + ", " + self.text

