# A simple web scrapper for a Web Page

#  requests and BeautifulSoup are externale Libraries and you will need to install them before
# (in terminal)
# pip intall requests
# pip intall beautifulsoup4
import requests 
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Jaguar"
response = requests.get(URL)
print("Connection : ",response.status_code) #should print 200 for all ok

#Note : response.text is a string which contains the entire webpage
# print(response.text)

#creating a instance of a BeautifulSoup object
soup = BeautifulSoup(response.text,'html.parser')   #we telling that we have the response.text and that we want to parse it as a html

#We convert the string (response.text) into a bs4.BeautifulSoup obj because as a string, we cannot do much with that data, but bs4.BeautifulSoup obj has a ton of functionality

#getting the title and paragraph from the wiki page:
all_paragraphs = soup.find_all('p')     #this returns a BeautifulSoup ResultSet which functions similar to a list of all the paragraphs of the page
# print(all_paragraphs[2])        
first_para = all_paragraphs[2]          #saving the first paragraph material into a variable
print(first_para.text)      #printing only the text part of the seperated first para

#getting all the anchor tags from the first paragraph :    (cause entire articles is too big)
all_links = first_para.find_all('a')
print("All the words which are Links in the First Paragraph are : ")
for link in all_links:
    print(link.text)

#getting all the h2 tags from the entire Article :
all_h2 = soup.find(id='bodyContent').find_all('h2')
print("\n\nAll the words which are H2 Headings in the entire Article are : ")
for h2 in all_h2:
    print(h2.text)



#making the scrapping a little variable :
topic = input("\n\nEnter the topic you want to get from the wiki : ")
URL = f'https://en.wikipedia.org/wiki/{topic}'      # f'...' for formatting teh string
print(URL)
response = requests.get(URL)
print("Connection : ",response.status_code) 

soup = BeautifulSoup(response.text,'html.parser')
all_paragraphs = soup.find_all('p') 
first_para = all_paragraphs[2]
print(first_para.text)
print("\n\nAll the words which are Links in THIS page's  First Paragraph are : ")
all_links = first_para.find_all('a')
for link in all_links:
    print(link.text)

