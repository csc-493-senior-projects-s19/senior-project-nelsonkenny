import random

class GroceryList:
    def __init__(self, pref, cash):
        '''
        :param pref: 1, 2, 3 depending on which checkbox the user entered in the Tk module
        :param cash: The total amount of money the user has to spend on groceries
        :return: Nothing. Initiates all of the class variables.
        '''
        self.grainpercent = (int(cash) * .4)
        self.veggiepercent = (int(cash) * .3)
        self.dairypercent = (int(cash) * .2)
        self.proteinpercent = (int(cash) * .1)
        self.pref = pref
        self.money = cash
        self.grains = []
        self.grainsdict ={}
        self.dairylist = []
        self.dairydict ={}
        self.proteinlist =[]
        self.proteindict ={}
        self.veggielist = ["broccoli", "carrots", "bananas"]
        self.veggiedict = {"broccoli": 2.24, "carrots": .48 , "bananas": 0.52}

    def setlistdicts(self):
        '''
        :return: Nothing. Updates the class variables depending on self.pref
        '''
        if int(self.pref) == 1:
            self.grains = ["corn", "millet", "quinoa"]
            self.grainsdict = {"corn": 2.78, "millet": 4.22, "quinoa": 3.58}
            self.dairy = ["soymilk", "soycheese"]
            self.dairydict = {"soymilk": 2.24, "soycheese": 2.68}
            self.proteinlist = ["tofu", "black beans"]
            self.proteindict = {"tofu": 1.34, "black beans": 2.50}
        elif int(self.pref) == 2:
            self.grains = ["oatmeal", "brown rice", "wholewheatbread"]
            self.grainsdict = {"oatmeal": 2.35, "brown rice": 2.00, "wholewheatbread": 4.00}
            self.dairy = ["milk", "cheese"]
            self.dairydict = {"milk": 3.76, "cheese": 3.33}
            self.proteinlist = ["tofu", "black beans"]
            self.proteindict = {"tofu": 1.34, "black beans": 2.50}
        else:
            self.grains = ["oatmeal", "brown rice", "wholewheatbread"]
            self.grainsdict = {"oatmeal": 2.35, "brown rice": 2.00, "wholewheatbread": 4.00}
            self.dairy = ["milk", "cheese"]
            self.dairydict = {"milk": 3.76, "cheese": 3.33}
            self.proteinlist = ["chicken", "hotdogs"]
            self.proteindict = {"chicken": 2.48, "hotdogs": 2.00}


    def listandspent(self):
        '''
        This funciton calls creategrocerylist to create a dictionary and get the price spent on each section
        :return: a list containing 4 dictionaries, and the total sum of money spent
        '''
        ######################
        Grainlist = self.creategrocerylist(self.grains, self.grainsdict, self.grainpercent)
        GD = self.count_data(Grainlist[0])

        FVlist = self.creategrocerylist(self.veggielist, self.veggiedict, self.veggiepercent)
        VD= self.count_data(FVlist[0])

        Dairylist = self.creategrocerylist(self.dairy, self.dairydict, self.dairypercent)
        DD = self.count_data(Dairylist[0])

        Proteinlist = self.creategrocerylist(self.proteinlist, self.proteindict, self.proteinpercent)
        PD = self.count_data(Proteinlist[0])

        return [GD, VD, DD, PD, (Grainlist[1] + FVlist[1] +Dairylist[1] + Proteinlist[1])]

    def creategrocerylist(self, foodlist, dict, spendingmoney):
        '''
        :param foodlist: the selection of foods in that category
        :param dict: the dictionary associated with the foods & prices of that category
        :param spendingmoney: the total amount of money the user has to spend on category
        :return: returns a randomized grocerylist and the amount of money spent
        '''
        grocerylist = []
        currentprice = 0
        while (currentprice <= spendingmoney):
            pick = random.choice(foodlist)
            grocerylist.append(pick)
            currentprice += dict[pick]
        del grocerylist[-1]
        currentprice -= dict[pick]
        return [grocerylist, currentprice]

    def count_data(self, grocery):
        '''
        This function is so that you can remove duplicates
        :param grocery: takes in the total grocery list and removes duplicates
        :return: a dictionary with each item you can purchase and the amount that you can purchase
        '''
        finalgroceries ={}
        for each in ["corn", "millet", "quinoa","soymilk", "soycheese","tofu", "black beans","oatmeal", "brown rice", "wholewheatbread", "broccoli", "carrots", "bananas", "milk", "cheese","chicken", "hotdogs"]:
            if grocery.count(each) == 0:
                pass
            else:
                finalgroceries[each] = (grocery.count(each))
        return finalgroceries



def main():
    mylist = GroceryList(1, 100)
    mylist.setlistdicts()
    what = mylist.listandspent()
    print what

#main()









