from django.shortcuts import render
import requests 

from bs4 import BeautifulSoup

# news from times of India

toi_r = requests.get("https://timesofindia.indiatimes.com/briefs")
toi_soup = BeautifulSoup(toi_r.content, 'html.parser')

toi_headings = toi_soup.find_all('h2')
toi_headings = toi_headings[0:-13] #this removes the footers

toi_news = []

for th in toi_headings:
    toi_news.append(th.text)

hindu_r = requests.get("https://www.hindustantimes.com/india-news/")
hindu_soup = BeautifulSoup(hindu_r.content, 'html.parser')
hindu_headings = hindu_soup.findAll("div", {"class": "headingfour"})
hindu_headings = hindu_headings[2:]
hindu_news = []

for hth in hindu_headings:
    hindu_news.append(hth.text)

def index(request):
    context = {'toi_news':toi_news, 'hindu_news':hindu_news}
    return render(request, 'news/index.html', context)
