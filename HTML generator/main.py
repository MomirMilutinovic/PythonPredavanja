import HTMLGen
import MarkdownGen

file = open('Web.html','a')
file.write('<html>\n<body>')
mfile = open('Nesto.md','a')

mh1 = MHeading('Moj prvi nasolov')
mp1 = MParagraph('Moj prvi paragraf')

h1 = Heading('Moj prvi nasolov')
p1 = Paragraph('Moj prvi paragraf')

h1.write(file)
p1.write(file)
file.close()

mh1.write(mfile)
mp1.write(mfile)
mfile.close()

