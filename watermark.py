'''
write a py script which accepts a pdf file and watermarks it, based on a given watermark pdf file

eg. the command would look like this:
python watermark.py pdf-to-be-watermarked.pdf watermark-pdf.pdf 
       ^arg [0]     ^arg[1]                   ^arg[2] 

'''

import sys
import PyPDF2

template = PyPDF2.PdfFileReader(open('merged.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range (template.getNumPages()):
    page = template.getPage(i) 
    page.mergePage(watermark.getPage(0)) #since watermark.pdf has only one page, index 0 is used
    output.addPage(page)
    
    with open('watermarked-pdf.pdf', 'wb') as file:
        output.write(file)

print('the file has been watermarked!')