# L06-T3: Menu-based program for shopping list processing

shopping_list = []

def display_menu():
    print("Your shopping list contains the following products:")
    print(shopping_list)
    print("You can choose from the functions below:")
    print("1) Add")
    print("2) Remove")
    print("0) End")

def add_item():
    item = input("Enter the product to be added:\n")
    shopping_list.append(item)
    print()

def remove_item():
    if not shopping_list:
        print("Your shopping list is empty.")
        return
    print(f"You have {len(shopping_list)} items in your shopping list.")
    index = int(input("Enter the location of the product to be removed:\n")) - 1
    if 0 <= index < len(shopping_list):
        shopping_list.pop(index)
    print()
    
while True:
    display_menu()
    choice = input("Your choice:\n")
    if choice == '1':
        add_item()
    elif choice == '2':
        remove_item()
    elif choice == '0':
        print("You are going to buy the following products:")
        print(shopping_list)
        break
    else:
        print("Unknown selection.")
        print()
        

