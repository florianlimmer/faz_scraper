import io
import re
import requests
from bs4 import BeautifulSoup
import lxml

#Open the Website and use GET-function to scrape information + convert it into text
source = requests.get("https://www.faz.net/aktuell/politik/ausland/may-will-aufschub-fuer-brexit-16121316.html").text

#Create a Soup-Object with the lxml-parser active
soup = BeautifulSoup(source, "lxml")

#create empty list for text
text=[]

#set counters to 0
par_count=0
sen_count=0
word_count=0

#Find Headline
headline=soup.find("span", class_="atc-HeadlineText").text

#Find Author
author=soup.find("a", class_="atc-MetaAuthorLink").text

#Find Paragraphs with text and add to list
for p in soup.find_all("p", class_="atc-TextParagraph"):
    text.append(p.text)

#count paragraphs
for paragraph in text:
    par_count=par_count+1

#create one string to split on
list="".join(text)

#split for sentences
sätze=list.split(".")

#count sentences
for satz in sätze:
    sen_count=sen_count+1

#split for words
wörter=list.split()

#count words
for wort in wörter:
    word_count=word_count+1

print("Titel des Artikels:",headline,"\n"
      "Autor:",author,"\n"
      "Paragraphen:",par_count,"\n"
      "Sätze:", sen_count,"\n"
      "Wörter:", word_count)