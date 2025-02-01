#Global Scope
hello = "Hello World!"

def getX():
    #Local Scope
    x = 10
    def printX():
        print("x =", x)
    printX()

print(hello)
getX()

print()
#Recrusion
def fact(n):
    if n == 0:
        return 1
    else:
        return n * fact(n - 1)

print("Factorial of 4 =", fact(4))

print()
#List Mutability
def addToList(list, value):
    list.append(value)

list = [1, 2, 3, 4]
addToList(list, 5)
addToList(list, 6)
print("Altered List:", list)
