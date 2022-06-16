from django.shortcuts import render
import requests
import random


books = [
  {'book': 'ruth', 'url': 'https://getbible.net/json?passage=ruth&raw=true&version=valera', 'chapter': 4, 'vers': [22, 23, 18, 22]},
  {'book': 'philippians', 'url': 'https://getbible.net/json?passage=philippians&raw=true&version=valera', 'chapter': 4, 'vers': [30, 30, 21, 23]}
]


def optimized_bible(request):

  book = random.sample(books,1)[0]
  choice_chapter = random.sample( range(1, book["chapter"]+1), 1 )[0]
  choice_vers = random.sample( range( 1, book["vers"][choice_chapter-1]+1 ), 1 )[0]

  chosen_text = requests.get(book["url"]).json()['book'][f'{choice_chapter}']['chapter'][f'{choice_vers}']['verse']

  phrase_description = {'phrase':chosen_text, 'book':book["book"].upper(), 'chapter':choice_chapter, 'vers':choice_vers}

  return render(request, 'faith.html', phrase_description)