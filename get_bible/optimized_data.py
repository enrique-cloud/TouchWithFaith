from django.shortcuts import render
import requests
import random


books = [
  ['leviticus', 'https://getbible.net/json?passage=leviticus&raw=true&version=valera', 27, [17, 16, 17, 35, 19, 30, 38, 36, 24, 20, 47, 8, 59, 57, 33, 34, 16, 30, 37, 27, 24, 33, 44, 23, 55, 46, 34]],
  ['numbers', 'https://getbible.net/json?passage=numbers&raw=true&version=valera', 36, [54, 34, 51, 49, 31, 27, 89, 26, 23, 36, 35, 16, 33, 45, 41, 50, 13, 32, 22, 29, 35, 41, 30, 25, 18, 65, 23, 31, 40, 16, 54, 42, 56, 29, 34, 13]]
]



def optimized_bible(request):

  book = random.sample(books,1)[0]
  # print(book)

  choice_chapter = random.sample( range(1, book[2]+1), 1 )[0]
  # print(choice_chapter)
  
  choice_vers = random.sample( range( 1, book[3][choice_chapter-1]+1 ), 1 )[0]
  # print(choice_vers)

  chosen_text = requests.get(book[1]).json()['book'][f'{choice_chapter}']['chapter'][f'{choice_vers}']['verse']

  phrase_description = {'phrase':chosen_text, 'book':book[0].upper(), 'chapter':choice_chapter, 'vers':choice_vers}

  return render(request, 'faith.html', phrase_description)