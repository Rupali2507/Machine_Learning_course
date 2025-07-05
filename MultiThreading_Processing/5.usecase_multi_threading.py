'''
Real world example: Multithreading for I/O-bound Tasks
Scenario: Web Scraping

Web scraping often involves making numerous network requests to fetch webpages. These tasks are I/O -bound because they spend a lot of time waiting for waiting for responses from servers. Multithreading can significantly improve the performance by allowing multiple web pages to be fetched concurrently. 

'''
'''
https://python.langchain.com/docs/introduction/
https://python.langchain.com/docs/concepts/architecture/
https://python.langchain.com/docs/concepts/async/

'''

import threading 
import requests

from bs4 import BeautifulSoup

urls=[
  "https://python.langchain.com/docs/introduction/",
"https://python.langchain.com/docs/concepts/architecture/",
"https://python.langchain.com/docs/concepts/async/"
]

def fetch_content(url):
  response=requests.get(url)
  soup=BeautifulSoup(response.content,'html.parser')
  print(f'Fetched: {len(soup.text)} characters from {url}')

threads = []

for url in urls:
  thread = threading.Thread(target=fetch_content, args=(url,))
  threads.append(thread)
  thread.start()

for thread in threads:
  thread.join()

print("All web pages fetched.")    