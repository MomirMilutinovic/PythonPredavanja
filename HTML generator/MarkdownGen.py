class MarkdownElement:
    def __init__(self,ttext):
        self.text = ttext
    def write(self,file):
        raise NotImplementedError
        
class MHeading(MarkdownElement):
    def write(self,file):
        file.write('#'+self.text+'\n')
        
class MParagraph(MarkdownElement):
    def write(self,file):
        file.write(self.text+'\n')

