#Define the menu of restaurant 

menu = {
     'pasta':40,
     'shorma':90,
     'pizza':40,
     'combo pizza':150,
     'burger':60,
     'hotdog':25,
     'salad':35,
     'coffee':30,
     'Tea':10,
}

#Greet
print("WELCOME TO PYTHON RESTAURANT")
print("pizza: Rs-40\npasta: RS-40\ncombo pizza: Rs-150\nburger: RS-60\nhotdog: Rs-25\nsalad: RS-35\ncoffee: Rs-30\ntea: RS-10\n")

order_total = 0
#60 + 50 = 110
item_1 = input("Enter the name of item u want to order = ")
if item_1 in menu:
    order_total += menu[item_1] #0 + 90
    print(f"your item {item_1} has been added to your order")

else:
     print(f"ordered item {item_1} is not avaialabe!")

another_order = input("Do you want to add another item? (YES/NO) ")
if another_order =="Yes":
   item_2 =input("enter the name of second item = ")
   if item_2 in menu:
      order_total += menu[item_2]
      print(f"Item {item_2} has been added to order")
   else:
      print(f"ordered item {item_2} is not avaialable!")
      print(f"The total amount of items to pay is {order_total}")
