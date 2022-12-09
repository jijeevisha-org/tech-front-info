import urllib.request as req
from PIL import Image

def optimize(imgPath = "featured.jpg", picNameDefault = "featured.jpg", reduceBy = 45):
  # if url is given
  if 'http://' in imgPath or 'https://' in imgPath:
    #imgURL = input("URL of banner image: ")
    _ = req.urlretrieve(imgPath, picNameDefault)
    imgPath = picNameDefault
  # optimize
  currImg = Image.open(imgPath)
  # downsize the image with an ANTIALIAS filter (gives the highest quality)
  currImg = currImg.resize(currImg.size,Image.ANTIALIAS)
  currImg.save(picNameDefault, optimize=True, quality=reduceBy)
  return
