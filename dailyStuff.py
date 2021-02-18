
import requests
from bs4 import BeautifulSoup

def getQuote():
    url = "https://www.brainyquote.com/quote_of_the_day"
    r = requests.get(url)
    page = BeautifulSoup(r.content, 'html.parser')
    quote = page.select('img')
    startQuote = str(quote).find('alt="')+len('alt="')
    endQuote = str(quote).find('" class')
    quote = str(quote)[startQuote:endQuote]
    return quote


def getWord():
    url = 'https://www.dictionary.com/e/word-of-the-day/'
    r = requests.get(url)
    page = BeautifulSoup(r.content, 'html.parser')
    wordContainer = page.find(class_="otd-item-headword")
    word = wordContainer.find('div', {"class": "otd-item-headword__word"}).text.replace('\n', '').replace(' ', '')
    desc = page.find('div', {"class": "otd-item-headword__pos"}).text.replace('\n', ' ').replace('   ', ' - ')
    return str(word).capitalize()+str(desc).capitalize()


def lineBreaker(string):
    output = string
    n = 0
    for i in output:
        n = n + 1
        if i == "\n":
            n = 0
        elif n % 35 == 0:
            x = output.rfind(" ", 0, n)
            output = output[:x]+'\n '+output[x+1:]
    return output





