from pypdf import PdfReader, PdfWriter

'''
logic
-----
get each page from the pdf, and get the single page from watermark.pdf
and use page.page_merge() to merge both of them page to page

then
----
add all those pages to writer (it stores all of them internally)
and finally write them?
'''


def pdfWatermarker(input_pdf, watermark_pdf, output_pdf):

    with open(input_pdf, 'rb') as input_pdf, open(watermark_pdf, 'rb') as watermark_pdf:
        pdf_reader = PdfReader(input_pdf)
        watermark_reader = PdfReader(watermark_pdf)
        writer = PdfWriter()

        for page in pdf_reader.pages:
            page.merge_page(watermark_reader.pages[0])
            writer.add_page(page)

    with open(output_pdf, 'wb') as f:
        writer.write(f)


pdfWatermarker('./twopage.pdf', './watermark.pdf', './output.pdf')