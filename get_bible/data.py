from django.shortcuts import render
import requests
import random


books=["leviticus","hebrews","mark"]    # add more books
version='valera' # asv, valera, there are more versions (lenguages)

def bible(request):
  book = random.choice(books)
  url_hebrews = f"https://getbible.net/json?passage={book}&raw=true&version={version}"
  
  list_chapters = list(range(1,len(requests.get(url_hebrews).json()['book'])+1))
  choice_chapter = random.choice(list_chapters)
  
  list_vers = list(range(1,len(requests.get(url_hebrews).json()['book'][f'{choice_chapter}']['chapter'])+1))
  choice_vers = random.choice(list_vers)
  
  chosen_text = requests.get(url_hebrews).json()['book'][f'{choice_chapter}']['chapter'][f'{choice_vers}']['verse']

  phrase_description = {'phrase':chosen_text, 'book':book.upper(), 'chapter':choice_chapter, 'vers':choice_vers}
  
  return render(request, 'faith.html', phrase_description)


