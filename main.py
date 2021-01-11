import binascii


def Image_to_Code(filename):
    with open(filename, 'rb') as f:
        content = f.read()
    Data = (binascii.hexlify(content))
    #print (Data)
    return(Data)


def Code_to_Image(Data):
    #print (Data)
    #Data = Data[:125158]
    Data1 = binascii.a2b_hex(Data)
    with open('image.bmp', 'wb') as image_file:
        image_file.write(Data1)
        image_file.close

Image_to_Code(filename)
Code_to_Image(Data)