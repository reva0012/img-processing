'''
write a py script which accepts multiple pdf files and creates a merged pdf

eg. eg. the command would look like this:
python pdf-merger.py pdf1.pdf pdf2.pdf ...
       ^arg [0]      ^arg[1]  ^arg[2]  ...

'''

import sys
import PyPDF2

#grab a list of all the inputs
input_pdfs = sys.argv[1:] 

def pdf_merger(pdf_list):
    merger = PyPDF2.PdfFileMerger() 
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write('merged.pdf')
        
pdf_merger(input_pdfs)
