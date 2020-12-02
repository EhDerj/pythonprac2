import struct

def read_struct(fmt, fl):
    return struct.unpack(fmt, fl.read(struct.calcsize(fmt)))

with open(input(), "br") as fl:
    ls = read_struct("4cI12cHHI6cH4cI", fl)
    if b"".join(ls[5:9]) == b"WAVE":
        print(f"Size={ls[4]}, Type={ls[17]}, Channels={ls[18]}, Rate={ls[19]}, Bits={ls[26]}, Data size={ls[31]}")
    else:
        print("NO")