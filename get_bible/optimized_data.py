from django.shortcuts import render
import requests
import random


def optimized_bible(request):


  if request.GET.get("idiom") == None:
    language = "valera"
  if request.GET.get("idiom") == "valera":
    language = "valera"
  if request.GET.get("idiom") == "asv":
    language = "asv"
  if request.GET.get("idiom") == "ostervald":
    language = "ostervald"


  books = [
    {'book': 'genesis', 'url': f'https://getbible.net/json?passage=genesis&raw=true&version={language}', 'chapters': 50, 'vers': [31, 25, 24, 26, 32, 22, 24, 22, 29, 32, 32, 20, 18, 24, 21, 16, 27, 33, 38, 18, 34, 24, 20, 67, 34, 35, 46, 22, 35, 43, 55, 32, 20, 31, 29, 43, 36, 30, 23, 23, 57, 38, 34, 34, 28, 34, 31, 22, 33, 26]},
    {'book': 'exodus', 'url': f'https://getbible.net/json?passage=exodus&raw=true&version={language}', 'chapters': 40, 'vers': [22, 25, 22, 31, 23, 30, 25, 32, 35, 29, 10, 51, 22, 31, 27, 36, 16, 27, 25, 26, 36, 31, 33, 18, 40, 37, 21, 43, 46, 38, 18, 35, 23, 35, 35, 38, 29, 31, 43, 38]},
    {'book': 'leviticus', 'url': f'https://getbible.net/json?passage=leviticus&raw=true&version={language}', 'chapters': 27, 'vers': [17, 16, 17, 35, 19, 30, 38, 36, 24, 20, 47, 8, 59, 57, 33, 34, 16, 30, 37, 27, 24, 33, 44, 23, 55, 46, 34]},
    {'book': 'numbers', 'url': f'https://getbible.net/json?passage=numbers&raw=true&version={language}', 'chapters': 36, 'vers': [54, 34, 51, 49, 31, 27, 89, 26, 23, 36, 35, 16, 33, 45, 41, 50, 13, 32, 22, 29, 35, 41, 30, 25, 18, 65, 23, 31, 40, 16, 54, 42, 56, 29, 34, 13]},
    {'book': 'deuteronomy', 'url': f'https://getbible.net/json?passage=deuteronomy&raw=true&version={language}', 'chapters': 34, 'vers': [46, 37, 29, 49, 33, 25, 26, 20, 29, 22, 32, 32, 18, 29, 23, 22, 20, 22, 21, 20, 23, 30, 25, 22, 19, 19, 26, 68, 29, 20, 30, 52, 29, 12]},
    {'book': 'joshua', 'url': f'https://getbible.net/json?passage=joshua&raw=true&version={language}', 'chapters': 24, 'vers': [18, 24, 17, 24, 15, 27, 26, 35, 27, 43, 23, 24, 33, 15, 63, 10, 18, 28, 51, 9, 45, 34, 16, 33]},
    {'book': 'judges', 'url': f'https://getbible.net/json?passage=judges&raw=true&version={language}', 'chapters': 21, 'vers': [36, 23, 31, 24, 31, 40, 25, 35, 57, 18, 40, 15, 25, 20, 20, 31, 13, 31, 30, 48, 25]},
    {'book': 'ruth', 'url': f'https://getbible.net/json?passage=ruth&raw=true&version={language}', 'chapters': 4, 'vers': [22, 23, 18, 22]},
    {'book': '1samuel', 'url': f'https://getbible.net/json?passage=1samuel&raw=true&version={language}', 'chapters': 31, 'vers': [28, 36, 21, 22, 12, 21, 17, 22, 27, 27, 15, 25, 23, 52, 35, 23, 58, 30, 24, 42, 15, 23, 29, 22, 44, 25, 12, 25, 11, 31, 13]},
    {'book': '2samuel', 'url': f'https://getbible.net/json?passage=2samuel&raw=true&version={language}', 'chapters': 24, 'vers': [27, 32, 39, 12, 25, 23, 29, 18, 13, 19, 27, 31, 39, 33, 37, 23, 29, 33, 43, 26, 22, 51, 39, 25]},
    {'book': '1kings', 'url': f'https://getbible.net/json?passage=1kings&raw=true&version={language}', 'chapters': 22, 'vers': [53, 46, 28, 34, 18, 38, 51, 66, 28, 29, 43, 33, 34, 31, 34, 34, 24, 46, 21, 43, 29, 53]},
    {'book': '2kings', 'url': f'https://getbible.net/json?passage=2kings&raw=true&version={language}', 'chapters': 25, 'vers': [18, 25, 27, 44, 27, 33, 20, 29, 37, 36, 21, 21, 25, 29, 38, 20, 41, 37, 37, 21, 26, 20, 37, 20, 30]},
    {'book': '1chronicles', 'url': f'https://getbible.net/json?passage=1chronicles&raw=true&version={language}', 'chapters': 29, 'vers': [54, 55, 24, 43, 26, 81, 40, 40, 44, 14, 47, 40, 14, 17, 29, 43, 27, 17, 19, 8, 30, 19, 32, 31, 31, 32, 34, 21, 30]},
    {'book': '2chronicles', 'url': f'https://getbible.net/json?passage=2chronicles&raw=true&version={language}', 'chapters': 36, 'vers': [17, 18, 17, 22, 14, 42, 22, 18, 31, 19, 23, 16, 22, 15, 19, 14, 19, 34, 11, 37, 20, 12, 21, 27, 28, 23, 9, 27, 36, 27, 21, 33, 25, 33, 27, 23]},
    {'book': 'ezra', 'url': f'https://getbible.net/json?passage=ezra&raw=true&version={language}', 'chapters': 10, 'vers': [11, 70, 13, 24, 17, 22, 28, 36, 15, 44]},
    {'book': 'nehemiah', 'url': f'https://getbible.net/json?passage=nehemiah&raw=true&version={language}', 'chapters': 13, 'vers': [11, 20, 32, 23, 19, 19, 73, 18, 38, 39, 36, 47, 31]},
    {'book': 'esther', 'url': f'https://getbible.net/json?passage=esther&raw=true&version={language}', 'chapters': 10, 'vers': [22, 23, 15, 17, 14, 14, 10, 17, 32, 3]},
    {'book': 'job', 'url': f'https://getbible.net/json?passage=job&raw=true&version={language}', 'chapters': 42, 'vers': [22, 13, 26, 21, 27, 30, 21, 22, 35, 22, 20, 25, 28, 22, 35, 22, 16, 21, 29, 29, 34, 30, 17, 25, 6, 14, 23, 28, 25, 31, 40, 22, 33, 37, 16, 33, 24, 41, 30, 24, 34, 17]},
    {'book': 'psalms', 'url': f'https://getbible.net/json?passage=psalms&raw=true&version={language}', 'chapters': 150, 'vers': [6, 12, 8, 8, 12, 10, 17, 9, 20, 18, 7, 8, 6, 7, 5, 11, 15, 50, 14, 9, 13, 31, 6, 10, 22, 12, 14, 9, 11, 12, 24, 11, 22, 22, 28, 12, 40, 22, 13, 17, 13, 11, 5, 26, 17, 11, 9, 14, 20, 23, 19, 9, 6, 7, 23, 13, 11, 11, 17, 12, 8, 12, 11, 10, 13, 20, 7, 35, 36, 5, 24, 20, 28, 23, 10, 12, 20, 72, 13, 19, 16, 8, 18, 12, 13, 17, 7, 18, 52, 17, 16, 15, 5, 23, 11, 13, 12, 9, 9, 5, 8, 28, 22, 35, 45, 48, 43, 13, 31, 7, 10, 10, 9, 8, 18, 19, 2, 29, 176, 7, 8, 9, 4, 8, 5, 6, 5, 6, 8, 8, 3, 18, 3, 3, 21, 26, 9, 8, 24, 13, 10, 7, 12, 15, 21, 10, 20, 14, 9, 6]},
    {'book': 'proverbs', 'url': f'https://getbible.net/json?passage=proverbs&raw=true&version={language}', 'chapters': 31, 'vers': [33, 22, 35, 27, 23, 35, 27, 36, 18, 32, 31, 28, 25, 35, 33, 33, 28, 24, 29, 30, 31, 29, 35, 34, 28, 28, 27, 28, 27, 33, 31]},
    {'book': 'ecclesiastes', 'url': f'https://getbible.net/json?passage=ecclesiastes&raw=true&version={language}', 'chapters': 12, 'vers': [18, 26, 22, 16, 20, 12, 29, 17, 18, 20, 10, 14]},
    {'book': 'songofsongs', 'url': f'https://getbible.net/json?passage=songofsongs&raw=true&version={language}', 'chapters': 8, 'vers': [17, 17, 11, 16, 16, 13, 13, 14]},
    {'book': 'isaiah', 'url': f'https://getbible.net/json?passage=isaiah&raw=true&version={language}', 'chapters': 66, 'vers': [31, 22, 26, 6, 30, 13, 25, 22, 21, 34, 16, 6, 22, 32, 9, 14, 14, 7, 25, 6, 17, 25, 18, 23, 12, 21, 13, 29, 24, 33, 9, 20, 24, 17, 10, 22, 38, 22, 8, 31, 29, 25, 28, 28, 25, 13, 15, 22, 26, 11, 23, 15, 12, 17, 13, 12, 21, 14, 21, 22, 11, 12, 19, 12, 25, 24]},
    {'book': 'jeremiah', 'url': f'https://getbible.net/json?passage=jeremiah&raw=true&version={language}', 'chapters': 52, 'vers': [19, 37, 25, 31, 31, 30, 34, 22, 26, 25, 23, 17, 27, 22, 21, 21, 27, 23, 15, 18, 14, 30, 40, 10, 38, 24, 22, 17, 32, 24, 40, 44, 26, 22, 19, 32, 21, 28, 18, 16, 18, 22, 13, 30, 5, 28, 7, 47, 39, 46, 64, 34]},
    {'book': 'lamentations', 'url': f'https://getbible.net/json?passage=lamentations&raw=true&version={language}', 'chapters': 5, 'vers': [22, 22, 66, 22, 22]},
    {'book': 'ezekiel', 'url': f'https://getbible.net/json?passage=ezekiel&raw=true&version={language}', 'chapters': 48, 'vers': [28, 10, 27, 17, 17, 14, 27, 18, 11, 22, 25, 28, 23, 23, 8, 63, 24, 32, 14, 49, 32, 31, 49, 27, 17, 21, 36, 26, 21, 26, 18, 32, 33, 31, 15, 38, 28, 23, 29, 49, 26, 20, 27, 31, 25, 24, 23, 35]},
    {'book': 'daniel', 'url': f'https://getbible.net/json?passage=daniel&raw=true&version={language}', 'chapters': 12, 'vers': [21, 49, 30, 37, 31, 28, 28, 27, 27, 21, 45, 13]},
    {'book': 'hosea', 'url': f'https://getbible.net/json?passage=hosea&raw=true&version={language}', 'chapters': 14, 'vers': [11, 23, 5, 19, 15, 11, 16, 14, 17, 15, 12, 14, 16, 9]},
    {'book': 'joel', 'url': f'https://getbible.net/json?passage=joel&raw=true&version={language}', 'chapters': 3, 'vers': [20, 32, 21]},
    {'book': 'amos', 'url': f'https://getbible.net/json?passage=amos&raw=true&version={language}', 'chapters': 9, 'vers': [15, 16, 15, 13, 27, 14, 17, 14, 15]},
    {'book': 'obadiah', 'url': f'https://getbible.net/json?passage=obadiah&raw=true&version={language}', 'chapters': 1, 'vers': [21]},
    {'book': 'jonah', 'url': f'https://getbible.net/json?passage=jonah&raw=true&version={language}', 'chapters': 4, 'vers': [17, 10, 10, 11]},
    {'book': 'micah', 'url': f'https://getbible.net/json?passage=micah&raw=true&version={language}', 'chapters': 7, 'vers': [16, 13, 12, 13, 15, 16, 20]},
    {'book': 'nahum', 'url': f'https://getbible.net/json?passage=nahum&raw=true&version={language}', 'chapters': 3, 'vers': [15, 13, 19]},
    {'book': 'habakkuk', 'url': f'https://getbible.net/json?passage=habakkuk&raw=true&version={language}', 'chapters': 3, 'vers': [17, 20, 19]},
    {'book': 'zephaniah', 'url': f'https://getbible.net/json?passage=zephaniah&raw=true&version={language}', 'chapters': 3, 'vers': [18, 15, 20]},
    {'book': 'haggai', 'url': f'https://getbible.net/json?passage=haggai&raw=true&version={language}', 'chapters': 2, 'vers': [15, 23]},
    {'book': 'zechariah', 'url': f'https://getbible.net/json?passage=zechariah&raw=true&version={language}', 'chapters': 14, 'vers': [21, 13, 10, 14, 11, 15, 14, 23, 17, 12, 17, 14, 9, 21]},
    {'book': 'malachi', 'url': f'https://getbible.net/json?passage=malachi&raw=true&version={language}', 'chapters': 4, 'vers': [14, 17, 18, 6]},
    {'book': 'matthew', 'url': f'https://getbible.net/json?passage=matthew&raw=true&version={language}', 'chapters': 28, 'vers': [25, 23, 17, 25, 48, 34, 29, 34, 38, 42, 30, 50, 58, 36, 39, 28, 27, 35, 30, 34, 46, 46, 39, 51, 46, 75, 66, 20]},
    {'book': 'mark', 'url': f'https://getbible.net/json?passage=mark&raw=true&version={language}', 'chapters': 16, 'vers': [45, 28, 35, 41, 43, 56, 37, 38, 50, 52, 33, 44, 37, 72, 47, 20]},
    {'book': 'luke', 'url': f'https://getbible.net/json?passage=luke&raw=true&version={language}', 'chapters': 24, 'vers': [80, 52, 38, 44, 39, 49, 50, 56, 62, 42, 54, 59, 35, 35, 32, 31, 37, 43, 48, 47, 38, 71, 56, 53]},
    {'book': 'john', 'url': f'https://getbible.net/json?passage=john&raw=true&version={language}', 'chapters': 21, 'vers': [51, 25, 36, 54, 47, 71, 53, 59, 41, 42, 57, 50, 38, 31, 27, 33, 26, 40, 42, 31, 25]},
    {'book': 'acts', 'url': f'https://getbible.net/json?passage=acts&raw=true&version={language}', 'chapters': 28, 'vers': [26, 47, 26, 37, 42, 15, 60, 40, 43, 48, 30, 25, 52, 28, 41, 40, 34, 28, 41, 38, 40, 30, 35, 27, 27, 32, 44, 31]},
    {'book': 'romans', 'url': f'https://getbible.net/json?passage=romans&raw=true&version={language}', 'chapters': 16, 'vers': [32, 29, 31, 25, 21, 23, 25, 39, 33, 21, 36, 21, 14, 23, 33, 27]},
    {'book': '1corinthians', 'url': f'https://getbible.net/json?passage=1corinthians&raw=true&version={language}', 'chapters': 16, 'vers': [31, 16, 23, 21, 13, 20, 40, 13, 27, 33, 34, 31, 13, 40, 58, 24]},
    {'book': '2corinthians', 'url': f'https://getbible.net/json?passage=2corinthians&raw=true&version={language}', 'chapters': 13, 'vers': [24, 17, 18, 18, 21, 18, 16, 24, 15, 18, 33, 21, 14]},
    {'book': 'galatians', 'url': f'https://getbible.net/json?passage=galatians&raw=true&version={language}', 'chapters': 6, 'vers': [24, 21, 29, 31, 26, 18]},
    {'book': 'ephesians', 'url': f'https://getbible.net/json?passage=ephesians&raw=true&version={language}', 'chapters': 6, 'vers': [23, 22, 21, 32, 33, 24]},
    {'book': 'philippians', 'url': f'https://getbible.net/json?passage=philippians&raw=true&version={language}', 'chapters': 4, 'vers': [30, 30, 21, 23]},
    {'book': 'colossians', 'url': f'https://getbible.net/json?passage=colossians&raw=true&version={language}', 'chapters': 4, 'vers': [29, 23, 25, 18]}
]


  b,c,v = 0,0,0
  for i in books:
    b += 1
    c += i["chapters"]
    v += sum(i["vers"])
    
  print("Total books so far: ", b)
  print("Total chapters so far: ", c)
  print("Total vers so far: ", v)
  
  
  
  book = random.sample(books,1)[0]
  choice_chapter = random.sample( range(1, book["chapters"]+1), 1 )[0]
  choice_vers = random.sample( range( 1, book["vers"][choice_chapter-1]+1 ), 1 )[0]
  
  chosen_text = requests.get(book["url"]).json()['book'][f'{choice_chapter}']['chapter'][f'{choice_vers}']['verse']
  
  phrase_description = {'phrase':chosen_text, 'book':book["book"].upper(), 'chapter':choice_chapter, 'vers':choice_vers}

  return render(request, 'faith.html', phrase_description)



