from urllib.request import urlopen  #is a module to allow us to connect to webpages from python
from link_finder import LinkFinder
from general import *

class Spider : 

    # We are trying to make a multi-crawlers (spiders) 
    # a class variable is a common variable chared amoing all the instances of the class
    project_name = ''
    base_url = ''
    domain_name = ''
    queue_file = ''               #these are the files
    crawled_file = ''           #these are the files
    queue_set = set()         #these are the variables
    crawled_set = set()      #these are the variables


    def __init__(self, project_name, base_url, domain_name) :
        Spider.project_name = project_name
        Spider.base_url = base_url
        Spider.domain_name = domain_name
        Spider.queue_file = Spider.project_name+'/queue.txt'
        Spider.crawled_file = Spider.project_name+'/crawled.txt'
        self.boot()
        self.crawled_page('First Spider', Spider.base_url)

    @staticmethod
    def boot() : 
        create_project_dir(Spider.project_name)
        create_data_files(Spider.project_name,Spider.base_url)
        Spider.queue_set = file_to_set(Spider.queue_file)
        Spider.crawled_set = file_to_set(Spider.crawled_file)

    @staticmethod
    def crawled_page(thread_name, page_url) : 
        if page_url not in Spider.crawled_set : 
            print(thread_name + ' now crawling ' + page_url)
            print('Queue : ' + str(len(Spider.queue_set)) + " | Crawled : " + str(len(Spider.crawled_set)))

            Spider.add_links_to_queue(Spider.gather_links(page_url))
            Spider.queue_set.remove(page_url)
            Spider.crawled_set.add(page_url)        #removing the page from the waiting queue to the cralwed file

            Spider.update_files()

    @staticmethod
    def gather_links(page_url) : 
        html_string = ''        #the urlopen returns the html code in byte format (0 and 1)
                                        # hence we need to convert it into normal html
        try :
            response = urlopen(page_url)
            if response.hetheader('Content-Type') == 'text/html' : 
                html_bytes = response.read()
                html_string = html_bytes.decode('utf-8')
            
            finder = LinkFinder(Spider.base_url, page_url)
            finder.feed(html_string)
        except : 
            print("Error : can not crawl page")
            return set()
        
        return finder.page_links()      # if no errors then call the page_link function to return a set of all the links on the page 

    def add_links_to_queue(links) : 
        for url in links : 
            if url in Spider.queue_set :
                continue
            if url in Spider.crawled_set : 
                continue
            if Spider.domain_name not in url : 
                continue 
            Spider.queue.add(url)

    @staticmethod
    def update_files() : 
        set_to_file(Spider.queue_set,Spider.queue_file)
        set_to_file(Spider.crawled_set,Spider.crawled_file)