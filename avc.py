
basket=[]
def helper(filename,basket):
    m=open(filename)
    l=m.readlines()
    for i in l:
        print(i)
    a=0
    while a!=-1:
        a=int(input("Select the item you want to buy, using the corressponding serial no.(-1 for main menu).)"))   
        if a==-1:
            return
        else:
            a=l[a].strip().split()
            q=input("Quantity? ")
            a.append(q)
            basket.append(a[1:])
            total(basket)
def bill(basket):
    total=0
    print("Item   price   quantity")
    for i in basket:
        print(i[0],"   ",i[-2],"   ",i[-1])
        a=int(i[-1])*int(i[-2])
        total=total+a
    print("Your total bill is",total)
    print("Check out?")
    print("0. Yes")
    print("1. No")
    c=int(input())
    if c==0:
        print("5% of your bill is awarded as loyalty points which you can avail to get different things.")
        print("Loyalty points= ",total*0.05)
        return False
def total(basket):
    total=0
    for i in basket:
        a=int(i[-1])*int(i[-2])
        total=total+a
    print("Your total bill is: ",total)

def remove(basket):
    print("Sr#   items    Quantity")
    for i in range(len(basket)):
        print(i,"  ",basket[i][0],"     ",basket[i][-1])
    a=int(input("Enter serial no. of item you want to remove.(-1 to return to main menu" ))
    if a==-1:
        return
    else:
        b=int(input("Quantity? "))
        basket[a][-1]=int(basket[a][-1])-b
        if basket[a][-1]==0:
            basket.remove(basket[a])
def market(basket):
    name=input("Enter name. ")
    print("welcome "+name," to Matts's super market")
    a=True
    while a==True:
        print("MAIN MENU")
        m=open("menu.txt")
        l=m.readlines()
        for i in l:
            print(i)
        select=int(input("Choose the number of the option you want to access. "))
        if select==0:
            helper("vegetables.txt",basket)
        elif select==1:
            helper("fruits.txt",basket)
        elif select==2:
            helper("fishfood.txt",basket)
        elif select==3:
            helper("bakery.txt",basket)
        elif select==4:
            helper("cosmetics.txt",basket)
        elif select==5:
            remove(basket)
        elif select==6:
            a=bill(basket)
    
market(basket)
