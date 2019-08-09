import urllib.request

url = input("Enter your url here -> ")
print(urllib.request.urlopen(url))