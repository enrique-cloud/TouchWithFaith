from django.shortcuts import render
import requests
import random
import time


books=["leviticus","hebrews","mark","luke","matthew","john","revelation","romans","numbers"]    # add more books
version='valera' # asv, valera, there are more versions (lenguages)


def url_build(books_,version_):
  book_ = random.sample(books_,1)[0]
  url_ = f"https://getbible.net/json?passage={book_}&raw=true&version={version_}"
  return url_, book_


def chapter(url_):
  len_chapter = len(requests.get(url_).json()['book'])+1
  list_chapters = range(1,len_chapter)
  choice_chapter = random.sample(list_chapters,1)[0]
  return choice_chapter


def vers(url_, choice_chapter_):
  len_vers = len(requests.get(url_).json()['book'][f'{choice_chapter_}']['chapter'])+1
  list_vers = range(1,len_vers)
  choice_vers = random.sample(list_vers,1)[0]
  return choice_vers


def bible(request):
  url = url_build(books, version)[0]
  print(time.time())
  book = url_build(books, version)[1]
  print(time.time())
  
  choice_chapter = chapter(url)
  print(time.time())
  choice_vers = vers(url, choice_chapter)
  print(time.time())
  
  chosen_text = requests.get(url).json()['book'][f'{choice_chapter}']['chapter'][f'{choice_vers}']['verse']
  print(time.time())

  phrase_description = {'phrase':chosen_text, 'book':book.upper(), 'chapter':choice_chapter, 'vers':choice_vers}

  return render(request, 'faith.html', phrase_description)


