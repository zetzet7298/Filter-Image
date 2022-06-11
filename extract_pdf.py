# STEP 1
# import libraries
import fitz
import io
from PIL import Image, ImageOps

# STEP 2
# file path you want to extract images from
file = "pdf.pdf"

# open the file
pdf_file = fitz.open(file)

# STEP 3
# iterate over PDF pages
print("Bắt đầu export")
for i in range(pdf_file.pageCount):
    for item in pdf_file.get_page_images(i):
        pix = fitz.Pixmap(pdf_file, item[0])  # pixmap from the image xref
        pix0 = fitz.Pixmap(fitz.csRGB, pix)  # force into RGB
        pix0.save(f"album-pdf/image{i+1}_{item[0]}.png")
        #image.save(open(f"pdf-images/image{page_index+1}_{image_index}.png", "wb"))
print("Export hoàn tất")