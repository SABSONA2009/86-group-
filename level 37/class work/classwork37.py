










def my_len(x):
    count = 0
    for _ in x:
        count += 1
    return count




def text(a,b):
    a=int(input("enter your num"))
    return print(text.insert(a))




def num(a,b):
   
    if a == "salami":
        print("you got it")









a=int(input("enter your number: "))
b=int(input("enter your number: "))
c=int(input("enter your number: "))

num = (a,b,c)





for num in range(a,b,c):

    print(num)



    






def len_clone(colection):
    if str != type(colection) != list:
        return "Error: Invalid arguments(function takes only str or list)"

    result = 0

    for _ in colection:
        result += 1
    return result

print(len_clone(True))



def find_clone(text, symbol, start_index = 0):
    for i in range(start_index, len(text)):
        if text[i] == symbol:
            return i
    return -1

print(find_clone("abcdabcd", "a", 5))





