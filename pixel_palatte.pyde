
def setup():
    global pixelSize
    pixelSize = 5
     
    global palatte 
    palatte  = []
    
    #Grey palatte:
    palatte.append(int(color(149, 166, 176)))
    palatte.append(int(color(123, 114, 131)))
    palatte.append(int(color(105, 118, 134)))
    palatte.append(int(color(238, 242, 243)))
    palatte.append(int(color(194, 199, 202)))
    
    #Uncomment for color palatte suited for animegirl1.png
    # palatte.append(int(color(29, 11, 1)))
    # palatte.append(int(color(251, 229, 192)))
    # palatte.append(int(color(242, 191, 124)))
    # palatte.append(int(color(155, 25, 0)))
    # palatte.append(int(color(0, 35, 20)))

    size(736, 459)
    global img
    img = loadImage("animegirl1.png")
    img.filter(GRAY)
    noStroke()
    
        
def draw():
    for x in range(0, img.width, pixelSize):
        for y in range(0, img.height, pixelSize):
            #get the color at x, y.
            col = color(img.get(x, y))

            #Whatever colour is at x and y, find the palatte  approximation in the array.
            fl = min(palatte , key=lambda x:abs(x - int(col)))
            #Make the rectangle the colour of the closest approximation.
            fill(color(fl))
            rect(x, y, pixelSize, pixelSize) 
    