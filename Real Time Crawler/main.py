import threading 
from queue import Queue
from spider import Spider
from domain import *
from general import *

# Constants are generally coded in CAPS
PROJECT_NAME = 'Wikipedia'
HOMEPAGE = 'https://en.wikipedia.org/wiki/Main_Page'
DOMAIN_NAME = get_domain__name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADS = 8
queue = Queue()

# The first spider :  
Spider(PROJECT_NAME, HOMEPAGE, DOMAIN_NAME)

# Each queued link is a new job
def create_jobs() : 
    for link in file_to_set(QUEUE_FILE) :
        queue.put(link)
    queue.join()
    crawl()

# check if there are items in teh queue, if so crawl em
def crawl() : 
    queue_links = file_to_set(QUEUE_FILE)
    if len(queue_links) > 0 :
        print(str(len(queue_links)) + ' links in the queue')
        create_jobs()



# Create a worker threads (will die when main exits)
def create_workers() : 
    for _ in range(NUMBER_OF_THREADS) :
        t = threading.Thread(target=work)
        t.daemon = True     #unsures that the spider threads dies when the main exits 
        t.start()

# Do the next job in the queue
def work() : 
    while True : 
        url = queue.get()
        Spider.crawled_page(threading.current_thread().name, url)
        queue.task_done()


create_workers()
crawl()