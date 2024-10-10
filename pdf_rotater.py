from pypdf import PdfReader, PdfWriter

#pdf rotater and content printer
#to open and read the file
with open('./twopager.pdf', 'rb') as f:
    reader = PdfReader(f)
    writer = PdfWriter(f)

    # to read each page and print it
    for page in reader.pages:
        page.rotate(-90)
        writer.add_page(page)
        
    with open('newFile.pdf', 'wb') as f:
        writer.write(f)