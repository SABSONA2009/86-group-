# 1

# append() - სიის ბოლოში ამატებს ახალ ელემენტს
# insert() - სიის კონკრეტულ პოზიციაზე ამატებს ელემენტს
# pop() - შლის ელემენტს სიიდან (ნაგულისხმევად ბოლო ელემენტს)





numbers = [10, 20, 30, 40, 50]


print(len(numbers))







num1=int(input("enter your number: "))


num2=int(input("enter your number: "))


num3=int(input("enter your number: "))


num4=int(input("enter your number: "))


num5=int(input("enter your number: "))


number=(num1, num2, num3, num4, num5)



numbers.append(23)

print(numbers)

colors = ["red", "green", "blue", "yellow", "purple"]

colors.pop()  
print(colors)


animals = ["dog", "cat", "elephant", "lion"]

animals.insert(1, "monkey")
print(animals)



name1=(input("enter your name: "))

name2=(input("enter your name: "))

name3=(input("enter your name: "))



names=[name1, name2, name3]

names.insert(0,"teacher")

names.pop(3)
print(names)





def jami(a, b):
    return a + b


result = jami(5, 7)
print(result)



def num (a):
    return num % 2 == 0


result=num(5)


if num % 2 == 0:
    print("luwia")

else:
    print("kentia")

def kvadrati(a):
    return a ** 2


result=kvadrati(6)

print(result)



def didi_asoebi(text):
    return text.upper()


result = didi_asoebi("vai")
print(result)







def fullname(a,b):
    return a + b

result = fullname("saba", "salukvadze")


print(result)
