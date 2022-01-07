
def jpeg_res(file_name):
    with open(file_name,'rb') as img_file:
        img_file.seek(163)

        a = img_file.read(2)

        height = (a[0] << 8) + a[1]

        a = img_file.read(2)

        width = (a[0] << 8) + a[1]

    print("Resolution of the image is",width,"x",height)
jpeg_res("windows 10.jpg")