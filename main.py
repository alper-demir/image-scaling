from PIL import Image, ImageTk
import tkinter as tk
from tkinter import filedialog
import os
window = tk.Tk()
window.title("Image scaling")
window.geometry("550x370")


stringDifference = tk.StringVar()
stringDifference.set("")
labelDifferenceOfSize = tk.Label(window, textvariable=stringDifference, font="Arial 9")
labelDifferenceOfSize.place(x=320, y=130)

targetHeight = tk.StringVar()
targetHeight.set("")
labelHeight = tk.Label(window, textvariable=targetHeight, font="Arial 9", fg="black")
labelHeight.place(x=128, y=100)


stringInitialSize = tk.StringVar()
stringInitialSize.set("")
labelInitialSize = tk.Label(window, textvariable=stringInitialSize, font="Arial 9", fg="black")
labelInitialSize.place(x=10, y=130)


stringRenderedSize = tk.StringVar()
stringRenderedSize.set("")
labelRenderedSize = tk.Label(window, textvariable=stringRenderedSize, font="Arial 9", fg="black")
labelRenderedSize.place(x=150, y=130)


stringOriginalResolution = tk.StringVar()
stringOriginalResolution.set("")
labelStringOriginalResolution = tk.Label(window, textvariable=stringOriginalResolution, font="Arial 10", fg="black")
labelStringOriginalResolution.place(x=120, y=42)

def selectFile():

    global filePath
    filePath = tk.filedialog.askopenfilename()
    if(filePath !=''):
        if(os.path.getsize(filePath) < 500000): # smaller image than 5 mb
            stringDifference.set("")
            labelDifferenceOfSize.__setitem__('bg','#F0F0F0')
            targetHeight.set("")
            stringInitialSize.set("")
            stringRenderedSize.set("")

            image1 = Image.open(filePath)
            new = image1.resize((250,146))
            test = ImageTk.PhotoImage(new)

            label1 = tk.Label(image=test)
            label1.image = test

            label1.place(x=15, y =160)

            global initialSize
            initialSize = os.path.getsize(filePath)
            global image
            image = Image.open(filePath)

            stringInitialSize.set("Initinal Size:" + str(initialSize) + " Byte")

            path = tk.Label(text="Path:" + filePath, font="Arial 10", bg="#EBEBEB", fg="black")
            path.place(x=120, y=12)
            print(image.size , "px")

            stringOriginalResolution.set("Original Resolution:" + str(image.size) + "px")

        else:
            print("Please give smaller image than 5mb")
    else:
        print("Choose a file path")

def calculateHeight(width):
    # Based on 16:9 ratio
    ratio = 1.777777777777778
    return width / ratio

def calculateSizeDifference(initial,rendered):

    formula = ((rendered - initial) / initial) * 100

    if(formula < 0):
        stringDifference.set("File size reduced by " + str(abs(round(formula, 2))) + "%")
        labelDifferenceOfSize.__setitem__('bg','#40c970')
    else:
        stringDifference.set("File size increased by " + str(abs(round(formula, 2))) + "%")
        labelDifferenceOfSize.__setitem__('bg','#d94c6d')


def Take_input():
    global INPUT,WIDTH
    INPUT = int(Output.get("1.0", "end-1c"))
    WIDTH = int(Width.get("1.0", "end-1c"))
    if(INPUT !='' and len(filePath) > 0):

        HEIGHT = int(calculateHeight(WIDTH))

        targetHeight.set("Target Height(16:9):" + str(HEIGHT) + "px")

        new_image = image.resize((WIDTH, HEIGHT))
        new_image.save('renderedImage.jpg', optimize=True, quality=INPUT)
        renderedSize = os.path.getsize("renderedImage.jpg")

        stringRenderedSize.set("Rendered Size:" + str(renderedSize) + " Byte")

        calculateSizeDifference(initialSize, renderedSize)

        image1 = Image.open('renderedImage.jpg')
        new = image1.resize((250, 146))
        test = ImageTk.PhotoImage(new)

        label1 = tk.Label(image=test)
        label1.image = test

        label1.place(x=285, y=160)

    else:
        print("Please fill all inputs")


b1 = tk.Button(text="Select File", font="Arial 12 bold", bg="#DCDCDC", fg="white", command=selectFile)
b1.place(x=10, y=10)

l = tk.Label(text="Quality(%):")
l.place(x=10, y=70)

inputWidth = tk.Label(text="Width(px):")
inputWidth.place(x=10, y=100)

Output = tk.Text(window, height=1, width=5, bg="#F6F8FA")
Output.place(x=75, y=70)

Width = tk.Text(window, height=1, width=5, bg="#F6F8FA")
Width.place(x=75, y=100)

Display = tk.Button(window, height=2, width=10, text ="Show", command=lambda: Take_input())

Display.place(x=470, y=320, width=70)

window.mainloop()