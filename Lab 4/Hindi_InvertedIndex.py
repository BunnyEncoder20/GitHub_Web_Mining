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
    "https://hi.wikipedia.org/wiki/%E0%A4%B5%E0%A5%87%E0%A4%AC%E0%A4%AA%E0%A5%87%E0%A4%9C#:~:text=%E0%A4%9C%E0%A4%BE%E0%A4%B2%E0%A4%AA%E0%A5%83%E0%A4%B7%E0%A5%8D%E0%A4%A0%20%E0%A4%AF%E0%A4%BE%20%E0%A4%B5%E0%A5%87%E0%A4%AC%E0%A4%AA%E0%A5%87%E0%A4%9C%20(webpage)%20%E0%A4%8F%E0%A4%95,%E0%A4%AD%E0%A5%80%20%E0%A4%9C%E0%A4%BE%E0%A4%AF%E0%A4%BE%20%E0%A4%9C%E0%A4%BE%20%E0%A4%B8%E0%A4%95%E0%A4%A4%E0%A4%BE%20%E0%A4%B9%E0%A5%88%E0%A5%A4",
    "https://hi.wikipedia.org/wiki/%E0%A4%B5%E0%A4%BF%E0%A4%95%E0%A4%BF%E0%A4%AA%E0%A5%80%E0%A4%A1%E0%A4%BF%E0%A4%AF%E0%A4%BE:%E0%A4%9A%E0%A5%8C%E0%A4%AA%E0%A4%BE%E0%A4%B2",
    "https://hi.wikipedia.org/wiki/%E0%A4%B5%E0%A4%BF%E0%A4%B6%E0%A5%87%E0%A4%B7:RecentChanges?hidebots=1&hidecategorization=1&hideWikibase=1&limit=50&days=7&urlversion=2",
    "https://hi.wikipedia.org/wiki/%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%B5%E0%A5%87%E0%A4%B6%E0%A4%A6%E0%A5%8D%E0%A4%B5%E0%A4%BE%E0%A4%B0:%E0%A4%B9%E0%A4%BE%E0%A4%B2_%E0%A4%95%E0%A5%80_%E0%A4%98%E0%A4%9F%E0%A4%A8%E0%A4%BE%E0%A4%8F%E0%A4%81",
    "https://hi.wikipedia.org/wiki/%E0%A4%B5%E0%A4%BF%E0%A4%95%E0%A4%BF%E0%A4%AA%E0%A5%80%E0%A4%A1%E0%A4%BF%E0%A4%AF%E0%A4%BE:%E0%A4%A8%E0%A4%BF%E0%A4%B0%E0%A5%8D%E0%A4%B5%E0%A4%BE%E0%A4%9A%E0%A4%BF%E0%A4%A4_%E0%A4%B5%E0%A4%BF%E0%A4%B7%E0%A4%AF_%E0%A4%B5%E0%A4%B8%E0%A5%8D%E0%A4%A4%E0%A5%81",
    "https://hi.wikipedia.org/wiki/%E0%A4%95%E0%A5%87%E0%A4%9C,_%E0%A4%AC%E0%A5%80%E0%A4%A1",
    "https://hi.wikipedia.org/wiki/%E0%A4%B5%E0%A4%BF%E0%A4%95%E0%A4%BF%E0%A4%AA%E0%A5%80%E0%A4%A1%E0%A4%BF%E0%A4%AF%E0%A4%BE:%E0%A4%AA%E0%A5%8D%E0%A4%B0%E0%A4%AF%E0%A5%8B%E0%A4%97%E0%A4%B8%E0%A5%8D%E0%A4%A5%E0%A4%B2",
    "https://hi.wikipedia.org/wiki/%E0%A4%B5%E0%A4%BF%E0%A4%95%E0%A4%BF%E0%A4%AA%E0%A5%80%E0%A4%A1%E0%A4%BF%E0%A4%AF%E0%A4%BE:%E0%A4%85%E0%A4%A8%E0%A5%81%E0%A4%B0%E0%A5%8B%E0%A4%A7",
    "https://hi.wikipedia.org/wiki/%E0%A4%B5%E0%A4%BF%E0%A4%95%E0%A4%BF%E0%A4%AA%E0%A5%80%E0%A4%A1%E0%A4%BF%E0%A4%AF%E0%A4%BE:%E0%A4%B8%E0%A4%B9%E0%A4%BE%E0%A4%AF%E0%A4%A4%E0%A4%BE",
    "https://hi.wikipedia.org/wiki/%E0%A4%B5%E0%A4%BF%E0%A4%95%E0%A4%BF%E0%A4%AA%E0%A5%80%E0%A4%A1%E0%A4%BF%E0%A4%AF%E0%A4%BE:%E0%A4%B8%E0%A5%8D%E0%A4%B5%E0%A4%B6%E0%A4%BF%E0%A4%95%E0%A5%8D%E0%A4%B7%E0%A4%BE"
]


# call to create the inverted index 
inverted_index = create_inverted_index(urls)

# Printing the inverted Index : {word} : {number of occurances}
for word, urls in inverted_index.items() : 
    print(f"{word} : {len(urls)}")