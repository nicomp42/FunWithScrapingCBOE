#ScrapeCBOE.py

# Need to install lxml
# pip install lxml - use the Eclipse tool in the project properties
# We don't need to import lxml

from bs4 import BeautifulSoup
import requests

def demo():
    url = "https://www.cboe.com/delayed_quotes/ko"
    # Get the webpage “Page Source”, it’s provided as a Response object. 
    response = requests.get(url)
    # Extract the source code of the page.
    data = response.text
    # Passing the source code to BeautifulSoup to create a BeautifulSoup object for it.
    # lxml is the parser, provided by a different library.
    soup = BeautifulSoup(data, 'lxml')
    #print(soup)  # This is the text transmitted from cboe.com. It has not yet been executed/rendered by the browser.
    
    # Look for the class we identified when we did "Inspect Object" from our browser.
    # Unfortunately, it's not there because the rendering engine in the browser creates it.
    div= soup.find_all("div", {"class":"Box-sc-jzm6b1-0"})
    print(div)
