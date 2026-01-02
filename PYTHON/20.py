#"Shopping list manager" mini-project:
#Start with empty list.
#Keep asking user what to do in a while loop:
#"add" → ask for item name and add to list
#"remove" → ask which item to remove (by name)
#"show" → print current shopping list
#"quit" → exit the program
#(use if-elif inside while loop)
List=[]
while True:
    print("1.Add")
    print("2.Remove")
    print("3.Show")
    print("4.Quit")
    i=int(input("Enter choice:"))

    if i==1:
        add_item=str(input("Enter item:")).upper()
        List.append(add_item)
    elif i==2:
        remove_item=str(input("Enter item:")).upper()
        if (remove_item in List):
            List.remove(remove_item)
        else:
            print("Item not found")
    elif i==3:
        print(List)
    elif i==4:
        print("Quit")
        break
    else:
        print("Invalid Choice")
        break
