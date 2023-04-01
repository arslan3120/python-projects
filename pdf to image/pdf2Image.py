from pdf2image import convert_from_path


pdf = convert_from_path("null.pdf", poppler_path=r"C:\Users\Administrator\Desktop\python projects\poppler-23.01.0\Library\bin")

for i in range(len(pdf)):
    pdf[i].save("new"+str(i)+".jpg", "JPEG")

