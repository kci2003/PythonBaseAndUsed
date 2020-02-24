from bs4 import BeautifulSoup
from urllib.request import urlopen
import lxml
xml = urlopen("https://stepik.org/media/attachments/lesson/245681/map2.osm").read().decode('utf-8')
content = str(xml)
soup = BeautifulSoup(content, 'lxml').find_all('osm')
s = BeautifulSoup(str(soup), 'lxml').find_all('tag', k='amenity', v='fuel')
cnt = 0
for i in s:
    cnt+=1
    print(cnt,i)
# print(content)
# soup = BeautifulSoup(s,'html.parser')
# soup = BeautifulSoup(content, 'lxml').find_all('node','k'=='amenity','v'=='fuel')
# soup = BeautifulSoup(content, 'lxml').find_all('node','@k'=='amenity')

# for tag in soup.find_all("td"):
#         #print("{0}: {1}".format(tag.name, tag.text))
#         sum = sum + int(tag.text)
print(s)
#print(soup.prettify())
#print(list(soup.children))
# pos = s.find('<a href=')