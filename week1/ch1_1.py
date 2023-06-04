from urllib.request import urlopen

shakespeare = urlopen('http://composingprograms.com/shakespeare.txt')   # shakespeare is a http.client.HTTPResponse object

words = set(shakespeare.read().decode().split())