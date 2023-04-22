from PIL import Image
import struct
import sys


def r8(f):
    return ord(f.read(1))

def convert(filename):
    with open(filename, 'rb') as f:
        f.seek(2457600)
        magic = f.read(8)
        f.seek(42, 1)
        dat = f.read(6)
        width, height = struct.unpack('<HxxH', dat)
        print('Size: %dx%d' % (width, height))
        img = Image.new('RGBA', (width, height))

        f.seek(0)
        imgd = img.load()
        for y in range(height):
            for x in range(width):
                b, g, r, a = r8(f), r8(f), r8(f), r8(f)
                imgd[x, y] = (r, g, b, a)
        
        img.save('copied_files/wallpaper.jpg')