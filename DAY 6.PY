num1 = float(input("ENTER UR FIRST NUMBER: "))
operator = input("ENTER UR OPERATOR(+,-,*,/): ")
num2 = float(input("ENTER UR SECOND NUMBER: "))

if operator == "+":
    result = num1 + num2
    print(f"{num1} + {num2} = {num1 + num2}")
elif operator == "-":
    result = num1 - num2
    print(f"{num1} - {num2} = {num1 - num2}")
elif operator == "*":
    result = num1 * num2
    print(f"{num1} * {num2} = {num1 * num2}")
elif operator == "/":
    if num2 == 0:
        print("error:the division cant be done")
    else:
        result = num1 / num2
        print(f"{num1} / {num2} = {num1 / num2}")
else:
    print("sorry the opeator doent match please check")