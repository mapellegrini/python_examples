#!/usr/bin/python

from PIL import Image

def makesquare(pixels, width, x1, x2, y1, y2, color):
  for a in range (x1, x2):
    for b in range (y1, y2):
      pixels[b*width+a]=color
  return pixels 

def genchecker3(size, rows, cols):
  pwidth=size[0]
  pheight=size[1]
  pixels=[]

  #define color values
  red=(256,0,0)
  green=(0,256,0)
  blue=(0,0,256)
  purple=(256,0,256)
  yellow=(256,256,0)  
  white=(256,256,256)
  backcolor=white

  for a in range(0, pwidth*pheight):
    pixels.append(backcolor) 

  pixels=makesquare(pixels, pwidth, 100,150,100,150, red)
  pixels=makesquare(pixels, pwidth, 0  , 50,  0, 50, green)
  pixels=makesquare(pixels, pwidth, 400,500,400,500, blue)
  pixels=makesquare(pixels, pwidth, 350,400,350,400, purple)
  pixels=makesquare(pixels, pwidth, 200,400,0,25, yellow)
  return pixels

targetfile="checkboard.png" 
size=(500,500) 
pixels=genchecker3(size, 8, 8)
im = Image.new("RGB", size)
im.putdata(pixels) 
im.save(targetfile)
