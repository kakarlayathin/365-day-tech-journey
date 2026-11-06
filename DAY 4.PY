#BASIC IF-ELSE
mark = 30
if mark >= 35:
    print("pass")
else:
    print("fail")

#if-elif-else [multy steps]
marks = 70
if marks >= 90:
    print("grade a")
elif marks >=70:
    print("grade b")
elif marks >= 50:
    print("grade c")
else:
    print("grade d")


# COMBING CONDITIONS BETWEEN AND , OR
print("\n----login check----")
user = "admin"
password = 1234
if user == "admin" and password == 1234:
    print("you can login")
else:
    print("you need valid Id")