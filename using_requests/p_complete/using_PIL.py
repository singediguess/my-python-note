import requests
from io import BytesIO
from PIL import Image
from sys import argv

png_url = 'http://www.wallpapersin4k.org/wp-content/uploads/2017/04/Wallpaper-Png-5.png'
jpeg_url = 'http://wallpaper.1000webgames.com/wallpapers/german_shepherd_pc_wallpaper_jpeg-800x600.jpg'

if argv[1] == 'jpeg':
    r = requests.get(jpeg_url)
    print ('Status code:', r.status_code)
elif argv[1] == 'png':
    r = requests.get(png_url)
    print ('Status code:', r.status_code)
else :
    print ('Please add one instruction')

img=Image.open(BytesIO(r.content))
print(img.size, img.format, img.mode)

path = './PILtest.' + img.format

try:
    img.save(path, img.format)
except IOError:
    print ('Cannot save this image')
