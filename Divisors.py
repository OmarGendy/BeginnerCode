def divisors(n):
    divs = range(2, n)
    final = []
    [final.append(i) for i in divs if n % i == 0]
    print(final)


num = int(input("Enter a number: "))
divisors(num)
