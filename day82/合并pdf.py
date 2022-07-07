from PyPDF2 import PdfFileMerger
import os

pdf_list = os.listdir('/Users/abc/Desktop/第一章')
pdf_list.sort()
print(pdf_list)

# pdfs = ['/Users/abc/Projects/Python/pythoncode/day82/pdf2.pdf', '/Users/abc/Projects/Python/pythoncode/day82/pdf3.pdf']

# merger = PdfFileMerger()
#
# for pdf in pdfs:
#     merger.append(pdf)
#     merger.write("result.pdf")
#
# merger.close()
