from datetime import date
from PIL import Image


def cons(foo):
        stre = ""
        for cons in foo:
            stre = stre + cons
        return stre

class Content(object):
    # list to keep track of all pieces of content
    existing_content = []

    def __init__(self, year, month, day, contributors):
        # log each piece of content as existing upon creation
        self.existing_content.append(self)

        # TODO: Delete the following line and replace it with a line
        # that stores the year, month, and day (hint: check out datetime.date)
        self.creation_date = date(year, month, day)

        # list of contirbutors
        self.contributors = contributors

    # this defines a show method that has nothing in it, to be overridden later
    def show(self):
       	pass


class Article(Content):

    def __init__(self, year, month, day, headline, content, contributors):
        super(Article, self).__init__(year, month, day, contributors)
        self.headline = headline
        self.content = content

    def show(self):
       	print 'Date: {0}; Contributors: {1}\n\
       		  Headline: {2} \n Content: {3} \n'.format(self.creation_date.strftime('%Y, %B, %d'), cons(self.contributors), self.headline, self.content)


class Picture(Content):

    def __init__(self, year, month, day, title, caption, path, contributors):
        super(Picture, self).__init__(year, month, day, contributors)
        self.title = title
        self.caption = caption
        self.path = path

    def show(self):
        Image.open(self.path).show()
    	print 'Date: {0}; Contributors: {1}\n\
       		  Title: {2} \n Caption: {3}'.format(self.creation_date.strftime('%Y, %B, %d'),\
                cons(self.contributors), self.title, self.caption)

