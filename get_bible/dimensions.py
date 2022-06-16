import requests


books = ["philippians"]
version = 'valera'

summary_data= {}
aux = []

# for
url = f"https://getbible.net/json?passage={books[0]}&raw=true&version={version}"

summary_data["book"] = books[0] 
summary_data["url"] = url
summary_data["chapter"] = len(requests.get(url).json()['book'])

for i in range(1,len(requests.get(url).json()['book'])+1):
  aux.append(len(requests.get(url).json()['book'][f'{i}']['chapter']))
summary_data["vers"] = aux


print(summary_data)
