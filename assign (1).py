    # Function to get user input
def getDetails():
    userDetails = {}

    print("Welcome to Arnold's Amazing Eats")
    userDetails["firstName"] = input("Please Enter your first name: ")
    userDetails["lastName"] = input("Please enter your last name: ")
    userDetails["phoneNumber"] = input("Enter your phone number: ")

    validInput = False

    while(not validInput):
        delivery = input(
            "Would you like delivery? The charge is $5 but free for orders above $30 before GST (Y/N) ")

        if delivery == "Y" or delivery == "y":
            validInput = True
            userDetails["delivery"] = True
            userDetails["streetNumber"] = input(
                "Please Enter your street number: ")
            userDetails["streetName"] = input(
                "Please Enter your street name: ")
            userDetails["unitNumber"] = input("Please Enter your unit no: ")
            userDetails["city"] = input("Please Enter your city: ")
            userDetails["postalCode"] = input("Enter your PostalCode here: ")
            userDetails["provinceCode"] = input(
                "Please Enter your Province Code: ")
            userDetails["specialInstructions"] = input(
                "Any special instructions for delivery: ")
        elif delivery == "N" or delivery == "n":
            validInput = True
            userDetails["delivery"] = False
        else:
            print("Please enter Y or N to proceed")

    print(userDetails)
    return userDetails

# Function to select menu item


def getOrder():
    foodItems = {
        "1": {"item": "MAKKI KI ROTI", "price": "$11", "val": 11},
        "2": {"item": "RICE", "price": "$14", "val": 14},
        "3": {"item": "FRIES", "price": "$12", "val": 12},
        "4": {"item": "SALAD", "price": "$15", "val": 15},
        "5": {"item": "JUICE", "price": "$10", "val": 10},
        "6": {"item": "ICE CREAM", "price": "$18", "val": 18}
    }

    print("\n\nHere is a Arnold's Amazing Eats Menu Items:")

    for food in foodItems:
        print(food + ") " + foodItems[food]
              ["item"] + " => " + foodItems[food]["price"])

    orderNumbers = list(
        map(str, input("Enter food items to purchase: ").split()))
    orders = []

    for orderNum in orderNumbers:
        orders.append(foodItems[orderNum])

    # print(orders)
    return orders


# Function to confirm order
def confirmOrder():
    orders = getOrder()
    print("\n\nThank you for selecting: ")
    for order in orders:
        print("  " + order["item"] + " => " + order["price"])

    validInput = False

    while(not validInput):
        Approv_item = input("\nConfirm order? (Y/N) ")

        if Approv_item == "Y" or Approv_item == "y":
            validInput = True
            print("Congratulations your Order Has been Confirmed")
        elif Approv_item == "N" or Approv_item == "n":
            validInput = True
            print("Sorry for INCONVENIENCE! Please enter your order again")
            orders = confirmOrder()
        else:
            print("Please enter Y or N to proceed")

    # print(orders)
    return orders

# Function to apply student discount


def studentDiscount():
    validInput = False

    while(not validInput):
        isStudent = input("\n\nAre you a student? (Y/N) ")

        if isStudent == "Y" or isStudent == "y":
            validInput = True
            student_Id = input("Please Provide your Student Id here: ")
            print("Amazing students will get 10% additional discount")
            print("13% GST COUNTED WITH TOTAL")

            return True
        elif isStudent == "N" or isStudent == "n":
            validInput = True
            print("13% GST COUNTED WITH TOTAL")

            return False
        else:
            print("Please enter Y or N to proceed")


def tip(total):
    validInput = False

    while(not validInput):
        tipPercent = input("\n\nTip delivery person (10, 15 or 20%): ")

        if tipPercent == "10" or tipPercent == "10%":
            validInput = True
            tipAmount = total * 0.1
        elif tipPercent == "15" or tipPercent == "15%":
            validInput = True
            tipAmount = total * 0.15
        elif tipPercent == "20" or tipPercent == "20%":
            validInput = True
            tipAmount = total * 0.2
        else:
            print("Please enter 10, 15 or 20 to proceed")
    return tipAmount

# Function to finalize order
def receipt(userDetails, orders, total):
    print("\n\n RECEIPT")
    print("NAME => " + userDetails["firstName"] +
          " " + userDetails["lastName"])
    print("PHONE NUMBER => " + userDetails["phoneNumber"])
    print("ORDERED ITEMS: ")
    for order in orders:
        print("  " + order["item"] + " => " + order["price"])
    print("TOTAL => $" + str(total))

# Function to calculate total
def getTotal():
    total = 0
    userDetails = getDetails()
    orders = confirmOrder()
    studDiscount = studentDiscount()
    studDiscountPercent = 10
    gstPercent = 13
    deliveryCharge = 5

    for order in orders:
        total = total + order["val"]

    if studDiscount:
        total = total - (total * (studDiscountPercent / 100))

    gst = (total * (gstPercent / 100))

    if userDetails["delivery"] == True:
        tipAmount = tip(total)
        if total < 30:
            total = total + deliveryCharge + tipAmount + gst
        else:
            total = total + tipAmount + gst
    else:
        total = total + gst

    # print("The total is " + str(total))
    receipt(userDetails, orders, total)


# getDetails()
# getOrder()
# confirmOrder()
# studentDiscount()
getTotal()

