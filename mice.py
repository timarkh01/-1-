from PIL import Image, ImageDraw
b = [int(i) for i in input().split()]
a = int(input())
im = Image.new('RGB', (a * 12, a * 12), color='white')
im_final = Image.new('RGB', (a * 12 * len(b), a * 12), color='white')
draw = ImageDraw.Draw(im)
pictures = []
draw.line((a, a * 4.5, a, a * 7.5), width=a // 10, fill='black')
draw.arc(xy=(a * 8.25, a * 6, a * 11.5, a * 9), start=-90, end=50, fill='#747474', width=a // 10)
draw.ellipse((2 * a, a * 2.5, a * 10, a * 9.5), fill='#D1D1D1', outline='#747474')
draw.polygon([
    (0, a * 6), (a * 2, a * 4), (a * 4, a * 4), (a * 4, a * 8), 
    (a * 2, a * 8), (0, a * 6)
               ], fill='#D1D1D1', outline='#747474')
draw.ellipse((a * 3, a * 1.5, a * 6, a * 4.5), fill='#D1D1D1', outline='#747474')
draw.ellipse((a * 3, a * 7.5, a * 6, a * 10.5), fill='#D1D1D1', outline='#747474')
draw.ellipse((a * 3.25, a * 1.75, a * 5.75, a * 4.25), fill='#FCAEBB', outline='#747474')
draw.ellipse((a * 3.25, a * 7.75, a * 5.75, a * 10.25), fill='#FCAEBB', outline='#747474')
draw.ellipse((a * 2, a * 3, a * 4, a * 5), fill='#D1D1D1', outline='#747474')
draw.ellipse((a * 2, a * 7, a * 4, a * 9), fill='#D1D1D1', outline='#747474')
draw.polygon([(0, a * 6), (a * 0.5, a * 5.5), (a * 0.5, a * 6.5), (0, a * 6)], fill='black')
draw.ellipse((a * 1.5, a * 5, a * 2, a * 5.5), fill='black')
draw.ellipse((a * 1.5, a * 6.5, a * 2, a * 7), fill='black')
width = 0
pictures.append(im)
pictures.append(im.transpose(method=Image.Transpose.ROTATE_270))
pictures.append(im.transpose(method=Image.Transpose.ROTATE_90))
pictures.append(im.transpose(method=Image.Transpose.ROTATE_180))
for i in b:
    im_final.paste(pictures[i], (width, 0))
    width += a * 12
im_final.save('mice.png')

