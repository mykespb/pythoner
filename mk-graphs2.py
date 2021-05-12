#! /usr/bin/env python3

#  mk-graphs2.py
#  tests with graphs: create a sample graphic picture with PIL
#  (C) Mikhail Kolodin, 2021
#  ver. 2021-05-12 1.1

# docs: https://pillow.readthedocs.io/en/stable/handbook/index.html

from PIL import Image, ImageDraw

# common settings
size = 500
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# picture 1
im = Image.new('RGB', (size, size), WHITE)
draw = ImageDraw.Draw(im)

for i in range(0, size, 10):
  draw.line(xy = ((0, 0), (size, i)), fill = 'black', width=1)
  draw.line(xy = ((0, 0), (size-i, size)), fill = 'black', width=1)

#im.show()
im.save('pil-01.jpg', quality=95)

# picture 2
im = Image.new('RGB', (size, size), WHITE)
draw = ImageDraw.Draw(im)

for i in range(0, size, 10):
    draw.line(xy=((0, i), (i, size), (size, size - i), (size - i, 0), (0, i)),
              fill='black',
              width=1)

#im.show()
im.save('pil-02.jpg', quality=95)

# picture 3
im = Image.new('RGB', (size, size), WHITE)
draw = ImageDraw.Draw(im)

for i in range(0, size, 10):
    draw.line(xy = ( (0, 0), (i, size) ), fill = 'black', width = 1)
    draw.line(xy = ( (0, 0), (size, size-i) ), fill = 'black', width = 1)
    draw.line(xy = ( (size, size), (i, 0) ), fill = 'black', width = 1)
    draw.line(xy = ( (size, size), (0, i) ), fill = 'black', width = 1)

#im.show()
im.save('pil-03.jpg', quality=95)

# picture 4
im = Image.new('RGB', (size, size), WHITE)
draw = ImageDraw.Draw(im)

for i in range(0, size+1, 10):
  draw.line(xy= ((i, 0), (size-i, size)), fill = 'black', width = 1)
  draw.line(xy= ((0, i), (size, size-i)), fill = 'black', width = 1)

#im.show()
im.save('pil-04.jpg', quality=95)
