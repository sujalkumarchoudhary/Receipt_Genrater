from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from datetime import datetime

r_num =int(input("Enter Receipt No.: "))
r_num_new = "Receipt No.: " + str(r_num)
now = datetime.now()
r_datetime = "Date and Time: " + now.strftime("%d/%m/%Y %H:%M:%S")
r_name = "Name: "+ input("Name: ")
r_amount =int(input("Amount: "))
r_amount ="Amount: $"+ str(r_amount)

file_name = "receipt"+str(r_num)+".pdf"
file_name_output = "receipt"+str(r_num)+"_output.pdf"

c = canvas.Canvas(file_name, pagesize= letter)
c.drawString(100,750, r_num_new)
c.drawString(100,735,r_datetime)
c.drawString(100,720,r_name)
c.drawString(100,705,r_amount)

c.save()
with open(file_name,"rb") as f:
    reader = PdfReader(f)
    writer = PdfWriter()

    for page in reader.pages:
        writer.add_page(page)

    with open(file_name_output,"wb") as output_pdf:
        writer.write(output_pdf)