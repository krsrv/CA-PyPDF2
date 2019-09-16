import PyPDF2 as pdf

inp = pdf.PdfFileReader(open('input.pdf','rb'))
out = pdf.PdfFileWriter()

for i in [1,2]:
	out.addPage(inp.getPage(i))

out.setPageMode("/UseOutlines")

out.addLink(0 , 1, [0, 0, 500, 840],[2,2,2])

book = out.addBookmark("First",1,parent=None)
book = out.addBookmark("Second",0,parent=None)

# out.addLink(0,1,[0,0,1000,1000])
# print(out.getNumPages())

outStream = open('2.pdf','wb+')
out.write(outStream)
outStream.close()




