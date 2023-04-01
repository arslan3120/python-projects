from turtle import *
import colorsys

bgcolor('black')
tracer(10)
pensize(5)
h=0
for i in range(300):
    c = colorsys.hsv_to_rgb(h,0,0.5)