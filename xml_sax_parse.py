import xml.sax

class CustomerHandler(xml.sax.ContentHandler):

    def startElement(self,tag,attrs):
        self.current=tag
        # if self.current == "customer":
        #     print("########### Customer ###########")
        #     print(f'{attrs["id"]}')

    # def startDocument(self):
    #     print("XML document started parsing")
    #
    # def endDocument(self):
    #     print("XML document parsing completed ")

    def characters(self,content):
        #print(self.current)
        if self.current == "name":
            self.name=content
        elif self.current == "address":
            self.address=content
        elif self.current == "email":
            self.email=content

    def endElement(self,tag):

        if tag == "name":
            print(f"Name: {self.name}")
        elif tag == "address":
            print(f"Address: {self.address}")
        elif tag == "email":
            print(f"Email: {self.email}")
        else:
            self.current=""

myhandler=CustomerHandler()
parser=xml.sax.make_parser()
parser.setContentHandler(myhandler)
parser.parse('customer.xml')

