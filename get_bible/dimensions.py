import requests


"""
    ______ _ _     _       ______       _   _              
    | ___ (_) |   | |      | ___ \     | | | |             
    | |_/ /_| |__ | | ___  | |_/ /_   _| |_| |_ ___  _ __  
    | ___ \ | '_ \| |/ _ \ | ___ \ | | | __| __/ _ \| '_ \ 
    | |_/ / | |_) | |  __/ | |_/ / |_| | |_| || (_) | | | |
    \____/|_|_.__/|_|\___| \____/ \__,_|\__|\__\___/|_| |_|
"""


books = ["revelation"]
version = 'valera'

summary_data= {}
aux = []

# for
url = f"https://getbible.net/json?passage={books[0]}&raw=true&version={version}"

summary_data["book"] = books[0] 
summary_data["url"] = url
summary_data["chapters"] = len(requests.get(url).json()['book'])

for i in range(1,len(requests.get(url).json()['book'])+1):
  aux.append(len(requests.get(url).json()['book'][f'{i}']['chapter']))
summary_data["vers"] = aux


print(summary_data)
#: 'h=>: f'h
#valera=>{lenguage}