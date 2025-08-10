from PIL import Image, ImageDraw
a = int(input())
back = input()
dino = input()
print(back, dino)
im = Image.new('RGB', (a * 23, a * 22), color=back)
draw = ImageDraw.Draw(im)
draw.polygon([
    (a * 13, a), (a * 21, a), (a * 21, a * 2), (a * 22, a * 2), (a * 22, a * 6),
    (a * 17, a * 6), (a * 17, a * 7), (a * 20, a * 7), (a * 20, a * 8), (a * 16, a * 8),
    (a * 16, a * 10), (a * 18, a * 10), (a * 18, a * 12), (a * 17, a * 12), (a * 17, a * 11),
    (a * 16, a * 11), (a * 16, a * 13), (a * 15, a * 13), (a * 15, a * 14), (a * 14, a * 14),
    (a * 14, a * 15), (a * 13, a * 15), (a * 13, a * 16), (a * 12, a * 16), (a * 12, a * 20),
    (a * 13, a * 20), (a * 13, a * 21), (a * 11, a * 21), (a * 11, a * 18), (a * 10, a * 18),
    (a * 10, a * 17), (a * 9, a * 17), (a * 9, a * 18), (a * 8, a * 18), (a * 8, a * 19),
    (a * 7, a * 19), (a * 7, a * 20), (a * 8, a * 20), (a * 8, a * 21), (a * 6, a * 21),
    (a * 6, a * 17), (a * 5, a * 17), (a * 5, a * 16), (a * 4, a * 16), (a * 4, a * 15),
    (a * 3, a * 15), (a * 3, a * 14), (a * 2, a * 14), (a * 2, a * 13), (a, a * 13),
    (a, a * 8), (a * 2, a * 8), (a * 2, a * 10), (a * 3, a * 10), (a * 3, a * 11),
    (a * 4, a * 11), (a * 4, a * 12), (a * 6, a * 12), (a * 6, a * 11), (a * 7, a * 11),
    (a * 7, a * 10), (a * 9, a * 10), (a * 9, a * 9), (a * 11, a * 9), (a * 11, a * 8),
    (a * 12, a * 8), (a * 12, a * 2), (a * 13, a * 2), (a * 13, a)
             ], fill=dino)
draw.rectangle((a * 14, a * 2, a * 15, a * 3), fill='white')
im.save('dino.png')

'''20
#FFFFCC
#7F7F7F'''