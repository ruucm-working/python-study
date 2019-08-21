import urllib.request
proxy = { "http" : "http://91.195.130.237:8080" }
print(urllib.request.urlopen("http://httpbin.org/ip").read())
# print(urllib.request.urlopen("http://httpbin.org/ip", proxies=proxy).read())



import requests
proxies = {"http": "http://91.195.130.237:8080"}
print(requests.get("http://httpbin.org/ip", proxies=proxies).text)