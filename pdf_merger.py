from pypdf import PdfReader, PdfWriter
import sys

pdfs = sys.argv[1:]

def pdfMerger(pdf_list):
    writer = PdfWriter()
    for pdf in pdf_list:
        writer.append(pdf)
    writer.write('super.pdf')
    writer.close()

pdfMerger(pdfs)