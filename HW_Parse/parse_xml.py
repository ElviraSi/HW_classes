import xml.etree.ElementTree as ET
import collections

parser = ET.XMLParser(encoding="utf-8")
tree = ET.parse("newsafr.xml", parser)
root = tree.getroot()

news_list = root.findall("channel/item/description")

words_list = []
for new in news_list:
    descipt = new.text
    words_list.extend(descipt.split())
words_list = [x.lower() for x in words_list]
words_list_upd = []
for i in words_list:
    if len(i) > 6:
        words_list_upd.append(i)
count_w = collections.Counter(words_list_upd).most_common(10)
print(count_w)
