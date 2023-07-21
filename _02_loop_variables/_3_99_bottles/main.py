import time
x=99
print("99 bottles of beer on the wall, 99 bottles of beer.")
for i in range(98):
    time.sleep(.2)
    x-=1
    x=str(x)
    print("Take one down and pass it around,"+x+" bottles of beer on the wall."+x+" bottles of beer on the wall, "+x+" bottles of beer.")
    x=int(x)
print("Take one down and pass it around, no more bottles of beer on the wall.No more bottles of beer on the wall, no more bottles of beer.Go to the store and buy some more, 99 bottles of beer on the wall.")