import time
from pprint import pprint

def buy_shares():
    n = input("name of share to  be bought: ").title().strip()
    v = int(input("enter no. of shares to be bought : "))
    p = int(input("enter price of shares to be bought : "))
    if p*v<=dic["balance"]:
        dic_shares.setdefault(n,0)
        a = dic_shares[n]
        dic_shares[n]  = a+v
        dic["balance"] = dic["balance"] - p*v
        print("Your remaining balance is :",dic["balance"])
        lonosb.append(n)
        locosb.append(p*v)
        lotosb.append(time.strftime("%H : %M"))

    else:
        print("Your balance {0} and price of shares is {1}".format(dic["balance"],float(p*v)))


def sell_shares():
    n = input("name of share to  be sold : ").title().strip()
    v = int(input("enter no. of shares to be sold : "))
    p = int(input("enter price of shares to be sold : "))
    if n in dic_shares:
        if v<=dic_shares[n]:
            dic_shares.setdefault(n, 0)
            a = dic_shares[n]
            dic_shares[n] = a - v
            dic["balance"] = dic["balance"] + p * v
            print("Your remaining balance is :", dic["balance"])
            lonoss.append(n)
            locoss.append(p * v)
            lotoss.append(time.strftime("%H : %M"))
            if  dic_shares[n] <= 0:
                dic_shares.pop(n)

        else:
            print("you don't have that much of shares")
    else:
        print("you don't have this share")


def increase():
    n = float(input("amount to  be increased : "))
    dic["balance"] = dic["balance"] + n
    print('balance : ',dic["balance"])


def analysis():
    eps = float(input("enter the current eps : "))
    g = float(input("enter the growth rate : "))
    r = float(input("enter your expected return : "))
    y = float(input("current government bond yield : "))
    v = 0
    v = (eps *(7 + g )* 4.4)/y
    print("intrinsic value of stock according to graham's formula is : ", v)
    vv = v*(100-r)  / 100
    print("You should buy stock at rs {} which is expected return of {} ".format(vv,r))


def print_details():
    pprint(dic)

def print_previous_trading_details():
    print("format of printing   %name of share %no. of shares %time at which share bought/sold")
    print("details of share bought")
    pprint(list(zip(lonosb,locosb,lotosb)))
    print("details of share sold")
    pprint(list(zip(lonoss, locoss,lotoss)))


dic = {}
k = True
print("enter details for ur account")
name = input("enter your name : ").title().strip()
balance = float(input("enter your balance : "))
lonosb = []
locosb = []
lonoss = []
locoss = []
lotosb = []
lotoss = []
dic_shares = {}
dic["name"]= name
dic["balance"] = balance
dic["shares"] = dic_shares
while k :
    print("what you want to do?")
    print("enter 1 to buy shares")
    print("enter 2 to sell shares")
    print("enter 3 to increase balance")
    print("enter 4 to do analysis of share")
    print("enter 5 to print details")
    print("enter 6 to get previous trading activities")
    print("enter 7 to exit trading activity")
    choice = int(input("enter your choice : "))
    if choice == 1:
        buy_shares()
    if choice == 2:
        sell_shares()
    if choice == 3:
        increase()
    if choice == 4:
        analysis()
    if choice == 5:
        print_details()
    if choice == 6:
        print_previous_trading_details()
    if choice == 7:
        k = False



