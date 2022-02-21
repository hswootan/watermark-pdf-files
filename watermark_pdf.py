from re import template
import PyPDF2

template = PyPDF2.PdfFileReader(open('mypdf.pdf', 'rb'))
watermark = PyPDF2.PdfFileReader(open('wtr.pdf', 'rb'))
output = PyPDF2.PdfFileWriter()

for i in range(template.numPages):
    page = template.getPage(i)
    page.mergePage(watermark.getPage(0))
    output.addPage(page)

    with open('watermarked.pdf', 'wb') as f:
        output.write(f)
