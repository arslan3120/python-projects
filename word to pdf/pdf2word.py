from pdf2docx import Converter

old = "null.pdf"
new = "new.docx"

object = Converter(old)
object.convert(new)
object.close()
