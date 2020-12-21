import xml.dom.minidom

tree=xml.dom.minidom.parse("customer.xml")
rootElement=tree.documentElement

customers=rootElement.getElementsByTagName("customer")

for c in customers:
    #print(c.getAttribute('id'))
    print(c.getElementsByTagName("name")[0].childNodes[0].data)
    print(c.getElementsByTagName("email")[0].childNodes[0].data)
    print(c.getElementsByTagName("address")[0].childNodes[0].data)

customers[0].getElementsByTagName("address")[0].childNodes[0].nodeValue="Jaipur"

tree.writexml(open("customer.xml","w"))