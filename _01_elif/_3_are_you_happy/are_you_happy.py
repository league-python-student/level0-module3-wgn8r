from tkinter import Tk, simpledialog, messagebox


if __name__ == '__main__':
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements
    x=input("are you happy?")
    if x=="yes":
        print("keep doing whatever you're doing")
    else:
        y=input("do you want to be happy?")
        if y=="yes":
            print("change something")
        else:
            print("keep doing whatever you're doing")

    pass
