import requests
from bs4 import BeautifulSoup
from collections import defaultdict

# function to fetch text from URL
def fetch_text_from_url(url) : 
    try :
        page = requests.get(url)
        soup = BeautifulSoup(page.content,'html.parser')
        text = soup.get_text().lower()
        return text
    except :
        return ""

# fucntion to crawl and create inverted index
def create_inverted_index(urls) :
    inverted_index =    defaultdict(set)

    for url in urls : 
        text = fetch_text_from_url(url)
        words = text.split() 

        for word in words : 
            inverted_index[word].add(url)
    return inverted_index


# Defining the urls to crawl
urls = [
    "https://en.wikipedia.org/wiki/Satisfactory",
    "https://en.wikipedia.org/wiki/Forza_Horizon_4",
    "https://en.wikipedia.org/wiki/Forza_Horizon_5",
    "https://en.wikipedia.org/wiki/Forza_Horizon_3",
    "https://en.wikipedia.org/wiki/Dead_Space_(2023_video_game)",
    "https://en.wikipedia.org/wiki/Left_4_Dead_2",
    "https://en.wikipedia.org/wiki/Toyota_Supra",
    "https://en.wikipedia.org/wiki/Nissan_Skyline_GT-R",
    "https://en.wikipedia.org/wiki/Subaru_WRX",
    "https://en.wikipedia.org/wiki/Toyota_AE86"
]


# call to create the inverted index 
inverted_index = create_inverted_index(urls)

# Printing the inverted Index : {word} : {number of occurances}
for word, urls in inverted_index.items() : 
    print(f"{word} : {len(urls)}")