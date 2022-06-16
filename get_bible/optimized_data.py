from django.shortcuts import render
import requests
import random


lenguage = "valera"

books = [
  {'book': 'genesis', 'url': f'https://getbible.net/json?passage=genesis&raw=true&version={lenguage}', 'chapter': 50, 'vers': [31, 25, 24, 26, 32, 22, 24, 22, 29, 32, 32, 20, 18, 24, 21, 16, 27, 33, 38, 18, 34, 24, 20, 67, 34, 35, 46, 22, 35, 43, 55, 32, 20, 31, 29, 43, 36, 30, 23, 23, 57, 38, 34, 34, 28, 34, 31, 22, 33, 26]},
  {'book': 'exodus', 'url': f'https://getbible.net/json?passage=exodus&raw=true&version={lenguage}', 'chapter': 40, 'vers': [22, 25, 22, 31, 23, 30, 25, 32, 35, 29, 10, 51, 22, 31, 27, 36, 16, 27, 25, 26, 36, 31, 33, 18, 40, 37, 21, 43, 46, 38, 18, 35, 23, 35, 35, 38, 29, 31, 43, 38]},
  {'book': 'leviticus', 'url': f'https://getbible.net/json?passage=leviticus&raw=true&version={lenguage}', 'chapter': 27, 'vers': [17, 16, 17, 35, 19, 30, 38, 36, 24, 20, 47, 8, 59, 57, 33, 34, 16, 30, 37, 27, 24, 33, 44, 23, 55, 46, 34]},
  {'book': 'numbers', 'url': f'https://getbible.net/json?passage=numbers&raw=true&version={lenguage}', 'chapter': 36, 'vers': [54, 34, 51, 49, 31, 27, 89, 26, 23, 36, 35, 16, 33, 45, 41, 50, 13, 32, 22, 29, 35, 41, 30, 25, 18, 65, 23, 31, 40, 16, 54, 42, 56, 29, 34, 13]},
  {'book': 'deuteronomy', 'url': f'https://getbible.net/json?passage=deuteronomy&raw=true&version={lenguage}', 'chapter': 34, 'vers': [46, 37, 29, 49, 33, 25, 26, 20, 29, 22, 32, 32, 18, 29, 23, 22, 20, 22, 21, 20, 23, 30, 25, 22, 19, 19, 26, 68, 29, 20, 30, 52, 29, 12]},
  {'book': 'joshua', 'url': f'https://getbible.net/json?passage=joshua&raw=true&version={lenguage}', 'chapter': 24, 'vers': [18, 24, 17, 24, 15, 27, 26, 35, 27, 43, 23, 24, 33, 15, 63, 10, 18, 28, 51, 9, 45, 34, 16, 33]},
  {'book': 'judges', 'url': f'https://getbible.net/json?passage=judges&raw=true&version={lenguage}', 'chapter': 21, 'vers': [36, 23, 31, 24, 31, 40, 25, 35, 57, 18, 40, 15, 25, 20, 20, 31, 13, 31, 30, 48, 25]},
  {'book': 'ruth', 'url': f'https://getbible.net/json?passage=ruth&raw=true&version={lenguage}', 'chapter': 4, 'vers': [22, 23, 18, 22]},
  {'book': '1samuel', 'url': f'https://getbible.net/json?passage=1samuel&raw=true&version={lenguage}', 'chapter': 31, 'vers': [28, 36, 21, 22, 12, 21, 17, 22, 27, 27, 15, 25, 23, 52, 35, 23, 58, 30, 24, 42, 15, 23, 29, 22, 44, 25, 12, 25, 11, 31, 13]},
  {'book': '2samuel', 'url': f'https://getbible.net/json?passage=2samuel&raw=true&version={lenguage}', 'chapter': 24, 'vers': [27, 32, 39, 12, 25, 23, 29, 18, 13, 19, 27, 31, 39, 33, 37, 23, 29, 33, 43, 26, 22, 51, 39, 25]}
]


# c = 0
# for i in books:
#   c += sum(i["vers"])
# print("Total vers so far: ", c)


def optimized_bible(request):

  book = random.sample(books,1)[0]
  choice_chapter = random.sample( range(1, book["chapter"]+1), 1 )[0]
  choice_vers = random.sample( range( 1, book["vers"][choice_chapter-1]+1 ), 1 )[0]

  chosen_text = requests.get(book["url"]).json()['book'][f'{choice_chapter}']['chapter'][f'{choice_vers}']['verse']

  phrase_description = {'phrase':chosen_text, 'book':book["book"].upper(), 'chapter':choice_chapter, 'vers':choice_vers}

  return render(request, 'faith.html', phrase_description)