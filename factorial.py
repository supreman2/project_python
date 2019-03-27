def fact(i:int):
    print(i, end=' ')
    if i == 0:
        return 1
    return i*fact(i-1)

a = int(input("введите число: "))
print(fact(a), end=' ')
