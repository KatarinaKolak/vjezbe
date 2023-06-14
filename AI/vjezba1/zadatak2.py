num1 = 324518
num2 = 251238

number1_str = str(num1)
number2_str = str(num2)

flag = True

for i in range(len(number2_str)):
    result = number1_str.find(number2_str[i])
    if result == -1:
        print("Nisu iste znamenke!")
        flag = False
        break
    
if flag == True:
    print("Iste znamenke!")


