# type() ფუნქცია გვიჩვენებს, თუ რა მონაცემთა ტიპისაა ცვლადი ან მნიშვნელობა


num1 = 10
print(type(num1)) 


num2 = 3.14
print(type(num2))  


name = "Giorgi"
print(type(name)) 


apple = True

print(type(apple))








print(int("5"))     
print(int(3.9))     
print(int(True)) 


print(float(5))        
print(float("3.2"))    
print(float(False)) 


print(str(10))       
print(str(3.14))      
print(str(True))

# Data Conversion ნიშნავს ერთი მონაცემთა ტიპის გადაყვანას მეორეში

num1 = int(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = int(input("შეიყვანეთ მეორე რიცხვი: "))
num3 = int(input("შეიყვანეთ მესამე რიცხვი: "))


print(num1 + num2 + num3)


num1_str = str(num1)
num2_str = str(num2)
num3_str = str(num3)


print(num1_str + num2_str + num3_str)




name = input("შეიყვანეთ თქვენი სახელი: ")

number = int(input("შეიყვანეთ მთელი რიცხვი: "))


print(name * number)
