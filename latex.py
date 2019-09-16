with open('contents','r') as f:
  olist = False
  ilist = False
  print("\\documentclass{article}")
  print("\\usepackage[legalpaper, margin=1in]{geometry}")
  print("\\usepackage{enumitem}")
  print("\\setlist[itemize]{itemsep=1.2pt, topsep=1.2pt, parsep=1.2pt, partopsep=1.2pt}")
  print("\\begin{document}")
  print("\\begin{flushleft}")
  print("\\begin{itemize}")
  for line in f:
    title, page = line.split(',')
    title.replace('#','')
    page = int(page.strip())-1
    if title[:4] == "Part":
      if ilist == True:
        print("\\end{itemize}")
        ilist = False
      if olist == True:
        print("\\end{itemize}")
        olist = False

      print("\\item " + title)
    elif title[:2] == '  ':
      title = title.strip()
      if ilist == False:
        print("\\begin{itemize}")
        ilist = True
      
      print("\\item " + title)
    else:
      if olist == False:
        print("\\begin{itemize}")
        olist = True
      if ilist == True:
        print("\\end{itemize}")
        ilist = False
      
      print("\\item " + title)

  if ilist == True:
    print("\\end{itemize}")
    ilist = False
  if olist == True:
    print("\\end{itemize}")
    olist = False
  print("\\end{itemize}")
  print("\\end{flushleft}")
  print("\\end{document}")