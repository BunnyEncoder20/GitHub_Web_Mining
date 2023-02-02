from html.parser import HTMLParser
from urllib import parse

class LinkFinder(HTMLParser):
    
    def _init_(self, base_url, page_url):           #constructor calling the super class (HTMLParser)
        super()._init_()
        self.base_url = base_url       #The base / root url
        self.page_url = page_url        
        self.links = set()                      #add the new links into this set here

    #overriding the handle_starttag function (this will only get us the starting tags as they contain the href attribute)
    def handle_starttag(self,tag,attrs):        
        if tag == 'a' :
            for (attribute, value) in attrs:
                if attribute == 'href' :
                    url = parse.urljoin(self.base_url,value)
                    self.links.add(url)

    def page_links(self):
        return self.links

    def error(self, message):
        pass


# finder = LinkFinder()
# finder.feed('<html><head><title>Test</title></head>'
                    # '<body><h1>Parse me !</h1></body></html>')