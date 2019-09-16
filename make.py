import PyPDF2 as pdf

output = pdf.PdfFileWriter()
inputs = [pdf.PdfFileReader('table.pdf'), pdf.PdfFileReader('CA.pdf')]

# Add the table of contents - table.pdf
# Generated using latex.py
for page in range(inputs[0].numPages):
  output.addPage(inputs[0].getPage(page))

# Add the actual document - CA.pdf
for page in range(inputs[1].numPages):
  output.addPage(inputs[1].getPage(page))

# Required for boxes
voffset = 936
loffset = 50
height, width = 13, 500

# Contents stores the topics in lines
# Topic,Pg.#
# Example:
# Global Warming,48
# Computers,23
with open('contents','r') as f:
  pbook = None
  cbook = None
  count = 0

  for line in f:
    title, page = line.split(',')
    # Add and subtract offsets due to additional pages because of table.pdf
    page = int(page.strip())-1+3

    # Link on which page in table of contents
    link_page = 0 if count <= 59 else 1 if count <= 119 else 2
    # print(title, page, count)
    
    if title[:4] == "Part":
      pbook = output.addBookmark(title, page, parent=None)
      
      # print(title, page)
    elif title[:2] == '  ':
      title = title.strip()
      output.addBookmark(title, page, parent=cbook)
      
      # Add boxes for each hyperlink
      add_offset = 14.33 * (count % 60)
      output.addLink(link_page, page, [loffset, voffset-height-add_offset, loffset+width, voffset-add_offset], [2,2,2])
      
      # print('\t\t',title.strip(),page)
    else:
      cbook = output.addBookmark(title, page, parent=pbook)
      
      # Add boxes for each hyperlink
      add_offset = 14.33 * (count % 60)
      output.addLink(link_page, page, [loffset, voffset-height-add_offset, loffset+width, voffset-add_offset], [2,2,2])
      
      # print('\t',title,page)

    count += 1

output.setPageMode("/UseOutlines")

outputStream = open('result.pdf', 'wb')
output.write(outputStream)

outputStream.close()
