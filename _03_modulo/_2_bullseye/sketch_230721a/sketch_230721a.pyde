def setup():
    # Set the size of your sketch
    size(1000,1000)
    
    pass
    
def draw():
    # Starting with the largest ellipse, use a for loop to draw a bullseye with ellipses
    sze=500
    x=1
    x=int(x)
    for i in range(8):
        if x%2!=0:
            fill(255,0,0)
        else:
            fill(0,0,0)
        x+=1
        ellipse(500,500,sze,sze)
        sze-=50

      # Use an if statement and modulo to alternate the color of your rings
    
    
    
    
    
    pass
