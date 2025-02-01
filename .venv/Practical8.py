try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))

    print("x / y =", x/y)
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print("Something bad happened!\n", str(e))
finally:
    print("Program done!")