class HTMLElement:
    def __init__(self,ttext):
        self.text = ttext
    def write(self,file):
        raise NotImplementedError
    
class Heading(HTMLElement):
    def write(self,file):
        file.write('<h1>'+self.text+'</h1>')
        
class Paragraph(HTMLElement):
    def write(self,file):
        file.write('<p>'+self.text+'</p>')