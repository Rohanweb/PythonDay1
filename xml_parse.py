import xml.etree.ElementTree as ET
tree=ET.parse("customer.xml")
print(dir(tree))
root=tree.getroot()
print(dir(root))
print(root.tag)
attr=root.attrib
print(attr)
for c in root.findall('customer'):
    cname = c.find("name")
    email = c.find("email")
    print(cname.text)
    print(email.text)

for item in root.getchildren():
    print(item)