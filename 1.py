def func(number):
    try:
        number = int(number)
        if number % 2 == 1:
            print("Even")
        else : print("Odd")
    except ValueError:
        print("Not a number")


string = input("Enter the number ")
func(string)
