import xmltodict

fin = open('E:\\Sergey\\Python\\stepic\\course1\\temp\\map2.osm', 'r', encoding='utf8')
xml = fin.read()
fin.close()

parsedxml = xmltodict.parse(xml)
# print(parsedxml['osm']['node'][100]['@id'])
cntTag = 0
cntNoTag = 0
for node in (parsedxml['osm']['node']):
    if 'tag' in node:
        # print(node)
        tags = node.get("tag")
        if isinstance(tags, list):
        # tags=node['tag']
        #  if isinstance(tags,list):
             for tag in tags:
                 if '@k' in tag and tag['@k']=='amenity' and tag['@v']=='fuel':
                     cntTag += 1
                     print(cntTag,node)
        elif isinstance(tags, dict):
            if (tags['@v']) == 'fuel':
                print(cntTag, node)
    # print(i)
    # if 'fuel' in i:
    #     cntTag += 1
    # # else:
    # #     cntNoTag += 1
# print(cntTag,cntNoTag)
# print(parsedxml['osm']['node'])
# print(parsedxml)
# print()
# print(parsedxml)
# Tag:amenity=fuel