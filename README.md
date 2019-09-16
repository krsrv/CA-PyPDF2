Using PyPDF2(http://mstamy2.github.io/PyPDF2/) to create table of content for a PDF. The documentation of PyPDF2 is here: https://pythonhosted.org/PyPDF2/

The documentation for PyPDF2 is not so comprehensive, so I'll list a few things that were not in the docs that I figured out:
1. Bookmarks and Table of Contents are different things - PyPDF2 gives a functionality to set up bookmarks, but you'll have to manually create the table of contents - the hyperlink boxes are difficult to get correct.
2. There are some bugs in ``PyPDF2.PdfFileMerger()``, and you would be better off using ``PyPDF2.PdfFileWriter()``. Iterate through all pages of the PDFs to be added and add them to the new PDF.
3. The ``addLink`` method of ``PyPDF2.PdfFileWriter()`` does not specify the parameters for the border argument and I could not find any relevant documentation. From looking at the source code, what I found is that ``border = [a,b,c]`` represents a box with rounded corners with parameters `a`, `b` (I'm not clear on what they parameterise exactly), while `c` represents the thickness. The `border` argument can also take an array of length 4 as input, but I was not able to figure out what the 4th element does. I do know however, that the 4th element must be an array itself.

In ``latex.py``, I set the parameters ``\itemsep``, ``\topsep``, ``\parsep``, ``\partopsep`` to be the same so that it's a lesser hassle when trying to figure out the rectangle boundaries for the hyperlinks.

The ``contents`` file had the table of contents in an indented format to indicate hierarchy. The code is built around the fact that I have only 3 levels of hierarchy, i.e., topic sub-topic and sub-sub-topic.
