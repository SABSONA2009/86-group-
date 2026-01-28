


name="saba salukvadze var me"

up_name=(name.upper())

print(up_name)


down=(name.lower())

print(down)


cap=(name.capitalize())

print(cap)


next=(name.title())

print(next)


find=(name.find(""))

print(find)


text = "hello world hello python"


index_o = text.find("o")
print(index_o)


first_l = text.find("l")
second_l = text.find("l", first_l + 1)
print(second_l)


index_x = text.find("x")
print(index_x)


index_world = text.find("world")
print(index_world)


print(text.find("java"))