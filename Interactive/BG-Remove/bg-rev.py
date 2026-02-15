from PIL import Image
from rembg import remove

imgfile=Image.open("Interactive/BG-Remove/img.jpg")
outputFile=remove(imgfile)
outputFile.save("Interactive/BG-Remove/output.png")