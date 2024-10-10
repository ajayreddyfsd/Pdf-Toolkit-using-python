from pypdf import PdfReader, PdfWriter

#pdf content printer
#to open and read the file
with open('./twopager.pdf', 'rb') as f:
    reader = PdfReader(f)

    # to read each page and print it
    for page in reader.pages:
        content = page.extract_text()
        print(content)


