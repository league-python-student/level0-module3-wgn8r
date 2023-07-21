from tkinter import simpledialog, messagebox, Tk

# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story
x=input("once upon a time there was a coding student learning python. This student was on the first day of their class and was wondering if they should skip class. Now this is a complicated issue involving politics and global warming. If the student was to stay there is an extremely small chance that they may phase through the ground and collide with the earth core going mach 10, sustaining 150 g's, and the planet imploded, which do you choose")
if x=="stay":
    y=input("during the tedious school, the bright individual prospered through the courses, until they are given the opportunity to code independently from their group. they have the bright idea of hacking into NORAD and launching off ICBM's to assasinate the north macedonian head of state. The only downside of this is there is a large chance of commencing MAD and starting WW3")
    if y=="not hack":
        z=input("after the class finished, the student decided to go out to get ice cream what flavor should they choose: vanilla, or chocolate?")
        print("everyone dies")
        quit()
    if y == " hack":
        print("everyone dies")
        quit()

if x=="go":
    print("everyone dies")
    quit()