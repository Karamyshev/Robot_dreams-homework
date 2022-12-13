a = input("Enter string or number: ")
if a.isdigit():
    if int(a) % 2 == 0:
        print("The entered data is an even number")
    else:
        print("The entered data is an odd number")
else:
    print("The entered data is a word, its lenght is " + str(len(a)))
