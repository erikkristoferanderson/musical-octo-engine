import tkinter
from util import octo_sounds


def main():
    def start():
        octo_sounds.go(var1, var2, var3, var4, var5, var6, var7, var8)
    print("Welcome to musical octo engine")
    master = tkinter.Tk()
    var1 = tkinter.IntVar()
    tkinter.Checkbutton(master, text="1", variable=var1).grid(row=0, column=0, sticky=tkinter.W)
    var2 = tkinter.IntVar()
    tkinter.Checkbutton(master, text="2", variable=var2).grid(row=0, column=1, sticky=tkinter.W)
    var3 = tkinter.IntVar()
    tkinter.Checkbutton(master, text="3", variable=var3).grid(row=0, column=2, sticky=tkinter.W)
    var4 = tkinter.IntVar()
    tkinter.Checkbutton(master, text="4", variable=var4).grid(row=1, column=0, sticky=tkinter.W)
    var5 = tkinter.IntVar()
    tkinter.Checkbutton(master, text="5", variable=var5).grid(row=1, column=2, sticky=tkinter.W)
    var6 = tkinter.IntVar()
    tkinter.Checkbutton(master, text="6", variable=var6).grid(row=2, column=0, sticky=tkinter.W)
    var7 = tkinter.IntVar()
    tkinter.Checkbutton(master, text="7", variable=var7).grid(row=2, column=1, sticky=tkinter.W)
    var8 = tkinter.IntVar()
    tkinter.Checkbutton(master, text="8", variable=var8).grid(row=2, column=2, sticky=tkinter.W)
    start_button = tkinter.Button(text="go", command=start).grid(row=1, column=1)
    tkinter.mainloop()

if __name__ == "__main__":
    main()