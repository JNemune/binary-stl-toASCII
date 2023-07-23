# -*- encoding: utf-8 -*-
import struct

infile = open("binary.stl", "rb")  # import file
out = open("ASCII.stl", "w")  # export file

data = infile.read()


out.write("solid ")

for x in range(0, 80):
    if not data[x] == 0:
        out.write(chr(data[x]))
out.write("\n")

number = data[80:84]
faces = struct.unpack("I", number)[0]

for x in range(0, faces):
    out.write("facet normal ")

    xc = data[84 + x * 50 : 88 + x * 50]
    yc = data[88 + x * 50 : 92 + x * 50]
    zc = data[92 + x * 50 : 96 + x * 50]

    out.write(str(struct.unpack("f", xc)[0]) + " ")
    out.write(str(struct.unpack("f", yc)[0]) + " ")
    out.write(str(struct.unpack("f", zc)[0]) + "\n")

    out.write("outer loop\n")

    for y in range(1, 4):
        out.write("vertex ")

        xc = data[84 + y * 12 + x * 50 : 88 + y * 12 + x * 50]
        yc = data[88 + y * 12 + x * 50 : 92 + y * 12 + x * 50]
        zc = data[92 + y * 12 + x * 50 : 96 + y * 12 + x * 50]

        out.write(str(struct.unpack("f", xc)[0]) + " ")
        out.write(str(struct.unpack("f", yc)[0]) + " ")
        out.write(str(struct.unpack("f", zc)[0]) + "\n")

    out.write("endloop\n")
    out.write("endfacet\n")

out.close()
print("end")
