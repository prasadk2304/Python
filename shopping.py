items = [ ]
price = [ ]

print("\nWelcome to D'Mart")

while True:
    n = int(input('''
                                    Select below actions to shop

                                    1. Add item to basket  
                                    2. Display basket
                                    3. Remove item from basket
                                    4. Total bill
                                    5. Discontinue shopping                            
'''))
    
    if n == 1:
        iname = input("Name of item : ")
        items.append(iname)
        ip = float(input("Enter price of item : "))
        price.append(ip)
    elif n == 2:
        if ( len(items)==0 or len(price)==0):
            print("Basket is empty")
        else:    
            print("Index No.   Item Name    Item Price")
            for index, (e, i) in enumerate(zip (items, price)):
                print(f"{index}.          {e}.          {i}/-")    
    elif n == 3:
        itd = int(input("Enter index no of the item that you want to remove from basket : "))
        if 0 <= itd < len(items):
            print(f"Item that you removed from basket is : {items.pop(itd)}")
        else :
            print("Invalid index number")
    elif n == 4:
        print("Index No.   Item Name    Item Price")
        for index, (e, i) in enumerate(zip (items, price)):
            print(f"{index}.          {e}.          {i}/-")
        print(f"Total                    {sum(price)}/-")
    elif n == 5:
        break       
print("Thank you for shopping")            




