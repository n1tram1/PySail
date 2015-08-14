#!/usr/bin/python
from PIL import Image

original = Image.open("HB16.png")

for i in range(0, 360, 5):
	tmp_img = original.rotate(-i)
	tmp_img.save("HB16_{0}.png".format(i))
