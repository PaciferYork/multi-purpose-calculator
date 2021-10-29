'''
Make a faulty claculator which gives a wrong output as a calculations of ywo numbers.
'''
#
print("Welcome to the CalculateKaro.hum\n ")
print("What you want to calculate?" )
print("For Multiplication press 1 , For division press 2 , For addition press 3 , For subtraction press 4 , For power input press 5")

choice1 = int(input())


if choice1 == 1:
    print("You have to multiply.")
    print("Enter First number" )
    var1 = int(input())
    print("Enter Second number")
    var2 = int(input())
    print("On evaluating we get-")
    print(var1*var2)

elif choice1 == 2:
    print("You have to divide.")
    print("Enter First number")
    var3 = int(input())
    print("Enter Second number")
    var4 = int(input())
    print("On evaluating we get-")
    print(var3/var4)


elif choice1 == 3:
    print("You have to add.")
    print("Enter First number")
    var5 = int(input())
    print("Enter Second number")
    var6 = int(input())
    print("On evaluating we get-")
    print(var5+var6)

if choice1 == 4:
    print("You have to subtract.")
    print("Enter First number")
    var7 = int(input())
    print("Enter Second number")
    var8 = int(input())
    print("On evaluating we get-")
    print(var7-var8)

else:
    print("You have to calculate power.")
    print("Enter First number")
    var9 = int(input())
    print("Enter Second number")
    var10 = int(input())
    print("On evaluating we get-")
    print(var9**var10)



