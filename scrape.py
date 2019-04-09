import io
import re
import requests
from bs4 import BeautifulSoup
import lxml

#Open the Website and use GET-function to scrape information + convert it into text
link=input("Please enter Link (if hyperlinks are enabled in your console, please add a space before typing enter): ")
link=link.rstrip()
try:
    source = requests.get(link).text
except:
    print("This link is not correct."  )
    quit()

#Create a Soup-Object with the lxml-parser active
soup = BeautifulSoup(source, "lxml")

#create empty list for text
text=[]

#set counters to 0
par_count=0
sen_count=0
word_count=0

#Find Headline with try-except
try:
    headline=soup.find("span", class_="atc-HeadlineText").text
except:
    headline="Not able to find headline"

#Find Author with try-except

try:
    author=soup.find("span", class_="atc-MetaAuthor").text
except:
    author="Not able to find headline"

try:
    author = soup.find("a", class_="atc-MetaAuthorLink").text
except:
    author="Not able to find author"

#Find Paragraphs with text and add to list
for p in soup.find_all("p", class_="atc-TextParagraph"):
    text.append(p.text)

#count paragraphs
for paragraph in text:
    par_count=par_count+1

#create one string to split on
text="".join(text)

#split for sentences
sätze=text.split(".")

#count sentences
for satz in sätze:
    sen_count=sen_count+1

#split for words
wörter=text.split()

#count words
for wort in wörter:
    word_count=word_count+1

print("Titel des Artikels:",headline,"\n"
    "Autor:",author,"\n"
      "Paragraphen:",par_count,"\n"
      "Sätze:", sen_count,"\n"
      "Wörter:", word_count)

#Ask if a .txt-file should be created
q1=input("Would you like to create a new .txt-file? (y/n): ")

if q1 == "y":

    file=open(headline+".txt","w+")
    file.write("Title: " + headline + "\n")
    file.write("Author: " + author +"\n")
    file.write("Paragraphs: " + str(par_count) + "\n")
    file.write("Sentences: " + str(sen_count) + "\n")
    file.write("Words: " + str(word_count) + "\n")
    file.write(text + "\n")
    file.close()
    print("File written.")
else:
    print("No file written.")


    #Formatfunktion anstatt write
    "{}{}{}".format(a1, a2, a3)