#  CSC 221
#  M1Lab1
#  Jeremy Locklear
#  08/18/21


def main():
    keep_going = 'y'
    while (keep_going.lower() == 'y'):
        
        print("Main Menu")
        print("-"*20)
        print("1) Double Numbers")
        print("2) Exit")
        
        user_choice = int(input("Enter a choice: "))
        
        if user_choice == 1:
            doubleNumber()
           
        elif user_choice == 2:
            keep_going = 'n'
            print("Program Terminated")
        else:
            print("Invalid Choice please hit Enter to continue")
            

def doubleNumber():
    """Input a number and the output is double of the user input"""
    numList = []
    
    keep_going = 0
    while (keep_going == 0):
        num = int(input("Enter a Number be doubled: "))
        doubling = num * 2
        print("The number doubled is:", doubling)
        print()
        
        validation = 0
        while validation == 0:
            print("1) Enter another number")
            print("2) Main Menu")
            user_input = int(input("Enter your Choice: "))
            print()
            
            if user_input == 1:
                validation += 1
                numList.append(num)
                numList.append(doubling)
                print(numList)
                doubleNumber()
            else:
                validation += 1
                numList.append(num)
                numList.append(doubling)
                print(numList)
                
        return numList
    

    



if __name__== "__main__":
    main()