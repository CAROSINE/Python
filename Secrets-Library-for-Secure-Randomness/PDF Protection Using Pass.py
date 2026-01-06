from PyPDF2 import PdfReader, PdfWriter
import getpass

def protect_pdf(input_pdf, output_pdf):
    reader = PdfReader('input.pdf')
    writer = PdfWriter()

    for page in reader.pages:
       writer.add_page(page)

    password = getpass.getpass("Enter Password: ")
    writer.encrypt(password)
    with open(output_pdf, "wb") as output_file:
        writer.write(output_file)
        print(f"The PDF has password_  {output_pdf}")
              
 protect_pdf("clcoding.pdf, "protect_file.pdf)