for i in range(10, -11, -1):
    print(i)





for i in range(1, 101):
    if i // 2 != 0:
        print(i)




correct_password = "goa123"
attempts = 3

while attempts > 0:
    password = input("Enter password: ")

    if password == correct_password:
        print("Password is correct!")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print("Password is incorrect! Try again")
            print("Remaining attempts:", attempts)
        else:
            print("No attempts left!")






