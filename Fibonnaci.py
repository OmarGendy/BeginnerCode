def fibonnaci():
    num = int(input("How many Fibonnaci numbers do you want? "))
    fib_list = []
    if num == 0:
        print(fib_list)
    elif num == 1:
        fib_list.append(1)
        print(fib_list)
    else:
        for i in range(num):
            if i == 0 or i == 1:
                fib_list.append(1)
            else:
                fib_list.append(fib_list[i-1] + fib_list[i-2])
    print(fib_list)


fibonnaci()
