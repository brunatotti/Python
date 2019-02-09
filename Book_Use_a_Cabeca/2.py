#1
import urllib.request
page = urllib.request.urlopen("http://www.beans-r-us.biz/prices")
text = page.read().decode("utf8")
price = text[203:205] 
print (price)

#2
import urllib.request
page = urllib.request.urlopen("http://www.beans-r-us.biz/prices-loyalty")
text = page.read().decode("utf8")
price = text[203:205] 
print (price)

#3 uppercase
import urllib.request
page = urllib.request.urlopen("http://www.beans-r-us.biz/prices-loyalty")
text = page.read().decode("utf8")
price = text[200:300]
print (price.upper())

#3b lowercase
import urllib.request
page = urllib.request.urlopen("http://www.beans-r-us.biz/prices-loyalty")
text = page.read().decode("utf8")
price = text[200:300]
print (price.lower())

#3c replace text
import urllib.request
page = urllib.request.urlopen("http://www.beans-r-us.biz/prices-loyalty")
text = page.read().decode("utf8")
price = text[200:300]
print (price.replace("1K8rXxK/TvX/XYBdVZRQfrXLJ47Y/P9pTM1BF/oG143GZiE3tHzWwEotVPyqYw==><head><meta charset=utf-8><title>be", "Hello"))

#3d retorna a posicao da string que o texto comeca
import urllib.request
page = urllib.request.urlopen("http://www.beans-r-us.biz/prices-loyalty")
text = page.read().decode("utf8")
price = text[200:300]
print (price.find("TvX"))

#3e
import urllib.request
page = urllib.request.urlopen("http://www.beans-r-us.biz/prices-loyalty")
text = page.read().decode("utf8")
price = text[200:300]
print (price.endswith(">be"))

#3f
import urllib.request
page = urllib.request.urlopen("http://www.beans-r-us.biz/prices-loyalty")
text = page.read().decode("utf8")
price = text[200:300]
print (price.strip())

#3g
import urllib.request
page = urllib.request.urlopen("http://www.beans-r-us.biz/prices-loyalty")
text = page.read().decode("utf8")
price = text[200:300]
print (price.startswith("1K8"))
print (price.startswith("abc"))

#4
import urllib.request
page = urllib.request.urlopen("http://www.beans-r-us.biz/prices-loyalty")
text = page.read().decode("utf8")
where = text.find("<html")
print(where)
a = where + 2
print(a)
b = a + 4
print(b)
price = text[a:b]
print(price)













