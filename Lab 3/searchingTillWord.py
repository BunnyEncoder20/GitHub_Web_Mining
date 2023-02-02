# Simple Crawler to find a specified word from root url

from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

class Crawler : 
    def __init__(self, matches, crawled, search_word, url=[]) : 
        print("\nList of Pages Found : ")
        self.search_word = search_word
        self.matches = matches
        self.crawled = crawled
        self.visited_urls = []
        self.urls_to_visit = url
        self.root = 0

    def download_url(self,url) : 
        #returning the text of the webpage
        return requests.get(url).text

    def get_linked_urls(self,url,htmltxt) : 
        soup = BeautifulSoup(htmltxt, 'html.parser')
        for link in soup.find_all('a') : 
            path = link.get('href')
            if path and path.startswith('/') :
                path = urljoin(url,path)
            yield path

    def add_urls_to_visit(self,url) : 
        if url not in self.visited_urls and url not in self.urls_to_visit :
            self.urls_to_visit.append(url)

    def crawl (self,url)  :
        txt = requests.get(url).text
        temp_soup = BeautifulSoup(txt, 'html.parser')

        print("Link ",self.crawled," ",url)

        if (self.root == 0) :                               #limiting the links only to the root pages
                htmltxt = self.download_url(url)       # code to crawl continously 
                self.root = 1
                for url in self.get_linked_urls(url,htmltxt) : 
                    self.add_urls_to_visit(url)

        if (temp_soup.find(string=search_word)) : 
            self.matches+=1
            print("Found it !!!")
            yield
            

            

    def run(self) : 
        while self.urls_to_visit and self.matches==0 :
            url = self.urls_to_visit.pop(0)
            try  :
                #limiting the crawling to a 50 pages only
                if(self.crawled == 50) : 
                    break
                else :
                    self.crawl(url)
                    self.crawled+=1
            except Exception :
                pass
            finally :
                self.visited_urls.append(url)
        
        print("\n")
        print("Pages Crawled : ",self.crawled)
        print("Key Word is : ",self.search_word)
        if self.matches>0 :
            print("Page with match found : ",self.matches)



#Driver Code 
if __name__ == '__main__' : 
    crawled = 0
    matches = 0
    search_word = "Supra"
    Crawler(matches,crawled,search_word,url=['https://en.wikipedia.org/wiki/Toyota_Celica']).run()
