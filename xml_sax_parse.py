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
       # print(self.current)
        if self.current == "name":
            self.name=content
        elif self.current == "address":
            self.address=content
        elif self.current == "email":
            self.email=content

    def endElement(self,tag):

        if self.current == "name":
            print(f"Name: {self.name}")
        elif self.current == "address":
            print(f"Address: {self.address}")
        elif self.current == "email":
            print(f"Email: {self.email}")
        else:
            print("")


myhandler=CustomerHandler()
parser=xml.sax.make_parser()
parser.setContentHandler(myhandler)
parser.parse('customer.xml')

