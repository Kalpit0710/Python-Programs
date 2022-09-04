import urllib
import webbrowser
weburl=urllib.request.urlopen('http://www.ted.com/')
html=weburl.read()
data=weburl.getcode()
url=weburl.geturl()
hd=weburl.headers
inf=weburl.info()
print("The url is",url)
print("HTTp status code is:",data)
print("headers returned \n",hd)
print("the info() returned \n".inf)
print("Now opening the url",url)
webbrowser.open_new(url)