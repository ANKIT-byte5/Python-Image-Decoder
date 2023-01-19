import zlib
from PIL import Image
import imghdr

# Open the encoded file in binary mode
with open("imagecache.0", "rb") as f:
    # Decompress the data using zlib
    decompressed_data = zlib.decompress(f.read(), wbits=-zlib.MAX_WBITS)
    # Decode the data using Pillow
    image = Image.open(io.BytesIO(decompressed_data))
    # Resize the image
    image.thumbnail((200,200), Image.ANTIALIAS)
    #get the image format
    image_format = imghdr.what(None, decompressed_data)
    #save the image with its original format
    image.save("decompressed_image"+"."+image_format.lower())
