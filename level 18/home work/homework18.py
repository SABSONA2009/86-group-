number = int(input("შეიყვანეთ რიცხვი: "))
result = 1

for i in range(1, number + 1):
    result *= i

print("ფაქტორიალი არის:", result)




print(10 % 3)  
print(8 % 2)   
print(7 % 2) 



num = 5

if num % 2 == 0:
    print("ლუწი რიცხვია")
else:
    print("კენტი რიცხვია")




number = int(input("შეიყვანეთ რიცხვი: "))

print("რიცხვის გამყოფებია:")

for i in range(1, number + 1):
    if number % i == 0:
        print(i)

