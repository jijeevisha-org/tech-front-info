import urllib.request as req
from PIL import Image

def optimize(imgPath = "featured.jpg", picNameDefault = "featured.jpg", reduceBy = 45, sizeOriginal=False):
  #####################
  # if url is given
  if 'http://' in imgPath or 'https://' in imgPath:
    #imgURL = input("URL of banner image: ")
    _ = req.urlretrieve(imgPath, picNameDefault)
    imgPath = picNameDefault
  #####################
  ## check for 'jpg' and convert if needed
  im = Image.open(imgPath)
  if imgPath[-4:] == ".png":
    jpg_im = im.convert('RGB')
    jpg_im.save(imgPath)
  # optimize
  currImg = Image.open(imgPath) # it can be same as jpg_im
  #####################
  # downsize the image with an ANTIALIAS filter (gives the highest quality)
  newSize = currImg.size if sizeOriginal else (1280,800)
  currImg = currImg.resize(newSize,Image.ANTIALIAS)
  currImg.save(picNameDefault, optimize=True, quality=reduceBy)
  return
