from django.shortcuts import render
import requests
import random


books=["leviticus","hebrews","mark","luke","matthew","john","revelation","romans","numbers"]    # add more books
version='valera' # asv, valera, there are more versions (lenguages)


def url_build(books_,version_):
  book_ = random.choice(books_)
  url_ = f"https://getbible.net/json?passage={book_}&raw=true&version={version_}"
  return url_, book_


def bible(request):
  url = url_build(books, version)[0]
  book = url_build(books, version)[1]
  
  list_chapters = list(range(1,len(requests.get(url).json()['book'])+1))
  choice_chapter = random.choice(list_chapters)
  
  list_vers = list(range(1,len(requests.get(url).json()['book'][f'{choice_chapter}']['chapter'])+1))
  choice_vers = random.choice(list_vers)
  
  chosen_text = requests.get(url).json()['book'][f'{choice_chapter}']['chapter'][f'{choice_vers}']['verse']

  phrase_description = {'phrase':chosen_text, 'book':book.upper(), 'chapter':choice_chapter, 'vers':choice_vers}
  
  return render(request, 'faith.html', phrase_description)


