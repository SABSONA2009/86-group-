num = int(input("enter your number: "))
num1 = int(input("enter your number: "))
num2 = int(input("enter your number: "))
num3 = int(input("enter your number: "))
num4 = int(input("enter your number: "))
num5 = int(input("enter your number: "))

num6 = num + num1 + num2 + num3 + num4 + num5

if num6 % 2 == 0:
    print("even")
else:
    print("odd")







total=int(input("enter your total: "))

if total >= 1500:
    print("შეგიძლიათ ლეპტოპის ყიდვა")
elif total >= 1000:



    print("შეგიძლიათ ტელეფონის ყიდვა")




elif total >= 100:
    print("შეგიძლიათ ფეხსაცმლის ყიდვა")


elif total >= 50:
    print("შეგიძლიათ პერანგის ყიდვა")


elif total >= 5:
    print("შეგიძლიათ რვეულის ყიდვა")
    
else:
    print("სამწუხაროდ, ვერ შეძლებთ არცერთი ნივთის ყიდვას")