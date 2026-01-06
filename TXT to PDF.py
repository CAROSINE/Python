from txt_to_pdf(txt_file, pdf_ile):
     c=canvas.Canvas(pdf_file)
     with open(txt_file,"r") as file:
     lines = file.readlines()

y=800
for line in lines
    c.drawString(100,y,line.strip())
    y-= 20
    c.save()

    txt_to_pdf("codabot.txt", "collection.pdf")