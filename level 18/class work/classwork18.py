
password="saba12345"
user_password=input("enter your password: ")

while user_password != password:
    print("this is not correct password: ")

    user_password=input("enter your password: ")

print("correct")





num = int(input("შეიყვანეთ რიცხვი: "))


if num > 50:
    print(num * 5)
else:
    print(num ** 2)



num = int(input("შეიყვანეთ რიცხვი: "))


num1 = 0


for i in range(1, num + 1):
    num1 += i


print(num,  num1 )