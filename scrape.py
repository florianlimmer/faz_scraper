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

    print("This link is not correct or you are not connected to the internet.")
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

if len(author)==0:

    try:
        author = soup.find("a", class_="atc-MetaAuthorLink").text
    except:
        author="Not able to find author"


#Check for multi-page articles and create list of all the sites
linklist=[]
linklist.append(link)
listcounter=0
counter=0

for a in soup.find_all("a", class_="nvg-Paginator_Link", href=True):
    if a["href"] not in linklist:
        linklist.append(a["href"])
        listcounter=listcounter+1


#open every site, read text and append it to text-list
while counter <= listcounter:

    try:
        source = requests.get(linklist[counter]).text
        # Create a Soup-Object with the lxml-parser active
        soup = BeautifulSoup(source, "lxml")

        # Find Paragraphs with text and add to list
        for p in soup.find_all("p", class_="atc-TextParagraph"):
            text.append(p.text)

        counter=counter+1

    except:

        print("This link is not correct or you are not connected to the internet.")
        quit()

    #end-condition for while-loop
    if counter == listcounter:
        continue



# count paragraphs
for paragraph in text:
    par_count = par_count + 1

#create one string to split on
text="".join(text)

#split for sentences (TO DO: improve to split on ! or ? too!)
sätze=text.split(".")

#count sentences
for satz in sätze:
    sen_count=sen_count+1

#split for words (split on blank space)
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

    file=io.open(headline+".txt","w", encoding="utf-8")
    file.write('Title: {}\n'
               'Author: {}\n'
               'Paragraphs: {}\n'
               'Sentences: {}\n'
               'Words: {}\n'
               '{}'.format(headline, author, par_count, sen_count, word_count, text))
    file.close()
    print("File written.")
else:
    print("No file written.")