# =============================================================================
# # Creation and Mainpulation of Arrays by using multiplication and addition
# # 08/23/21
# # CSC221 M1HW1 – Array Manipulations
# # Jeremy Locklear
# =============================================================================

# =============================================================================
# # The input of the program involves interacting with the menu function.
# # When the User enters 1 to create the array they are prompted to enter
# # integers. 
# # The Processing is taking that array and reshaping it into a 3x3 dataframe.
# # Then that original array is stored and can be mainpulated with other menu
# # options. When hitting 2-4 the array is mainpulated according to what is
# # corrisponding to. Menu 2 will square the array elements, menu 3 will add 4
# # to every element and menu 4 will multiply 6 to every element.
# # The output is the display of the first array from the creation, and the
# # other displays is showing the mainpulated array by the menu choices.
# #
# =============================================================================


import numpy as np


def main():
    """The Menu function that allows the starting of the program"""
    arr = []
    keep_going = 'y'
    while (keep_going.lower()=='y'):
        print("Main Menu")
        print()
        print("-"*10)
        print()
        print("1) Create 3 x 3 Array")
        print("2) Display cubed Values for elements in array")
        print("3) Add 7 to every element and display result")
        print("4) Multiply elements by 6 and display result")
        print("5) Exit")
        choice = int(input('Enter your choice: '))
        print()
        #Getting choices
        if choice == 1:
           arr = createArray()
           displayArray(arr)
        elif choice == 2:
             z = len(arr)
             if z >= 1:
                cubed = cubedArray(arr)
                displayArrayCubed(cubed)
             else:
                print("Create an array first before Continuing")
                print()
        elif choice == 3:
             z = len(arr)
             if z >= 1:
                total = additionArray(arr)
                displayAdditionArray(total)
             else:
                print("Create an array first before Continuing")
                print()
        elif choice == 4:
             z = len(arr)
             if z >= 1:
                product = multiplicationArray(arr)
                displayMultiplicationArray(product)
             else:
                print("Create an array first before Continuing")
                print()
        elif choice == 5:
            print("Program has Terminated")
            keep_going = 'n'
        else:
            print("Invalid Choice. Enter a Valid option.")
            input("Press any key to continue.")
            
def createArray():
    """This Function creates the array that is to be manipulated"""
    arrayList = []
    for x in range (3):
        for i in range(3):
            userInput = int(input("Enter a Integer: "))
            arrayList.append(userInput)
    creationArry = np.array(arrayList)
    newCreation = creationArry.reshape(3, 3)
    return newCreation


def displayArray(arr):
    """Displaying the Array that is to be mainpulated"""
    print()
    print()
    for x in (arr):
        for elem in x:
            print("{}".format(elem).rjust(3), end=" ")
        print(end="\n")
        print()
    
    
    
def cubedArray(arr):
    """Cubing of the original Array with itself"""
    cubed = arr**3
    return cubed

def displayArrayCubed(squared):
    """Displaying the Array that is to be mainpulated by cubing"""
    print()
    print()
    for x in (squared):
        for elem in x:
            print("{}".format(elem).rjust(3), end=" ")
        print(end="\n")
        print()

def additionArray(arr):
    """Adding 7 to the cubed array, and returning the new total""" 
    add = np.array([[7, 7, 7, 7, 7, 7, 7, 7, 7]])
    reshapeAdd = add.reshape(3,3)
    total = arr + reshapeAdd
    return total

def displayAdditionArray(total):
    """Displaying the Array that is to be mainpulated by addition"""
    print()
    print()
    for x in (total):
        for elem in x:
            print("{}".format(elem).rjust(3), end=" ")
        print(end="\n")
        print()
    
def multiplicationArray(arr):
    """Multiplying 6 to created array and returning the new product"""
    multiplication = np.array([[6,6,6,6,6,6,6,6,6]])
    reshapeProduct = multiplication.reshape(3,3)
    product = arr * reshapeProduct
    return product

def  displayMultiplicationArray(product):
    """Displaying the Array that is to be mainpulated by multiplication"""
    print()
    print()
    for x in (product):
        for elem in x:
            print("{}".format(elem).rjust(3), end=" ")
        print(end="\n")
        print()

if __name__ == "__main__":
    main()
