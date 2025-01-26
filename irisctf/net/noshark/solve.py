with open("./noshark.txt", "r") as packets:
    lines = packets.readlines()
    img_data = ""
    OFFSET = len(lines[2]) - 1
    for line in lines:
        if len(line) > len(lines[0]):
            img_data += line[OFFSET:] 

    bytedata = bytes.fromhex(img_data)
    with open("image.jpg", "wb") as imgfile:
        if imgfile.write(bytedata):
            print("suzzess")

