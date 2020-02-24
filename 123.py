import xmltodict

fin = open('E:\\Sergey\\Python\\stepic\\course1\\temp\\map1.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()

parsedxml = xmltodict.parse(xml)
# print(parsedxml['osm']['node'][100]['@id'])
cntTag = 0
cntNoTag = 0
for i in (parsedxml['osm']['node']):
    if 'tag' in i:
        cntTag += 1
    else:
        cntNoTag += 1
print(cntTag,cntNoTag)
# print(parsedxml['osm']['node'])
# print(parsedxml)
# print()
# print(parsedxml)