#Exercise!
#Display the image below to the right hand side where the 0 is going to be ' ', and the 1 is going to be '*'. This will reveal an image!
picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

#1 iterate Over Picture
  # if 0 -> print ' '
  # if 1 -> print '*'
fill = '*'
empty = ' '
for image in picture:
    for pixel in image:
        if (pixel == 1):
            print(fill,end="")
        else:
            print(empty,end="")
    print('')