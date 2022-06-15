import requests


books = ["numbers"]
version = 'valera'

bookTouch, urlTouch, chapterTouch, versTouch = [],[],[],[]

# for
url = f"https://getbible.net/json?passage={books[0]}&raw=true&version={version}"

bookTouch.append(books[0])
urlTouch.append(url)
chapterTouch.append(len(requests.get(url).json()['book']))

for i in range(1,len(requests.get(url).json()['book'])+1):
  versTouch.append(len(requests.get(url).json()['book'][f'{i}']['chapter']))


print(bookTouch + urlTouch + chapterTouch + [versTouch])
