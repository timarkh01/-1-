from PIL import Image, ImageDraw
a = int(input())
im = Image.new('RGB', (a * 16, a * 13), color='white')
draw = ImageDraw.Draw(im)
draw.polygon([
    (a * 4, a * 12), (a, a * 9), (a * 4, a * 5), (a * 3, a * 4), (a * 2.5, a * 2),
    (a * 5, a * 3), (a * 6, a * 4), (a * 10, a * 4), (a * 11, a * 3), (a * 13.5, a * 2),
    (a * 13, a * 4), (a * 12, a * 5), (a * 15, a * 9), (a * 12, a * 12), (a * 4, a * 12)
             ], fill='#F5F033')
draw.polygon([(0, a), (a * 2.5, a * 2), (a * 3, a * 4), (0, a)], fill='black')
draw.polygon([(a * 16, a), (a * 13.5, a * 2), (a * 13, a * 4), (a * 16, a)], fill='black')
draw.polygon([(a * 7.5, a * 7.5), (a * 8.5, a * 7.5), (a * 8, a * 8), (a * 7.5, a * 7.5)], fill='black')
draw.rectangle((a * 7.5, a * 8.5, a * 8.5, a * 9.5), fill='#F00')
draw.line([(a * 6.5, a * 8), (a * 7.5, a * 8.5), (a * 8.5, a * 8.5), (a * 9.5, a * 8)], fill='black', width=a // 10)
draw.ellipse((a * 7.5, a * 9, a * 8.5, a * 10), fill='#F00')
draw.ellipse((a * 12, a * 8, a * 13, a * 9), fill='#F00')
draw.ellipse((a * 3, a * 8, a * 4, a * 9), fill='#F00')
draw.ellipse((a * 5, a * 6, a * 6.5, a * 7.5), fill='black')
draw.ellipse((a * 9.5, a * 6, a * 11, a * 7.5), fill='black')
draw.ellipse((a * 5.5, a * 6.5, a * 6, a * 7), fill='white')
draw.ellipse((a * 10, a * 6.5, a * 10.5, a * 7), fill='white')
im.save('pikachu.png')