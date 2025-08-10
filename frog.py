from PIL import Image, ImageDraw
a = int(input())
im = Image.new('RGB', (a * 16, a * 12), color='white')
draw = ImageDraw.Draw(im)
draw.polygon([
    (a * 7, a * 4), (a * 2, a * 5), (a * 8, a * 8), (a * 14, a * 5), (a * 9, a * 4), (a * 8, a * 3.5),
    (a * 7, a * 4), (a * 9, a * 4), (a * 8, a * 8), (a * 7, a * 4)
             ], fill='#92D050')
draw.polygon([
    (a * 2, a * 5), (a, a * 6), (a * 4, a * 7.5), (a * 8, a * 8), (a * 7, a * 4), (a * 9, a * 4),
    (a * 8, a * 8), (a * 14, a * 5), (a * 15, a * 6), (a * 12, a * 7.5), (a * 8, a * 8), (a * 2, a * 5),
             ], fill='#44D047')
draw.polygon([
    (a * 4, a * 7.5), (a * 8, a * 8), (a * 12, a * 7.5), (a * 8, a * 10), (a * 4, a * 7.5),
             ], fill='#7F7F7F')
draw.polygon([
    (a * 4, a * 7.5), (a, a * 6), (a * 4, a * 11), (a * 12, a * 11), (a * 15, a * 6), (a * 12, a * 7.5),
    (a * 12, a * 11), (a * 8, a * 10), (a * 4, a * 11), (a * 4, a * 7.5),
             ], fill='#4B9F2D')
draw.polygon([
    (a, a * 6), (a * 2, a * 10), (a * 4, a * 11), (a * 4, a * 7.5), (a * 8, a * 10), (a * 12, a * 7.5), (a * 12, a * 11),
    (a * 15, a * 6), (a * 14, a * 10), (a * 12, a * 11), (a * 8, a * 10), (a * 4, a * 11), (a, a * 6),
             ], fill='#377521')
draw.ellipse((a * 2, a * 1, a * 6, a * 5), fill='#377521')
draw.ellipse((a * 2.5, a * 1.5, a * 5.5, a * 4.5), fill='#F3EE0D')
draw.ellipse((a * 3, a * 2, a * 5, a * 4), fill='black')
draw.ellipse((a * 3.75, a * 2, a * 4.25, a * 2.5), fill='white')
draw.ellipse((a * 10, a * 1, a * 14, a * 5), fill='#377521')
draw.ellipse((a * 10.5, a * 1.5, a * 13.5, a * 4.5), fill='#F3EE0D')
draw.ellipse((a * 11, a * 2, a * 13, a * 4), fill='black')
draw.ellipse((a * 11.75, a * 2, a * 12.25, a * 2.5), fill='white')
im.save('frog.png')