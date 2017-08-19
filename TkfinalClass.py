from Tkinter import *
import webbrowser
import tkMessageBox
from groceryClass import *
import io
import time


class TkClass:

    def __init__(self, parent, title, color, geometry, photo):
        '''
        This initializes our first windows variables as well as the class variables we will need
        :param parent: the tk() instance that we pass it
        :param title: the title of the instance
        :param color: the color of the background of the window
        :param geometry: the size of the window
        :param photo: the logo image
        :return: Nothing: initializes variables
        '''
        self.parent = parent
        self.title = parent.title(title)
        self.conf = parent.config(bg = color)
        self.size = parent.geometry(geometry)
        self.deny = parent.resizable(False, False)
        self.v = IntVar(None)
        self.custMoney = StringVar(None)
        self.pic = photo
        self.classlist = []
        self.grains = {}
        self.veggies = {}
        self.dairy = {}
        self.protein = {}
        self.prices = {}


    def openwally(self, win):
        '''
        :param win: the window to kill
        :return: opens walmart.com
        '''
        win.destroy()
        webbrowser.open("http://walmart.com")

    def write_grocerylist(self, win):
        '''
        The function writes the grocery list to a file
        :param win: the window to destroy
        :return: Nothing
        '''
        with io.FileIO("GroceryList.txt", "w") as file:
            file.write("GRAIN: \n ")
            for each in self.grains:
                file.write("-" + each + ":" + str(self.grains[each])+ "\n")
            file.write("\n")
            file.write("DAIRY: \n ")
            for each in self.dairy:
                file.write("-" + each + ":" + str(self.dairy[each]) + "\n")
            file.write("\n")
            file.write("VEGETABLES & FRUIT: \n ")
            for each in self.veggies:
                file.write("-" + each + ":" + str(self.veggies[each]) + "\n")
            file.write("\n")
            file.write("PROTEIN: \n ")
            for each in self.protein:
                file.write("-" + each + ":" + str(self.protein[each]) + "\n")
            file.close()
            win.destroy()



    def setupmainwin(self):
        '''
        This function sets up our main window
        :return: nothing but it calls the second window (customize_window) when the user
        has entered valid variables
        '''
        frame = Frame(self.parent)
        frame.config(height = 100, width = 500)

        photo = PhotoImage(file = self.pic)
        labelpho= Label(self.parent, image= photo)
        labelpho.pack(side = 'top')

        BrokeHungry = LabelFrame(frame, height = 20, width = 500, bg = "yellow green")
        frame.pack()
        BrokeHungry.pack()

        yourMoney = Entry(self.parent, textvariable= self.custMoney)
        self.custMoney.set("Enter $ Amount")
        self.custMoney.get()
        yourMoney.pack(side='top', pady = 10)

        def callback():
            '''
            :return: When the button has been pressed, check to see if values are valid, call customize if so, if not
            throw an error message and let the user re-enter values
            '''
            money = self.custMoney.get()
            pref = (self.v.get())
            try:
                money = int(money)
                if int(money) > 1000:
                    tkMessageBox.showinfo("Error!", "Please enter a reasonable amount of money! (below 1000)")
                elif int(money) < 10:
                    tkMessageBox.showinfo("Error!", "Please enter a reasonable amount of money (above 10)!")
                else:
                    mylist = GroceryList(int(pref), int(money))
                    mylist.setlistdicts()
                    self.classlist = mylist.listandspent()
                    self.grains = self.classlist[0]
                    self.veggies = self.classlist[1]
                    self.dairy = self.classlist[2]
                    self.protein = self.classlist[3]
                    self.prices = self.classlist[4]
                    self.parent.destroy()
                    self.customize_window()

            except ValueError:
                tkMessageBox.showinfo("Error!", "Please enter the amount and select your dietary needs!")
                return

        Radiobutton(self.parent, text="Vegan", variable=self.v, value=1, bg = "white").pack(anchor=W)
        Radiobutton(self.parent, text="Vegetarian", variable=self.v, value=2,  bg = "white").pack(anchor=W)
        Radiobutton(self.parent, text="Omnivore", variable=self.v, value=3,  bg = "white").pack(anchor=W)

        button = Button(self.parent,text = "Click Me", command=callback)
        button['text'] = "Submit"
        button.pack(side='top')

        def callback2():
            ''' Clears the values in our main window
            :return: Nothing
            '''
            self.custMoney.set("Enter $ Amount")
            self.v.set(None)

        button2 = Button(self.parent, command=callback2)
        button2['text'] = "Clear"
        button2.pack(side='top')

        self.parent.mainloop()


    def customize_window(self):
        '''
        This funciton creates our second window that lists the groceries. It has two buttons (either purchase or prepare
        to print). Purchase takes you to walmart.com and Prepare to Purchase creates a file with the list of groceries
        :return: Nothing
        '''

        window = Tk()
        window.title("BrokeNhungry")
        window.geometry('350x1000+400+0')
        window.resizable(False, False)
        photo = PhotoImage(file = "food.gif")
        label= Label(window, image= photo, height = 150)
        label.pack(side = 'top')

        header = Label(window, text = "Grocery List", font = "Times")
        header.pack(side = 'top')


        frame1 = Frame(window)
        frame1.config(height = 400, width = 350)

        grain = LabelFrame(frame1, height = 100, width = 350, text = "Grains", font = "Times", bg = "LightSteelBlue1")
        dairy = LabelFrame(frame1, height = 100, width = 350, text = "Dairy", font = "Times", bg = "LightSteelBlue2")
        fruits = LabelFrame(frame1, height = 100, width = 350, text = "Fruits & Vegetables", font = "Times", bg = "LightSteelBlue3")
        protein = LabelFrame(frame1, height = 100, width = 350, text = "Protein", font = "Times", bg = "LightSteelBlue4")
        total = LabelFrame(frame1, height = 100, width = 350, text = "Total", font = "Times", bg = "gray83")

        frame1.pack()
        grain.pack()
        dairy.pack()
        fruits.pack()
        protein.pack()
        total.pack()

        for item in self.grains:
                food = Label(grain, text = item +" : qty= "+ str(self.grains[item])+"\n", width = 350, bg = "LightSteelBlue1")
                food.pack()

        for item in self.dairy:
                food = Label(dairy, text = item +" : qty="+ str(self.dairy[item])+"\n", width = 350, bg = "LightSteelBlue2")
                food.pack()

        for item in self.veggies:
                food = Label(fruits, text = item +" : qty="+ str(self.veggies[item])+"\n", width = 350, bg = "LightSteelBlue3")
                food.pack()

        for item in self.protein:
                food = Label(protein, text = item +" : qty="+ str(self.protein[item])+"\n", width = 350, bg = "LightSteelBlue4")
                food.pack()

        sum = Label(total, text = "$" + str(self.prices) + "\n", width = 350, bg = "gray83")
        sum.pack()


        def callback():
            '''
            This function calls the open walmart function
            :return: Nothing
            '''
            self.openwally(window)

        b = Button(window, text="Purchase", command=callback)
        b.pack()

        def callback2():
            '''
            This function calls the write to file funciton
            :return: Nothing
            '''
            self.write_grocerylist(window)

        b1 = Button(window, text="Prepare to Print", command=callback2)
        b1.pack()

        window.mainloop()



def main():
    root = Tk()
    window1 = TkClass(root, "BrokeNhungry", "white", '300x380+400+100', "logo.gif")
    window1.setupmainwin()


main()