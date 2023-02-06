def Profit(costPrice, sellingPrice):

    profit = (sellingPrice - costPrice)

    return profit

def Loss(costPrice, sellingPrice):

    Loss = (costPrice - sellingPrice)

    return Loss

if __name__ == "__main__":

    costPrice = int(input("Please enter the price:\n"))
    sellingPrice = int(input("please enter the selling price:\n"))

if sellingPrice == costPrice:
    print("you have no profit")
elif sellingPrice > costPrice:
    print("you have ",Profit(costPrice,sellingPrice)," made")
elif sellingPrice < costPrice:
    print("you have ",Loss(costPrice,sellingPrice)," lost")