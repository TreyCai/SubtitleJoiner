#!/usr/bin/python

# filter image files
# downscale images to the output size
# set pixel spot
# read pixel and find top black border and bottom black border height
# full-image vs subtitle-only merge
# output the final image file

import os, sys
from PIL import Image

images = []

def process_files(files):
    output_image = None

    for index, f in enumerate(files):
        print f
        if not f.endswith(('.jpg', '.jpeg', '.png')):
            continue

        try:
            image = Image.open(f)
            images.append(image)
            rgb_image = image.convert('RGB')
            width, height = image.size
            top_border = find_top_border(rgb_image)
            bottom_border = find_bottom_border(rgb_image)
            crop = image.crop((0, top_border, width, bottom_border))
            crop.save(f.replace('.jpg', '2.jpg'))

            if output_image is None:
                output_image = Image.new("RGB", (width, (bottom_border - top_border) * len(files)))
            output_image.paste(crop, (0, index * (bottom_border - top_border), width, (index + 1) * (bottom_border - top_border)))
        except IOError:
            print "IOError: cannot open image file"

    if output_image is not None:
        print os.path.dirname(files[0])
        print os.path.dirname(files[0]) + '/la.jpg'
        output_image.save(os.path.dirname(files[0]) + '/la.jpg')

def scale_image(output_width, image):
    width, height = image.size
    output_height = int(round(height * (output_width * 1.0 / width)))
    image.resize(output_width, output_height)

def crop_image_border(rgb_image):
    width, height = image.size
    crop = image.crop((0, find_top_border(rgb_image), width, find_bottom_border(rgb_image)))
    crop.save(f.replace('.jpg', '2.jpg'))

def find_top_border(rgb_image):
    hook = []
    width, height = rgb_image.size
    width_step = width / 10
    height_step = 16
    for i in range(0, width, width_step):
        hook.append(i)
    print hook

    border_height = height_step
    while(True):
        for h in hook:
            r, g, b = rgb_image.getpixel((h, border_height))
            print height_step, h, border_height, (r, g, b)
            if r == g == b == 0:
                continue
            else:
                border_height -= height_step
                if height_step == 1:
                    return border_height
                else:
                    height_step = height_step >> 1
                    break
        border_height += height_step

def find_bottom_border(rgb_image):
    hook = []
    width, height = rgb_image.size
    width_step = width / 10
    height_step = 16
    for i in range(0, width, width_step):
        hook.append(i)
    print hook

    border_height = height - 1
    while(True):
        for h in hook:
            r, g, b = rgb_image.getpixel((h, border_height))
            print height_step, h, border_height, (r, g, b)
            if r == g == b == 0:
                continue
            else:
                border_height += height_step
                if height_step == 1:
                    return border_height
                else:
                    height_step = height_step >> 1
                    break
        border_height -= height_step


list_of_files = sys.argv[1:]
print list_of_files

process_files(list_of_files)

print images
